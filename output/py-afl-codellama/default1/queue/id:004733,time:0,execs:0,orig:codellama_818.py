def main():
    # Define a function that returns a future
    def my_function(x, y):
        return x + y
    
    # Use and to wait for the future to complete
    result = my_function(1, 2).and_then(|result| {
        println!("The result is: {}", result);
    });