# latex-to-md.py
# Converts an exam .tex file to a set of .md files, one for each problem
# Usage: python latex-to-md.py exam.tex out_folder
# out_folder is the slug (e.g. wi26-final); files are written to ../problems/{slug}/
# Requires pandoc. After running, review images and any complex layout by hand.

import os
import re
import sys


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read()


def strip_comments(tex):
    """Remove LaTeX comments, preserving escaped \\%."""
    lines = []
    for line in tex.splitlines():
        out = []
        i = 0
        while i < len(line):
            if line[i] == '%' and (i == 0 or line[i - 1] != '\\'):
                break
            out.append(line[i])
            i += 1
        lines.append(''.join(out))
    return '\n'.join(lines)


def extract_trailing_comment_solutions(tex):
    """Turn trailing % solution comments on a line into soln blocks."""
    hints = []

    def repl(line):
        m = re.search(r'%\s*(.+)$', line)
        if not m:
            return line
        hint = m.group(1).strip()
        skip = {'this one', 'this one.', 'lower, overfitting', 'increases bias, decreases variance'}
        if hint.lower().startswith('this one'):
            return re.sub(r'%.*$', '', line)
        if any(k in hint.lower() for k in ('lower', 'overfitting', 'increases', 'decreases', 'higher', 'underfitting')):
            hints.append(hint)
            return re.sub(r'%.*$', '', line)
        return line

    tex = '\n'.join(repl(line) for line in tex.splitlines())
    return tex, hints


def clean_latex_text(s):
    s = s.strip()
    s = s.replace(r'\{', '{').replace(r'\}', '}')
    s = re.sub(r'\\texttt\{([^}]*)\}', r'`\1`', s)
    s = re.sub(r'\\textbf\{([^}]*)\}', r'**\1**', s)
    s = re.sub(r'\\textit\{([^}]*)\}', r'*\1*', s)
    s = re.sub(r'\\_', '_', s)
    s = re.sub(r'\\\\', '\n', s)
    s = re.sub(r'\s+', ' ', s)
    return s.strip()


def extract_braced(tex, start_idx):
    """Return (inner_text, end_index) for content inside { ... } starting at start_idx."""
    if start_idx >= len(tex) or tex[start_idx] != '{':
        return '', start_idx
    depth = 0
    i = start_idx
    while i < len(tex):
        ch = tex[i]
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                return tex[start_idx + 1 : i], i + 1
        i += 1
    return tex[start_idx + 1 :], len(tex)


def replace_inlineresponseboxes(tex, solutions):
    """Extract answers from \\inlineresponsebox and \\biginlineresponsebox."""

    def repl(match):
        cmd = match.group(1)
        opt_end = match.end()
        # skip optional [...]
        idx = opt_end
        if idx < len(tex) and tex[idx] == '[':
            close = tex.find(']', idx)
            idx = close + 1 if close != -1 else idx
        if idx < len(tex) and tex[idx] == '{':
            content, end = extract_braced(tex, idx)
            cleaned = clean_latex_text(content)
            if cleaned and cleaned not in ('', 'N'):
                solutions.append(f'**Answer:** {cleaned}')
            return ''
        return match.group(0)

    for cmd in ('inlineresponsebox', 'biginlineresponsebox'):
        pattern = rf'\\{cmd}\[[^\]]*\]'
        while True:
            m = re.search(pattern, tex)
            if not m:
                break
            cmd_start = m.start()
            idx = m.end()
            if idx < len(tex) and tex[idx] == '{':
                content, end = extract_braced(tex, idx)
                cleaned = clean_latex_text(content)
                if cleaned and cleaned not in ('', 'N'):
                    solutions.append(f'**Answer:** {cleaned}')
                tex = tex[:cmd_start] + tex[end:]
            else:
                tex = tex[:cmd_start] + tex[m.end():]
    return tex


