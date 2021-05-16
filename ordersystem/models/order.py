import json


class Order:
    def __init__(self, orderId, orderDate, customer, billingAddress, amount):
        self.orderId = orderId
        self.orderDate = orderDate
        self.customer = customer
        self.billingAddress = billingAddress
        self.amount = amount

    def __str__(self):
        message = "{}, {}, {}, {}, {}".format(
            self.orderId, self.orderDate, self.customer,
            self.billingAddress, self.amount)

        return message

    def toJson(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.toJson()
