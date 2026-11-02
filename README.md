# Days-Calculator

A small command-line Python program that asks for two dates and tells you how many days are between them.

## Requirements

- Python 3.6 or newer (the script uses f-strings)
- No third-party packages; only the standard library `datetime` module

## Usage

Run the script from the project folder:

```bash
python3 main.py
```

You will be asked for a start date and an end date, both in `DD-MM-YYYY` format:

```text
Enter the start date as 'DD-MM-YYYY':01-01-2024
Enter the end date as 'DD-MM-YYYY':01-03-2024
Difference is 60 days
```

If the end date is earlier than the start date, the result is negative:

```text
Enter the start date as 'DD-MM-YYYY':15-06-2024
Enter the end date as 'DD-MM-YYYY':01-01-2024
Difference is -166 days
```

## How it works

1. **Input validation:** `main()` splits each date on `-` and checks that:
   - the year is a positive number,
   - the month is between 1 and 12,
   - the day fits the month (30 or 31 days, and 28 or 29 for February depending on leap years).

   If a date is invalid, an error message is printed and you are asked for both dates again.
2. **Calculation:** `calculator()` parses both dates with `datetime.strptime(..., '%d-%m-%Y')`, subtracts the start date from the end date, and returns the difference in days.

### Leap years

A year is a leap year (February has 29 days) when it is divisible by 4, except for years divisible by 100 that are not also divisible by 400. For example, 2000 and 2024 are leap years, but 1900 is not.

## Input tips and known limitations

- Use two digits for the day and month, e.g. `05-03-2024` rather than `5-3-2024`. Day-of-month checks are matched against zero-padded month values such as `03`.
- Input must contain exactly two `-` separators. Something like `2024/03/05` will crash the program with an error instead of asking again.
- The input loop stops as soon as either date passes validation, so an invalid date can still reach `datetime.strptime` and raise a `ValueError`.

## Project structure

```text
Days-Calculator/
├── main.py     # input handling, validation and the day calculation
└── README.md
```
