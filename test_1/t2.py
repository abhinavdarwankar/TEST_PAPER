import calendar

def print_calendar(year, month):
    # Create a plain text calendar
    cal = calendar.month(year, month)
    print(cal)

# Get user input for year and month
year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))

# Print the calendar for the given month and year
print_calendar(year, month)
