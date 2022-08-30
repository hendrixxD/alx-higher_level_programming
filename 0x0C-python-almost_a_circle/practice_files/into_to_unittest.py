#!/usr/bin/python3
import unittest

class TestStringsMethods(unittest.TestCase):
    
    def test_upper(self):
        self.assertEqual('foo'. upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()