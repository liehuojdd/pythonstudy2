'''
Unit test file name should start with testXXXXX.py
'''
import unittest
import os
import sys

def testAllinCurrent():
    path=os.path.abspath(os.path.dirname(sys.arv[0]))
    print(path)
    pass

if __name__=="__main__":
    unittest.main()