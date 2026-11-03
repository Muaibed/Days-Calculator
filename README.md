# Days-Calculator

A simple command-line Python program that takes two dates and calculates the number of days between them.

## Features

- Prompts for a start date and an end date in `DD-MM-YYYY` format
- Validates each date, including the correct number of days per month
- Handles leap years (29 days in February for leap years)
- Asks again until valid dates are entered
- Prints the difference between the two dates in days

## Requirements

- Python 3.6 or newer
- No external packages (uses only the standard library `datetime` module)

## Usage

Clone the repository and run the script:

```bash
git clone https://github.com/muaibed/days-calculator.git
cd days-calculator
python3 main.py
```

## Example

```
Enter the start date as 'DD-MM-YYYY':01-01-2024
Enter the end date as 'DD-MM-YYYY':01-03-2024
Difference is 60 days
```

## Notes

- Enter days and months with two digits (e.g. `05-03-2024`, not `5-3-2024`).
- If the end date is earlier than the start date, the result is negative.
