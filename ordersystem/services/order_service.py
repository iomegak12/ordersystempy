from pymongo import MongoClient

from ordersystem.utilities import ErrorProvider, OrderEncoder
from ordersystem.models import Order
from ordersystem.config import GlobalConfiguration
from ordersystem.constants import GlobalConstants

ERRORS = [
    {"errorKey": 1, "errorId": "ORDSVC001",
        "errorMessage": "Invalid Order Service Callback Specifid!"},
    {"errorKey": 2, "errorId": "ORDSVC002",
        "errorMessage": "Invalid Mongo Datails (Server/Port/DB) Specifid!"},
]

ORDERS_COLLECTION = "orders"


class OrderService():
    def __init__(self):
        configuration = GlobalConfiguration.get_configuration()
        mongoServer = configuration[GlobalConstants.MONGO_SERVER]
        mongoPort = configuration[GlobalConstants.MONGO_PORT]
        mongoDB = configuration[GlobalConstants.MONGO_DB]

        isMongoConfigurationValid = mongoServer is not None and \
            mongoPort is not None and mongoDB is not None

        if not(isMongoConfigurationValid):
            raise ErrorProvider.get_error(ERRORS, 2)

        self.mongoServer = mongoServer
        self.mongoPort = int(mongoPort)
        self.mongoDB = mongoDB

    def get_orders(self, customer=None):
        client = MongoClient(host=self.mongoServer,
                             port=self.mongoPort)
        database = client[self.mongoDB]
        collection = database[ORDERS_COLLECTION]

        if customer is None:
            orders = collection.find({})
        else:
            orders = collection.find({"customer": int(customer)})

        internetOrders = []

        for order in orders:
            internetOrders.append(
                OrderEncoder.transform(order))

        return internetOrders
