#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_result_list = []
    for x in range(list_length):
        try:
            new_result_list.append(my_list_1[x] / my_list_2[x])
        except ZeroDivisionError:
            print("division error")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            pass
        return new_resul_list
