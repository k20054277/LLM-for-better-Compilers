
# False and while demonstration

# Define a boolean variable
is_active = False

# While the variable is False, the loop will continue
while not is_active:
    # Print "Waiting..."
    print("Waiting...")

    # Simulate some time passing
    time.sleep(2)

# Once the variable becomes True, the loop will break
is_active = True

# Print "Done!"
print("Done!")
