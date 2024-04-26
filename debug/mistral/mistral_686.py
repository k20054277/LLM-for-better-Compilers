
# This is a simple Python script that checks if a user is old enough to install packages using pip

age = int(input("Enter your age: "))
is_old_enough = age >= 18

if is_old_enough:
    print("You're old enough to install packages using pip!")
    # Install Flask package as an example
    import subprocess
    try:
        subprocess.check_call(["pip", "install", "-u", "Flask"])
        print("Flask has been installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install Flask, error message: {e}")
else:
    print("You're not old enough to install packages using pip.")
