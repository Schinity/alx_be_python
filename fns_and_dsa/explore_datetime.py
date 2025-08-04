from datetime import datetime, timedelta

def display_current_datetime():
    """
    Prints the current date and time in both raw and formatted forms.

    The formatted date is displayed in the "YYYY-MM-DD HH:MM:SS" format.
    """
    current_date = datetime.datetime.now()
    print("Current date and time:", current_date)
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Formatted date:", formatted_date)
display_current_datetime()

def calculate_future_date():
    """
    Prompts the user for a number of days to add to the current date,
    calculates the future date, and prints it in "YYYY-MM-DD" format.
    """
    current_date = datetime.now()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=number_of_days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
calculate_future_date()