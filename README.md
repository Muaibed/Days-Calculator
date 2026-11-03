# Days-Calculator

A small command-line Python program that takes two dates and tells you how many days are between them.

## Requirements

- Python 3.6 or newer (it uses f-strings)
- No third-party packages; only the standard library `datetime` module

## Usage

Run the script from the project folder:

```bash
python3 main.py
```

You will be asked for two dates in `DD-MM-YYYY` format:

```
Enter the start date as 'DD-MM-YYYY':01-01-2024
Enter the end date as 'DD-MM-YYYY':01-03-2024
Difference is 60 days
```

If the end date is earlier than the start date, the result is negative.

## Input rules

- Use dashes between the parts: `DD-MM-YYYY`.
- Write the month with two digits (`03`, not `3`).
- The day must exist in that month. Leap years are handled, so `29-02-2024` is accepted but `29-02-2023` is not.
- If a date is invalid, an error message is printed and you are asked to enter the dates again.

## How it works

1. `main()` reads both dates, splits each into day, month and year, and checks that they form a real calendar date.
2. `calculator()` turns the two strings into `datetime` objects with `datetime.strptime(..., '%d-%m-%Y')`, subtracts them, and returns the number of days.

## Project structure

```
Days-Calculator/
├── main.py     # input, validation and day calculation
└── README.md
```
