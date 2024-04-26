from typing import List, Tuple

def create_namespace(names: List[str], values: List[int]) -> dict:
    """Creates a dictionary with the given names and values."""
    namespace = {}
    for name, value in zip(names, values):
        namespace[name] = value
    return namespace

def use_namespace(namespace: dict) -> None:
    """Prints the values of the variables in the given dictionary."""
    for name, value in namespace.items():
        print(f"{name}: {value}")

# Example usage
names = ["x", "y", "z"]
values = [1, 2, 3]
namespace = create_namespace(names, values)
use_namespace(namespace)