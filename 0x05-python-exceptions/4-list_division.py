#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_result_list = []
    new_list = 0
    for x in range(list_length):
        try:
            new_list = my_list_1[x] / my_list_2[x]
        except (ZeroDivisionError, IndexError, TypeError) as err:
            if isinstance(err, ZeroDivisionError):
                print("division error")
            elif isinstance(err, IndexError):
                print("out of range")
            elif isinstance(err, TypeError):
                print("wrong type")
            #new_result_list.append(0)
        finally:
            pass
    return new_result_list.append(new_list)

