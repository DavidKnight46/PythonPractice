def fun():
    print("hello")


# Tuple - ordered and unchangeable, duplicates allowed
def mytuple():
    return (1, 2, 3)


# Set - unordered and unchangeable, duplicates allowed
def myset():
    return {"", "", ""}


# Dictionary - ordered(post 3.7) and unchangeable, duplicates not allowed
def mydictonary(name, age):
    return {
        "name": name,
        "age": age
    }


# if statement
def ifstatement(x):
    # x = 4
    if x == 1:
        return "is 1"
    elif x == 3:
        return "is 3"
    else:
        return "is other"


# while loop
def loopfun():
    y = 1;

    while y <= 5:
        print(f'{ifstatement(y)} loop')
        y += 1;


