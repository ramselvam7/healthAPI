from flask import Flask, Request, jsonify
import json
from flask_restful import Resource, Api
import pickle
import json
from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from uber_rides.auth import AuthorizationCodeGrant
from pymongo import MongoClient


app = Flask(__name__)
api = Api(app)
db_demo = 'Sample'
session = Session(server_token="mw5HF4ytE56WjHeBJgcjWWFr7o_BIpZHaq89xVzL")
client = UberRidesClient(session)

class getRideEstimate(Resource):
    def get(self):
        response = client.get_products(37.77, -122.41)
        products = response.json.get('products')
        print(products)
        response = client.get_price_estimates(
        start_latitude=12.955285,
        start_longitude=80.145743,
        end_latitude=12.923790,
        end_longitude=80.114396,
        seat_count=2)
        estimate = response.json.get('prices')
        print(estimate) 

class getDoctorName(Resource):
    def get(self):
        client = MongoClient('localhost',27017)
        db = client.MembersDB
        collection = db.member
        member = collection.find_one()
        print(member)
        doctor_name = member["Has_Primary_Care_Phy"]
        return doctor_name

api.add_resource(getDoctorName, '/getDoctorName')


if __name__ =='__main__':

     app.run(port='5000')

