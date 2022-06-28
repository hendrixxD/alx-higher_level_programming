#!/usr/bin/python3
def fizzbuzz():
    var = []
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            var.append("FizzBuzz ")
        elif n % 3 == 0:
            var.append("Fizz ")
        elif n % 5 == 0:
            var.append("Buzz ")
        else:
            var.append("{:d} ".format(n))
    print("".join(var), end="")
