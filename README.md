# Days-Calculator

A small command-line Python program that takes two dates and tells you how many days are between them.

## Features

- Prompts for a start date and an end date in `DD-MM-YYYY` format
- Checks that each date is valid: month between 1 and 12, and the right number of days for that month
- Handles leap years (29 days in February when the year is divisible by 4, except century years not divisible by 400)
- Asks for the dates again if they are not valid
- Prints the difference in days

## Requirements

- Python 3.6 or newer (the code uses f-strings)
- No external packages; it only uses the standard library `datetime` module

## Usage

Clone the repository and run the script:

```bash
git clone https://github.com/muaibed/Days-Calculator.git
cd Days-Calculator
python3 main.py
```

Then enter the two dates when asked:

```text
Enter the start date as 'DD-MM-YYYY':01-01-2024
Enter the end date as 'DD-MM-YYYY':01-03-2024
Difference is 60 days
```

## Notes

- Write the day and month with two digits, e.g. `05-03-2024` rather than `5-3-2024`.
- The result is `end date - start date`, so if the end date comes before the start date the result is negative (for example, `10-05-2024` to `01-05-2024` gives `-9 days`).

## Project structure

```text
Days-Calculator/
├── main.py     # Input, date validation and the day calculation
└── README.md
```
