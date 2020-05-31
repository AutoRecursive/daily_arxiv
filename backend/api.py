from flask import Flask
import flask_restful
from get_arxiv_papers import get_arxiv_papers

app = Flask(__name__)
api = flask_restful.Api(app)


class DailyArxiv(flask_restful.Resource):
    def __init__(self):
        super(DailyArxiv, self).__init__()
        self.key_words = ['optimal control', 'non-linear control', 'nonlinear control', 'robotics', 'Systems and Control', 'Optimization and Control']
        self.Key_words = ['Koopman', 'Systems and Control']

    def get(self):
        self.papers = get_arxiv_papers(self.key_words, self.Key_words)
        return self.papers['meta']


api.add_resource(DailyArxiv, '/papers')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
