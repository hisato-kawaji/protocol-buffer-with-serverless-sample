import google.protobuf
import item_pb2
import sys
import json
from google.protobuf.json_format import MessageToJson


def hoge(event, context):
    print("event")
    print(event)
    print("context")
    print(context)
    test = item_pb2.GetItemDetailResponse().Item()
    test.item_id = '1'
    test.model = 'hoge'
    test.color = 'red'
    test.display_name = 'test'
    sys.stdout.write(test.SerializeToString())
    print(test.SerializeToString())
    print(MessageToJson(test))
    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            'Content-Type': 'application/x-protobuf',
        },
        "body": test.SerializeToString().decode('utf-8'),
        "isBase64Encoded": True
    }
