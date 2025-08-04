import datetime

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
    current_date = datetime.datetime.now()
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    new_date = current_date + datetime.timedelta(days=number_of_days)
    future_date = new_date.strftime("%Y-%m-%d")
    print("Future date:", future_date)
calculate_future_date()