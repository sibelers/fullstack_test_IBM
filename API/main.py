from flask import Flask
from flask_restful import Resource, Api
import controller
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dev_test_database
link_collection = db.links_collection

app = Flask(__name__)
api = Api(app)


class PostLinks(Resource):
    def post(self, url):
        # Scrapping the links in the html
        list_links_mapped = controller.link_map(url)

        # Posting the results to db
        link_collection.insert_many(list_links_mapped)

        return 'true'


class GetResults(Resource):
    def get(self):
        print("entrei/sai no get")
        return link_collection.find_one()


api.add_resource(GetResults, '/link')
api.add_resource(PostLinks, '/link/<url>')

if __name__ == '__main__':
    app.run()

