#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_result_list = []
    for x in range(list_length):
        try:
            new_result_list.append(my_list_1[x] / my_list_2[x])
        except (ZeroDivisionError, IndexError, TypeError) as err:
            if isinstance(err, ZeroDivisionError):
                print("division error")
            elif isinstance(err, IndexError):
                print("out of range")
            elif isinstance(err, TypeError):
                print("wrong type")
        finally:
            pass
        return new_resul_list
