The Open e-commerce dataset contains data about people's Amazon.com purchases. To collect the data, the researchers asked participants to fill out a survey. Only participants who completed the survey were recorded in the data. In one part of the survey, participants were given instructions to download their Amazon purchase history and share it with the researchers. Since this step was not required, not all participants shared their Amazon purchase history with the researchers. The dataset contains two tables, `df` and `survey`. The `df` table was created from participants' purchase history and records individual items purchased from Amazon.

<center><img src="../../assets/images/sp24-final/df.png" style="width: 100%; height: auto;"></center>


- `"date" (pd.Timestamp)`: The date that the purchase was made.

- `"code" (float)`: Cost of one item in US dollars.

- `"q" (float)`: Quantity of items purchased in the order.

- `"state" (str)`: US state where the order was shipped. If the item was an electronic gift card, the researchers recorded `NaN`.

- `"name" (str)`: Name of the item.

- `"cat" (str)`: Category of the item.

- `"id" (str)`: Participant ID.

<center><img src="../../assets/images/sp24-final/survey.png" style="width: 100%; height: auto;"></center>


- `"id" (str)`: Participant ID. Some values in this column don't appear in the `id` column of `df`.

- `"age" (str)`: Age of participant.

- `"income" (str)`: Income of participant.

- `"state" (str)`: US state where order was shipped.

- `"marijuana" (str)`: Whether the participant reported that they smoke marijuana (Yes) or don't smoke marijuana (No).

- `"diabetes" (str)`: Whether the participant reported that they have diabetes (Yes) or don't have diabetes (No).
