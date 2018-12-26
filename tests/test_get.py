from base import TestRequest
import sys
import os
import sample_pb2

n = TestRequest()

if __name__ == '__main__':
    test = sample_pb2.Test()
    test.test_id = 'aaa'
    test.hoge = 'yyy'
    print(test.SerializeToString())
    print(n.post("/get", test.SerializeToString()).text)
