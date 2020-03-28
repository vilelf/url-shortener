import json


def make_response(body, status_code, headers={}):
    return {
        'body': json.dumps(body),
        'statusCode': status_code,
        'headers': headers
    }