
import math

def double(num):
    return num * 2

@pytest.fixture
def square_root(request):
    number = request.param
    yield math.sqrt(number)

@pytest.fixture
def double_numbers(request, tmp_path):
    numbers = request.param
    yield [double(num) for num in numbers]
