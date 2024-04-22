
import cron

def test_assert_cron():
    # Define a cron expression
    cron_expression = "0 0 * * *"

    # Create a cron object
    cron_object = cron.Cron(cron_expression)

    # Assert that the cron object is valid
    assert cron_object.validate() is True

    # Assert that the cron object's schedule is correct
    assert cron_object.schedule == cron_expression

    # Assert that the cron object's next scheduled time is correct
    assert cron_object.next(datetime.datetime.now()) is not None

if __name__ == "__main__":
    test_assert_cron()
