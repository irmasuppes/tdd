from fizzbuzz import fizz_buzz

def test_3_is_fizz():
    assert fizz_buzz(3) == "Fizz"

def test_5_is_fizz():
    assert fizz_buzz(5) == "Buzz"

def test_15_is_fizzbuzz():
    assert fizz_buzz(15) == "FizzBuzz"

def test_1_is_1():
    assert fizz_buzz(1) == 1

def test_6_is_fizz():
    assert fizz_buzz(6) == "Fizz"

def test_10_is_buzz():
    assert fizz_buzz(10) == "Buzz"

def test_45_is_fizzbuzz():
    assert fizz_buzz(45) == "FizzBuzz"