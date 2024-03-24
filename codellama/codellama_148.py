import subprocess

def main():
    # Use and to run multiple commands in a single line
    output = subprocess.run(["echo", "Hello"], stdout=subprocess.PIPE)
    print(output.stdout.decode("utf-8"))

if __name__ == "__main__":
    main()