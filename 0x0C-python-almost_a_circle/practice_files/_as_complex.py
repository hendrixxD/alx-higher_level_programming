#!/usr/bin/python3
import json
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['img'])

print(json.loads('{"__complex__": true, "real": 1, "img": 8}', object_hook=as_complex))

import decimal
print(json.loads('1.1', parse_float=decimal.Decimal))
