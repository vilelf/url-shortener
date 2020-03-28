from processor import UrlProcessor
from utils import make_response

def hello(event, context):
    body = {
        'message': 'PONG'
    }

    return make_response(body, 200)

def url_generator(event, context):
    url_processor = UrlProcessor()
    url = url_processor.main()
    
    return make_response({'newUrl': url}, 200)