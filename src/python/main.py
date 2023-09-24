# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from clash_api import *
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

class ClanMembers(Resource):
    def get(self):
        result=get_members('')
        return jsonify({'message': result})
class ClanInfo(Resource):
    def get(self):
        clan_details=get_clan('')
        return jsonify({'message': clan_details})
class WarHistory(Resource):
    def get(self):
        return jsonify({'message': get_war_history()})
class MemberInfo(Resource):
    def get(self, tag):
        print(tag)
        result=get_member(tag)
        print(result)
        return jsonify({'message': result})

# adding the defined resources along with their corresponding urls
api.add_resource(ClanMembers, '/clan-members')
api.add_resource(ClanInfo, '/clan-info')
api.add_resource(WarHistory, '/war-history')
api.add_resource(MemberInfo, '/member-info/<string:tag>')


# driver function
if __name__ == '__main__':
    app.run(debug = True)

