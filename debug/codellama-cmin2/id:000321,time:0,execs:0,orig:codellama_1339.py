def demo_assert_sorted(mylist):
    assert sorted(mylist) == mylist, "List is not sorted"

demo_assert_sorted([3, 2, 1])  # Should pass
demo_assert_sorted([3, 2, 4])  # Should fail with AssertionError