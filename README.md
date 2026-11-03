# Days-Calculator

A small command-line Python program that asks for two dates and tells you how many days are between them.

## Requirements

- Python 3.6 or newer
- No extra packages (it uses only the built-in `datetime` module)

## How to run

```bash
python3 main.py
```

The program asks for two dates in `DD-MM-YYYY` format:

```
Enter the start date as 'DD-MM-YYYY':01-01-2024
Enter the end date as 'DD-MM-YYYY':01-03-2024
Difference is 60 days
```

## How it works

1. **Input:** you enter a start date and an end date.
2. **Validation:** each date is checked before calculating:
   - the year must be a positive number
   - the month must be between `01` and `12`
   - the day must exist in that month (30 or 31 days, and 28 or 29 for February)
   - leap years are handled: a year divisible by 4 is a leap year, unless it is divisible by 100 but not by 400
3. **Calculation:** the dates are turned into `datetime` objects and subtracted; the result is printed in days.

If a date is not valid, an error message is shown and you are asked to enter both dates again.

## Notes

- Write the day and month with two digits, for example `05-03-2024`, not `5-3-2024`.
- If the end date is before the start date, the result is a negative number.

## Project structure

```
Days-Calculator/
├── main.py     # the program: input, validation and calculation
└── README.md   # this file
```
