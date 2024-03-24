
import logging

def my_function(num1, num2):
    # Log a message when the function is called
    logging.info(f"Called my_function with arguments: num1={num1}, num2={num2}")
    
    # This line is supposed to return the larger number between num1 and num2, but contains an error
    if num1 > num2:
        return num1
    else:
        return False

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # Configure logging settings
    
    # Call my_function with different arguments
    print("Largest number between 5 and 10 is:", my_function(5, 10))
    print("Largest number between -3 and 7 is:", my_function(-3, 7))
