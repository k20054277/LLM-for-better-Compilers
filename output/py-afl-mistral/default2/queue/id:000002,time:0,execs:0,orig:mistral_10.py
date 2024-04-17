
class MyClass:
    def __init__(self, is_active=False):
        self.is_active = is_active

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

# Create an instance of MyClass and check its initial state
my_instance = MyClass()
print("Initial state:", my_instance.is_active)  # Initial state: False

# Activate the instance
my_instance.activate()
print("Activated state:", my_instance.is_active)  # Activated state: True

# Deactivate the instance
my_instance.deactivate()
print("Deactivated state:", my_instance.is_active)  # Deactivated state: False
