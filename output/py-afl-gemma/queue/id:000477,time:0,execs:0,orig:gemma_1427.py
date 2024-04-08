
import subprocess
import assert

# Define a function to test a command
def test_command(command):
    # Assert that the command is successful
    assert.assertTrue(subprocess.call(command) == 0)

    # Assert that the output of the command is equal to the expected output
    assert.assertEqual(subprocess.check_output(command).decode("utf-8"), "Expected output")

# Test a command
test_command(["ls", "-l"])

# Test a command that is not successful
test_command(["invalid_command", "does_not_exist"])
