
class MyClass:
    def __init__(self, name):
        self.is_enabled = True
        self.name = name

def toggle_enable(obj):
    obj.is_enabled = not obj.is_enabled

if __name__ == "__main__":
    my_instance = MyClass("Example")
    print(f"Name: {my_instance.name}")
    print(f"Is enabled: {my_instance.is_enabled}")

    toggle_enable(my_instance)
    print(f"Is enabled after toggle: {my_instance.is_enabled}")

    # Demonstrating setattr usage
    other_instance = MyClass("Another example")
    attribute_name = "new_attribute"

    setattr(other_instance, attribute_name, False)
    print(f"{other_instance.name} has {attribute_name}: {getattr(other_instance, attribute_name)}")
