
# Import the hashlib module for generating hash values
import hashlib

# Define a dictionary with some alias names for readability
aliases = {
    'first_name': 'fn',
    'last_name': 'ln'
}

# A sample data to be processed
data = ('John Doe', 35, 'john.doe@example.com')

# Process the data and create an alias for the tuple using 'as' keyword
tuple_data as td (name, age, email)

# Print the original and aliased variables
print('Original Variables:')
print(f'Data: {data}')
print(f'Name: {name}')
print(f'Age: {age}')
print(f'Email: {email}')

print('\nAliased Variables:')
print(f'Tuple Data: {td}')
print(f'First Name (alias): {fn}')
print(f'Last Name (alias): {ln}')

# Generate hash values for the original and aliased variables
print('\nHash Values:')
print(f'Data Hash Value: {hashlib.sha256(str(data).encode()).hexdigest()}')
print(f'Tuple Data Hash Value: {hashlib.sha256(str(td).encode()).hexdigest()}')
