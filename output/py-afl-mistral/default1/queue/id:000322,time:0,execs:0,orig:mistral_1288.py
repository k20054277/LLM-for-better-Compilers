
def convert_temperature(kelvin):
    """
    This function converts Kelvin temperature to Celsius or Fahrenheit based on user input.
    :param kelvin: The given temperature in Kelvin
    :return: Temperature value in Celsius or Fahrenheit
    """

    # Get temperature unit from user
    unit = input("Enter temperature unit (C for Celsius, F for Fahrenheit): ").upper()

    if unit == "C":
        # Convert Kelvin to Celsius using assert statement for validation
        celsius = assert(kelvin >= 0, "Kelvin value should be greater than or equal to zero") if kelvin is not None else None
        temperature = round(kelvin - 273.15, 2) if kelvin is not None else None

        # Check if the result is Celsius and print output
        assert type(celsius) == float, "Invalid Celsius value"
        assert temperature is not None, "Temperature conversion failed"
        print(f"{kelvin} K is equal to {celsius} °C.")
    elif unit == "F":
        # Convert Kelvin to Fahrenheit
        fahrenheit = round((kelvin - 273.15) * 9 / 5 + 32, 2) if kelvin is not None else None

        # Check if the result is Fahrenheit and print output
        assert type(fahrenheit) == float, "Invalid Fahrenheit value"
        assert temperature is not None, "Temperature conversion failed"
        print(f"{kelvin} K is equal to {fahrenheit} °F.")
    else:
        print("Invalid temperature unit.")

# Test the function with valid input
convert_temperature(300.15)

# Test the function with invalid input (unit)
convert_temperature(300.15) # Enter a invalid unit at prompt
