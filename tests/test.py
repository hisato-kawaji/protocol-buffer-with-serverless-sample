from base import TestRequest
import sys
import os

n = TestRequest()

if __name__ == '__main__':
    print(n.get("/sample").text)
