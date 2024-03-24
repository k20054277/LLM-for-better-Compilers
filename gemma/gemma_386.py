
import pickle

# Create a boolean variable
is_active = False

# Pickle the boolean variable
pickle.dump(is_active, 'active.pkl')

# Unpickle the boolean variable
is_active_unpickled = pickle.load('active.pkl')

# Print the value of the boolean variable
print(is_active_unpickled)
