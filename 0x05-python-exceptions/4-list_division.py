#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for idx in range(list_length):
        try:
            result_list.append(my_list_1[idx] / my_list_2[idx])
        except (ZeroDivisionError, IndexError, TypeError) as err:
            if isinstance(err, ZeroDivisionError):
                print("division error")
            elif isinstance(err, IndexError):
                print("out of range")
            elif isinstance(err, TypeError):
                print("wrong type")
        finally:
            pass
