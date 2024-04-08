def check_uppercase_printable(c):
    return c.isupper() and c.isprintable()

for c in range(ord('A'), ord('Z') + 1):
    if check_uppercase_printable(chr(c)):
        print(f"Character '{chr(c)}' is uppercase and printable.")