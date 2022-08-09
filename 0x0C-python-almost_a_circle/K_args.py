def greet_me(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print(f"{key} == {value}")

greet_me(name="yasoob")
