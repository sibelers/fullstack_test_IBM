from flask import Flask, request
from flask_restful import Resource, Api
import controller
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
db = client.test
link_collection = db.linksCollection

app = Flask(__name__)
api = Api(app)


class PostLinks(Resource):
    def post(self):
        data = request.form

        # Scrapping the links in the html
        list_links_mapped = controller.link_map(data)

        # Posting the results to db
        link_collection.insertOne(list_links_mapped)

        return list_links_mapped


class GetResults(Resource):
    def get(self):
        response = link_collection.find()

        return response['links']


api.add_resource(GetResults, '/getfoundlinks')
api.add_resource(PostLinks, '/links')

if __name__ == '__main__':
    app.run()
