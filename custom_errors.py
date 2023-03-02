class MyCustomError(TypeError):
    """
    A custom error that has not yet been defined.
    """
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code
  
raise MyCustomError('An error occured.', 500)

# to print out the doc string of an error:
# error = MyCustomError('An error occured.', 500)
# print(error.__doc__)


# creating a new custom error for count_from_zero_to_n(n)
class UncountableError(ValueError):
    """
    A custom error for a wrong_value if argument is not greater than 0.
    """
    def __init__(self, wrong_value):
        super().__init__(f'Invalid value for n, {wrong_value}. n must be greater than 0.')
        self.wrong_value = wrong_value

def count_from_zero_to_n(n):
    if n < 1:
        raise UncountableError(n)
    for x in range(0, n + 1):
        print(x)