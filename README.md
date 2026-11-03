# Days-Calculator

A small command-line Python program that calculates the number of days between two dates.

## Features

- Prompts for a start date and an end date in `DD-MM-YYYY` format
- Checks that each date is valid, including the number of days in each month and leap years (29 February)
- Asks for the dates again if either one is invalid
- Prints the difference between the two dates in days

## Requirements

- Python 3.6 or later
- No third-party packages (only the standard library `datetime` module)

## Usage

```bash
python3 main.py
```

Example session:

```
Enter the start date as 'DD-MM-YYYY':01-01-2024
Enter the end date as 'DD-MM-YYYY':01-03-2024
Difference is 60 days
```

## Notes

- Write the month with two digits, e.g. `05-03-2024` rather than `05-3-2024`.
- If the end date is before the start date, the result is negative (e.g. `-9 days`).
