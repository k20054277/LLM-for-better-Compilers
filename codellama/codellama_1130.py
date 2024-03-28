import re

def main():
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    string = "john.doe@example.com"
    result = re.search(pattern, string)
    
    if result:
        print("Valid email address")
    else:
        print("Invalid email address")

main()