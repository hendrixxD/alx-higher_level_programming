#!/usr/bin/python3
def hash_print(x, y):
    if x > y:
        raise ValueError("x must be less than y")
    else:
        for i in range(y):
            print('#'*x)

def main():
    hash_print(6, 10)
main()
