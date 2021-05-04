def decorator_function(parameter_function):
    def inner_function(*args, **kwargs):
        # action
        print("let's calculate...")
        parameter_function(*args, **kwargs )
        # more actions
        print("We've finished")
    return inner_function

@decorator_function
def addition(num1, num2):
    print(num1 + num2)

@decorator_function
def subtraction(num1, num2):
    print(num1 + num2)

@decorator_function
def powwer(base, exp):
    print(pow(base, exp))

addition(8, 20)
subtraction(30,8)
powwer(exp=2, base=5)