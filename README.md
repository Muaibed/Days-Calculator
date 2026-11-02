# Days-Calculator

A small command-line Python program that takes two dates and tells you how many days are between them.

## Features

- Asks for a start date and an end date in `DD-MM-YYYY` format
- Checks that each date is valid: the day has to exist in that month, and leap years are handled, so `29-02-2024` is accepted and `29-02-2023` is not
- Keeps asking until you enter valid dates
- Prints the number of days between the two dates

## Requirements

- Python 3.6 or newer (the program uses f-strings)
- Nothing else to install: it uses only the standard library (`datetime`)

## Getting started

```bash
git clone https://github.com/muaibed/Days-Calculator.git
cd Days-Calculator
python3 main.py
```

## Usage

Run the program and type the two dates when asked:

```
$ python3 main.py
Enter the start date as 'DD-MM-YYYY':01-01-2024
Enter the end date as 'DD-MM-YYYY':01-03-2024
Difference is 60 days
```

### Input notes

- Use the format `DD-MM-YYYY` with dashes, for example `05-09-2023`.
- Write the day and month with two digits (`05`, not `5`).
- If the end date comes before the start date, the result is negative (for example `-9 days`).

## How it works

1. `main()` reads both dates, splits each into day, month and year, and checks them. For February it applies the leap-year rule: divisible by 4, except century years, which must be divisible by 400.
2. Once both dates are valid, `calculator()` turns them into `datetime` objects with `datetime.strptime(date, '%d-%m-%Y')`, subtracts the start from the end, and returns the difference in days.

## Project structure

```
Days-Calculator/
├── main.py     # the program: input checks and day calculation
└── README.md   # this file
```
