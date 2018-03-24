import sys
import os
from flask import Flask, Response, request
from analysis import get_article_info
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def api_get():

    if 'text' in request.args:
        try:
            resp = get_article_info(request.args['text'])
            return Response(resp, status=200, mimetype='application/json')
        except:
            return Response(sys.exc_info()[0], status=200, mimetype='text/html')

    else:
        return Response('Please provide non-null "text" parameter', status=412)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('GENDERMEME_PORT'))
