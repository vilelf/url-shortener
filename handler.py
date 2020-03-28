from processor import UrlProcessor
from utils import make_response


def url_generator(event, context):
    url_processor = UrlProcessor()
    url = url_processor.generate()
    
    return make_response({'newUrl': url}, 200)