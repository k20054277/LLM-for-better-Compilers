import pickle

# And operator
x = 5
y = 10
print(x > y) # False
print(x < y) # True

# Pickle
person = {'name': 'John', 'age': 30}
f = open('person.pickle', 'wb')
pickle.dump(person, f)
f.close()

# Load the pickled data
f = open('person.pickle', 'rb')
person2 = pickle.load(f)
print(person == person2) # True