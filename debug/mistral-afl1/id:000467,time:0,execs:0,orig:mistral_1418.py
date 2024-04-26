
def process_purchase(store_inventory, item, quantity):
    """
    This function simulates purchasing an item from the given store inventory.
    :param store_inventory: A dictionary representing a store's inventory
    :param item: The name of the desired item
    :param quantity: The amount of the item to be purchased
    :return: The total cost of the purchase
    """
    # Assert checks for valid input
    assert isinstance(store_inventory, dict), "Invalid inventory data"
    assert isinstance(item, str) and item in store_inventory, f"Item '{item}' not found in the store"
    assert isinstance(quantity, int) > 0, "Invalid quantity"

    # Process purchase based on the validated input
    price = store_inventory[item]
    total_cost = price * quantity

    print(f"\nProcessing purchase for {quantity} items of '{item}'...")
    print(f"Total cost: ${total_cost}")

# Sample store inventory
store_inventory = {
    "Apple": 0.5,
    "Banana": 0.3,
    "Orange": 0.6
}

# Processing a valid purchase (purchasing 2 bananas)
process_purchase(store_inventory, "Banana", 2)

# Processing an invalid purchase (purchasing a non-existent item)
try:
    process_purchase(store_inventory, "Cherry", 5)
except AssertionError as e:
    print(e)
