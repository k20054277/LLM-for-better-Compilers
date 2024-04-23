
# Function definition with multiple arguments
def process_data(input1, input2, keyword1, keyword2):
    print("Input 1:", input1)
    print("Input 2:", input2)
    print("Keyword 1:", keyword1)
    print("Keyword 2:", keyword2)

# List and dictionary to be unpacked and assigned
data = [1, "one", 3.14], ["two", 2, "two text"], {"key1": "value1", "key2": "value2"}]

# Function call with list and dictionary unpacking
 inputs, keyword_list, input_dict = data
 process_data(*inputs, **keyword_list)
