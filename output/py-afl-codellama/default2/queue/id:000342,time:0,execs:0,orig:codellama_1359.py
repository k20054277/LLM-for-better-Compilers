import subprocess

def test_function():
    # Use assert to check if the command returns a specific exit code
    assert subprocess.call(["ls", "-l"]) == 0, "ls -l failed"

# Test the function by calling it and checking that it does not raise an exception
test_function()