
import logging

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a test case
def test_assert():
    # Assert an expected result
    assert 5 == 5

    # Log a message
    logger.info("Test case passed")

# Run the test case
test_assert()

# Print the logs
for handler in logger.handlers:
    print(handler)
