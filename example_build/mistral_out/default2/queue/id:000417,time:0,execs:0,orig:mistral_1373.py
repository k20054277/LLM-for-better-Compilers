
# Function to check if two tuples are equal with some additional conditions
def check_tuples(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        return "Number of elements in tuples must be equal"
     for i in range(len(tuple1)):
         if tuple1[i] != tuple2[i]:
             return f"Elements at index {i} are not equal: {tuple1[i]} vs {tuple2[i]}"
     return " tuples are equal"

# Define some tuples
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
tuple3 = (1, 2, 4)

# Check the tuples using the function and assert statement
assert check_tuples(tuple1, tuple2) == " tuples are equal", "Error: tuples are not equal"
assert check_tuples(tuple1, tuple3) == "Error: tuples are not equal", "Error: tuples are equal"

print("All assertions passed")