def replace_correct_variants(block):
    """Turn \\correctbubble into \\bubble (etc.) while collecting answers."""
    correct = []
    for wrong, right in (('correctsquarebubble', 'squarebubble'), ('correctbubble', 'bubble')):
        pattern = rf'\\{wrong}\{{'
        while True:
            m = re.search(pattern, block)
            if not m:
                break
            brace_start = m.end() - 1
            content, end = extract_braced(block, brace_start)
            correct.append(clean_latex_text(content))
            block = block[: m.start()] + f'\\{right}{{{content}}}' + block[end:]
    return block, correct


def remove_latex_cmd(tex, cmd, on_match=None):
    """Remove all \\cmd{...} occurrences; optionally collect inner content."""
    pattern = rf'\\{cmd}\{{'
    out = []
    pos = 0
    collected = []
    while pos < len(tex):
        m = re.search(pattern, tex[pos:])
        if not m:
            out.append(tex[pos:])
            break
        start = pos + m.start()
        out.append(tex[pos:start])
        brace_start = pos + m.end() - 1
        content, end = extract_braced(tex, brace_start)
        if on_match:
            collected.append(content)
        pos = end
    return ''.join(out), collected


def process_subprob_block(block):
    solutions = []

    def responsebox_repl(m):
        content = clean_latex_text(m.group(1))
        if content:
            solutions.append(f'**Answer:** `{content}`' if '`' not in content else f'**Answer:** {content}')
        return ''

    block = re.sub(
        r'\\begin\{responsebox\}\{[^}]*\}(.*?)\\end\{responsebox\}',
        responsebox_repl,
        block,
        flags=re.DOTALL,
    )

    block = replace_inlineresponseboxes(block, solutions)

    if 'how = "inner"' in block:
        block = re.sub(r'\\begin\{tabular\}.*?\\end\{tabular\}', '', block, flags=re.DOTALL)

    block, correct_raw = replace_correct_variants(block)
    correct = [clean_latex_text(c) for c in correct_raw]

    if correct:
        if len(correct) == 1:
            solutions.append(f'**Answer:** {correct[0]}')
        else:
            solutions.append('**Answer:** ' + ', '.join(correct))

    if solutions:
        block += '\n\\begin{soln}\n' + '\n\n'.join(solutions) + '\n\\end{soln}\n'

    return block


def preprocess_tex(tex):
    m = re.search(r'\\begin\{probset\}(.*)\\end\{probset\}', tex, re.DOTALL)
    if not m:
        raise ValueError('Could not find \\\\begin{probset} ... \\\\end{probset}')
    tex = m.group(1)

    tex, hint_solutions = extract_trailing_comment_solutions(tex)

    # images -> markdown image syntax pandoc can handle
    tex = re.sub(
        r'\\includegraphics\[[^\]]*\]\{([^}]+)\}',
        lambda m: f'\n\\begin{{center}}\n\\includegraphics{{{m.group(1)}}}\n\\end{{center}}\n',
        tex,
    )

    # process each subprob
    def subprob_repl(m):
        return '\\begin{subprob}' + process_subprob_block(m.group(1)) + '\\end{subprob}'

    tex = re.sub(r'\\begin\{subprob\}(.*?)\\end\{subprob\}', subprob_repl, tex, flags=re.DOTALL)

    # problems without subprobs but with soln at end (e.g. pipeline Q)
    return tex, hint_solutions


def replace_tags(prob_str):
    tags = {
        'probset': '',
        'prob': 'PROB',
        'soln': 'SOLUTION',
        'subprob': 'SUBPROB',
        'subprobset': '',
    }

    for tag, label in tags.items():
        latex_brace = '{' + tag + '}'
        prob_str = prob_str.replace(
            f'\\begin{latex_brace}',
            f'# BEGIN {label}\n\n' if label else '',
        ).replace(
            f'\\end{latex_brace}',
            f'\n\n# END {label}' if label else '',
        )

    prob_str = re.sub(r'\\begin\{prob\}\[[^\]]*\]', '# BEGIN PROB\n\n', prob_str)
    prob_str = re.sub(r'\\\[.*?pts.*?\]', '', prob_str)
    prob_str = re.sub(r'(\[)?\(\d+ pts?\)(\])?', '', prob_str)

    regex_map = {
        r'\\bubble\{(.*)\}': '( )',
        r'\\squarebubble\{(.*)\}': '[ ]',
    }

    def make_repl(mc_bubble):
        pattern = mc_bubble

        def repl(matchobj):
            inner = re.search(pattern, matchobj.group(0))
            text = inner.group(1) if inner else ''
            return regex_map[pattern] + ' ' + text

        return repl

    for mc_bubble in regex_map:
        prob_str = re.sub(mc_bubble, make_repl(mc_bubble), prob_str)

    return prob_str


