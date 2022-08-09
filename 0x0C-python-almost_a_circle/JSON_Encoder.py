#!/usr/bin/python3
import json
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        #let the base clas default method raise the exception
        return json.JSONEncoder.default(self, obj)

print(json.dumps(2+1j, cls=ComplexEncoder))
print(ComplexEncoder().encode(2 + 1j))
print(list(ComplexEncoder().iterencode(2 + 1j)))
