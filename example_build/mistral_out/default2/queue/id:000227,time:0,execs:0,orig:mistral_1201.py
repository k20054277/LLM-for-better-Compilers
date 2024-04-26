
# Original data
data = {'key1': 'value1', 'key2': 'value2'}

# Using as keyword to assign aliases
alias_data = {item as key: item for item in data}
print(alias_data)  # {'key1': 'value1', 'key2': 'value2'}