def pandoc_tex_to_md(prob_str_tex, work_dir):
    tex_path = os.path.join(work_dir, 'temp.tex')
    md_path = os.path.join(work_dir, 'temp.md')
    wrapped = (
        '\\documentclass{article}\n'
        '\\usepackage{amsmath}\n'
        '\\usepackage{amssymb}\n'
        '\\begin{document}\n'
        + prob_str_tex
        + '\n\\end{document}\n'
    )
    with open(tex_path, 'w') as f:
        f.write(wrapped)
    rc = os.system(f'pandoc -s "{tex_path}" -o "{md_path}"')
    if rc != 0 or not os.path.exists(md_path):
        raise RuntimeError('pandoc failed to convert LaTeX chunk')
    with open(md_path, 'r') as f:
        text = f.read()
    os.remove(tex_path)
    os.remove(md_path)
    return text


def convert_prob_block(prob_tex, utils_dir, slug):
    prob_tex = replace_tags(prob_tex)
    md = pandoc_tex_to_md(prob_tex, utils_dir)
    md = remove_leading_slash(md)
    return postprocess_md(md, slug)


def remove_leading_slash(prob_str_md):
    return (
        prob_str_md.replace('\\#', '#')
        .replace('\\[X\\]', '[X]')
        .replace('\\(X\\)', '(X)')
        .replace('\\[ \\]', '[ ]')
        .replace('\\( \\)', '( )')
    )


def postprocess_md(md, slug):
    img_map = {
        'imgs/scatter1.png': f'../../assets/images/{slug}/scatter1.png',
        'imgs/scatter2.png': f'../../assets/images/{slug}/scatter2.png',
        'imgs/preview.jpg': f'../../assets/images/{slug}/preview.jpg',
        'imgs/wait.jpg': f'../../assets/images/{slug}/wait.jpg',
    }

    for src, dst in img_map.items():
        md = md.replace(src, dst)
        md = re.sub(
            rf'!\[.*?\]\({re.escape(dst)}.*?\)',
            f'<center><img src="{dst}" width=450></center>',
            md,
        )

    md = re.sub(r'\\\[.*?\\\]', '', md)
    md = re.sub(r'\\\[.*?pts.*?\\\]', '', md)
    md = re.sub(r':::+\s*responsebox.*?:::', '', md, flags=re.DOTALL)
    md = re.sub(r':::+\s*center\s*:::', '', md)
    md = re.sub(r':::+\s*minipage.*?:::', '', md, flags=re.DOTALL)
    md = re.sub(r'# END SUBPROB\s+# BEGIN SUBPROB', '# END SUBPROB\n\n# BEGIN SUBPROB', md)

    # one MC option per line when multiple on same line
    md = re.sub(
        r'((?:\( \)|\[ \]) [^\n]+)( (?:(?:\( \)|\[ \]) ))',
        lambda m: re.sub(r' (?=(?:\( \)|\[ \]) )', '\n', m.group(0)),
        md,
    )

    # move # BEGIN SOLUTION from latex soln tags
    md = re.sub(r'# BEGIN SOLUTION\s+# END SOLUTION', '', md)

    # merge duplicate empty solution blocks with preceding soln content from pandoc
    md = re.sub(
        r'(# BEGIN SOLUTION\n\n)(.*?)(\n# END SOLUTION)',
        lambda m: m.group(0) if m.group(2).strip() else '',
        md,
        flags=re.DOTALL,
    )

    # convert ``` blocks to ```py where they look like python
    md = re.sub(
        r'```\s*\n((?:    )?(?:med|def |import |X =|y =|pl\.|dr_z|corpus|list\())',
        r'```py\n\1',
        md,
        flags=re.MULTILINE,
    )

    # Remove blank lines between consecutive MC options (required by run.py)
    md = re.sub(
        r'(^(\( \)|\[ \]).+$\n)\n+(?=^(\( \)|\[ \]))',
        r'\1',
        md,
        flags=re.MULTILINE,
    )

    md = re.sub(r'\\\*\\\*Answer:\\\*\\\*', '**Answer:**', md)
    md = re.sub(r'\\\*\\\*Answers:\\\*\\\*', '**Answers:**', md)
    md = md.replace(r'\_', '_')
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip() + '\n'


