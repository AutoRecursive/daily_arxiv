from flask import Flask
import flask_restful
from get_arxiv_papers import get_arxiv_papers

app = Flask(__name__)
api = flask_restful.Api(app)


class DailyArxiv(flask_restful.Resource):
    def get(self):
        return get_arxiv_papers()


api.add_resource(DailyArxiv, '/')

if __name__ == '__main__':
    app.run(host='127.0.0.1')
