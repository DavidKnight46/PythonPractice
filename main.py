# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# My first Python comment for first function
import davidpractice


def myarray(name):
    ar = [1, 2, 3]
    result = []

    for i in ar:
        result.append(i+1)
        print(i)

    for y in result:
        print(y)

    print(f'{name[0]} is {ar[2]}')


#
def add(n1, n2):
    n = n1 + n2
    print(f'{n} from {n1} add {n2}')


#
def myfunction(str):
    return str


#
def print_hi(name):
    add(5,7)
    i = myfunction('Hello')

    # Use a breakpoint in the code line below to debug your script.
    print(f'{i}, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    myarray(['David','Knight'])
    family = (davidpractice.mydictonary("David Knight", 35),
              davidpractice.mydictonary("Yang Zhou", 30),
              davidpractice.mydictonary("Dylan Knight", 2))

    for p in family:
        print(f'{p.get("name")}; age: {p.get("age")}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/