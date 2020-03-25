import json
import datetime

def check_code(code):
    return 200 <= code <= 209

class JsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

def get_response_body(resp):
    if resp.status_code == 204:
        return None
    body = resp.content
    if body and 'application/json' in resp.headers.get('content-type', ''):
        try:
            body = resp.json()
        except:
            pass
    return body