from flask import Flask
from flask_restful import Resource, Api, abort, reqparse
from flask_cors import CORS
from snownlp import SnowNLP

app = Flask(__name__)
cors = CORS(app, resources={r"/predict": {"origins": "*"}})
api = Api(app)

# 参数解析
parser = reqparse.RequestParser()
parser.add_argument('sentence', type=str)

class Prediction(Resource):
    def post(self):
        args = parser.parse_args()
        s = SnowNLP(args['sentence'])
        return s.sentiments*5, 200

api.add_resource(Prediction, '/predict')

if __name__ == '__main__':
    app.run(debug=True)
