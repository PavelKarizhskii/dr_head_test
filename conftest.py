import pytest
from termcolor import colored


@pytest.fixture
def set_up():
    print(colored("\nStart test", 'yellow'))
    yield
    print(colored("\nFinish tests", 'yellow'))
