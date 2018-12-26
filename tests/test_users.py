from base import TestRequest
import account_pb2
import sys
import os

n = TestRequest()

if __name__ == '__main__':
    body = account_pb2.RegisterAccountRequest()
    body.user_name = 'test'
    body.password = 'Hoge1234'
    body.email_address = 'hisato.kawaji@gmail.com'
    body.phone_number = '08055190952'

    print(n.post("/users/create", body))
    ##sys.stdout.write(test.SerializeToString())
    ##print(test.SerializeToString())
    ##print(MessageToJson(test))
