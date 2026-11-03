# Days-Calculator

A small command-line Python program that takes two dates and tells you how many days lie between them.

## Features

- Asks for a start date and an end date in `DD-MM-YYYY` format
- Checks that each date is valid, including the correct number of days in each month
- Handles leap years (29 February is accepted only in leap years)
- Asks again if a date is not valid
- Prints the difference in days

## Requirements

- Python 3.6 or later (it uses f-strings)
- No third-party packages; only the standard `datetime` module

## Getting started

```bash
git clone https://github.com/muaibed/days-calculator.git
cd days-calculator
python3 main.py
```

## Usage

Run the script and enter the two dates when asked:

```text
$ python3 main.py
Enter the start date as 'DD-MM-YYYY':01-01-2024
Enter the end date as 'DD-MM-YYYY':01-03-2024
Difference is 60 days
```

### Input format

- Use two digits for the day and month, and four for the year, separated by dashes: `05-09-2023`, not `5-9-2023`.
- If the end date is before the start date, the result is negative.

## How it works

1. `main()` reads both dates, splits them into day, month and year, and checks that each part is in range for that month and year.
2. Once the input is valid, `calculator()` turns both strings into `datetime` objects with `datetime.strptime(..., '%d-%m-%Y')`, subtracts them, and returns the number of days.

## Project structure

```text
Days-Calculator/
├── main.py     # input, validation and calculation
└── README.md
```

## Contributing

Issues and pull requests are welcome.
