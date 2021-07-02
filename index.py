import json
import datetime


def handler(event, context):
    data = {
        'output': 'Oh!Yes. Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
