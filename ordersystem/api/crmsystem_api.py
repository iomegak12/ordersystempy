import json
from flask import Flask
from flask_cors import CORS

from ordersystem.config import GlobalConfiguration
from ordersystem.constants import GlobalConstants
from ordersystem.services import OrderService
from ordersystem.utilities import OrderEncoder

configuration = GlobalConfiguration.get_configuration()
flaskApp = Flask(__name__)

CORS(flaskApp)

flaskApp.config["DEBUG"] = int(configuration[GlobalConstants.FLASK_DEBUG])


class OrderSystemApi:
    @staticmethod
    @flaskApp.route("/", methods=["GET"])
    def home():
        return "<h1> Order System Home </h1>"

    @ staticmethod
    @ flaskApp.route("/api/v1/orders/", methods=["GET"])
    def get_orders():
        service = OrderService()
        orders = service.get_orders()

        return json.dumps(orders, cls=OrderEncoder)

    @ staticmethod
    @ flaskApp.route("/api/v1/orders/<customerid>", methods=["GET"])
    def get_orders_by_customer(customerid: int):
        service = OrderService()
        orders = service.get_orders(customerid)

        return json.dumps(orders, cls=OrderEncoder)
