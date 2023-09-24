# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from clash_api import *
import urllib.parse
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

class MemberInfo(Resource):
    def get(self, tag):
        return jsonify({'message': get_member(urllib.parse.quote(tag, safe=''))})
class ClanMembers(Resource):
    def get(self):
        return jsonify({'message': get_members()})
class ClanInfo(Resource):
    def get(self):
        return jsonify({'message': get_clan()})
class WarHistory(Resource):
    def get(self):
        return jsonify({'message': get_war_history()})

# adding the defined resources along with their corresponding urls
api.add_resource(ClanMembers, '/clan-members')
api.add_resource(ClanInfo, '/clan-info')
api.add_resource(WarHistory, '/war-history')
api.add_resource(MemberInfo, '/member-info/<string:tag>')


# driver function
if __name__ == '__main__':
    app.run(debug = True)

