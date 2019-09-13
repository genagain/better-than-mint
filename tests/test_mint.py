# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

from betterthanmint import mint

def test_get_transactions():
    transactions = mint.get_transactions()
    # TODO assert no duplicates
    # TODO assert columns
    assert type(transactions).__name__ == 'DataFrame'
