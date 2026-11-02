# Days Calculator — Detailed Guide

A small command-line Python program that asks for two dates and tells you how many days lie between them.

For the short summary, see [README.md](README.md).

## Requirements

- Python 3.6 or newer (the program uses f-strings)
- No third-party packages; it uses only the standard `datetime` module

## Running the program

From the project folder:

```bash
python3 main.py
```

The program asks for two dates:

```
Enter the start date as 'DD-MM-YYYY':01-01-2024
Enter the end date as 'DD-MM-YYYY':01-03-2024
Difference is 60 days
```

## Date format

Enter each date as `DD-MM-YYYY`: day, month and year separated by dashes.

| Part  | Rule                                      | Example |
|-------|-------------------------------------------|---------|
| Day   | Must exist in the given month             | `09`    |
| Month | Two digits, `01` to `12`                  | `03`    |
| Year  | A positive whole number                   | `2024`  |

Write the month with two digits (`03`, not `3`). The program checks the month as text against `01`–`12`, so a one-digit month is not recognised and you are asked for the dates again.

## How it works

1. **Input:** `main()` reads the start and end dates and splits each one on `-` into day, month and year.
2. **Validation:** each part is checked. The day limit depends on the month (30 or 31 days), and February allows 29 days in leap years. A year is a leap year if it is divisible by 4, except century years, which must be divisible by 400 (so 2000 is a leap year and 1900 is not).
3. **Calculation:** `calculator()` turns both strings into `datetime` objects with `datetime.strptime(..., '%d-%m-%Y')`, subtracts the start date from the end date, and returns the number of days.

## Reading the result

- The result is **end date minus start date**.
- If the end date comes before the start date, the result is negative. For example, `15-06-2024` to `01-01-2024` gives `-166 days`.
- The start day is not counted, so `01-01-2024` to `02-01-2024` gives `1 day`.

## Known limitations

- **One valid date ends the input loop.** The loop stops when either date passes validation, even if the other one fails. If one date is invalid (for example `29-02-2023`), the error is printed and the program then crashes with `ValueError: day is out of range for month`.
- **Badly shaped input crashes the program.** Input without two dashes, such as `2024/01/01`, raises an `IndexError`.
- **One-digit months are not accepted** (see [Date format](#date-format)).

## Project structure

```
Days-Calculator/
├── main.py              # input, validation and calculation
├── README.md            # short project summary
└── README-DETAILED.md   # this guide
```
