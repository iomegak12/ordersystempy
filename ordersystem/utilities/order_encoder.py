import json
from ordersystem.utilities import ErrorProvider
from ordersystem.models import Order

ERRORS = [
    {"errorKey": 1, "errorId": "ORDTRANS001",
        "errorMessage": "Invalid Order Dictionary Specified!"},
]


class OrderEncoder(json.JSONEncoder):
    @staticmethod
    def transform(dictionary):
        if dictionary is None:
            raise ErrorProvider.get_error(ERRORS, 1)

        order = Order(dictionary["orderId"], dictionary["orderDate"],
                      dictionary["customer"], dictionary["billingAddress"], dictionary["amount"])

        return order

    def default(self, o):
        return o.__dict__
