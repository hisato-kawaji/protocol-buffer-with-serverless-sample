import json
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
