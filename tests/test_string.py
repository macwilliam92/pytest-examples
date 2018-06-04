from utils.string import capital_case, reverse_string


def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'


def test_reverse_string():
    assert reverse_string('hello') == 'olleh'