def split_probs_to_files(prob_str_md):
    probs = re.findall(r'# BEGIN PROB[\W\w]*?# END PROB', prob_str_md)
    new_probs = []
    for prob in probs:
        if '# END SUBPROB' in prob:
            # only add empty solution wrapper if subprob has no solution yet
            def add_soln_if_missing(match):
                chunk = match.group(0)
                if '# BEGIN SOLUTION' in chunk and re.search(
                    r'# BEGIN SOLUTION\n\n.+?\n# END SOLUTION', chunk, re.DOTALL
                ):
                    return chunk
                return chunk.replace(
                    '# END SUBPROB',
                    '# BEGIN SOLUTION\n\n# END SOLUTION\n\n# END SUBPROB',
                )

            prob = re.sub(r'# BEGIN SUBPROB[\W\w]*?# END SUBPROB', add_soln_if_missing, prob)
        else:
            if '# BEGIN SOLUTION' not in prob:
                prob = prob.replace(
                    '# END PROB',
                    '# BEGIN SOLUTION\n\n# END SOLUTION\n\n# END PROB',
                )
        new_probs.append(prob)
    return new_probs


def write_prob_files(probs, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    slug = os.path.basename(out_dir)
    for i, prob in enumerate(probs):
        save_file_name = os.path.join(out_dir, f'{slug}-q{str(i + 1).zfill(2)}.md')
        with open(save_file_name, 'w') as f:
            f.write(prob)


def extract_between_prob1_and_prob2(full_tex):
    """Text after Q1 that introduces the Wait column."""
    m = re.search(
        r'\\end\{prob\}\s*\\newpage\s*(.*?)\\begin\{prob\}\[\(M\) - 10 pts\]',
        full_tex,
        re.DOTALL,
    )
    if not m:
        return ''
    text = m.group(1)
    text = strip_comments(text)
    text = replace_tags(text)
    md = pandoc_tex_to_md(text, os.path.dirname(os.path.abspath(__file__)))
    md = remove_leading_slash(md)
    md = postprocess_md(md, 'wi26-final')
    return md.strip()


if __name__ == '__main__':
    if len(sys.argv[1:]) != 2:
        raise ValueError('Usage: python latex-to-md.py exam.tex slug (e.g. wi26-final)')

    file_path = sys.argv[1]
    slug = sys.argv[2]
    utils_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(utils_dir, '..', 'problems', slug)

    file_as_tex = read_file(file_path)
    between_q1_q2 = extract_between_prob1_and_prob2(file_as_tex)

    prob_str_tex, _ = preprocess_tex(strip_comments(file_as_tex))
    prob_blocks = re.findall(r'\\begin\{prob\}.*?\\end\{prob\}', prob_str_tex, re.DOTALL)

    probs = []
    for block in prob_blocks:
        md = convert_prob_block(block, utils_dir, slug)
        md = split_probs_to_files(md)[0] if '# BEGIN PROB' in md else md
        probs.append(md)

    if between_q1_q2 and probs:
        probs[0] = probs[0].replace('# END PROB', between_q1_q2 + '\n\n# END PROB')

    write_prob_files(probs, out_dir)
    print(f'Wrote {len(probs)} problems to {out_dir}')
