FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.

    Parameters:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature converted to Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.

    Parameters:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature converted to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def display_conversion(fahrenheit):
    """
    Prints the conversion of a Fahrenheit temperature to Celsius.

    Parameters:
        fahrenheit (float): Temperature in Fahrenheit.
    """
    celsius = convert_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is {celsius}°C")

def display_conversion_from_celsius(celsius):
    """
    Prints the conversion of a Celsius temperature to Fahrenheit.

    Parameters:
        celsius (float): Temperature in Celsius.
    """
    fahrenheit = convert_to_fahrenheit(celsius)
    print(f"{celsius}°C is {fahrenheit}°F")

def main():
    """
    Main function to run the temperature conversion tool.

    Prompts the user for a temperature and its unit, performs the conversion,
    and displays the result. Raises an error for invalid temperature input.
    """
    try:
        temperature_to_convert = float(input("Enter the temperature to convert: "))
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    celsius_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if celsius_or_fahrenheit == 'C':
        display_conversion_from_celsius(temperature_to_convert)
    elif celsius_or_fahrenheit == 'F':
        display_conversion(temperature_to_convert)
    else:        
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.") 

if __name__ == "__main__":
    main()