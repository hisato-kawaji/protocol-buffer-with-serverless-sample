import json
import sample_pb2
import base64
import sample_pb2

def sample(event, context):
    body = sample_pb2.Test()
    body.test_id = 'test'
    body.hoge = 'hogehoge'
    response = {
        'statusCode': 200,
        'headers': { 
            "Access-Control-Allow-Origin": "*",
            'Content-Type': 'application/x-protobuf' 
        },
        'body': body.SerializeToString().decode('utf-8'),
        'isBase64Encoded': True
    }

    return response

def get(event, context):
    obj = sample_pb2.Test()
    obj.ParseFromString(base64.b64decode(event['body']))
    obj.test_id = 'bbb'
    response = {
        'statusCode': 200,
        'headers': { 
            "Access-Control-Allow-Origin": "*",
            'Content-Type': 'application/x-protobuf' 
        },
        'body': obj.SerializeToString().decode('utf-8'),
        'isBase64Encoded': True
    }

    return response

def multi(event, context):
    response = {
        'statusCode': 200,
        'headers': { 
            "Access-Control-Allow-Origin": "*",
            'Content-Type': 'application/x-protobuf' 
        },
        'body': "",
        'isBase64Encoded': True
    }

    return response
