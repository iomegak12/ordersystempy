import json
from datetime import datetime


class CRMSystemError(Exception):
    def __init__(self, errorId, errorMessage, *args, **kwargs):
        super().__init__(errorMessage, *args, **kwargs)

        self.errorId = errorId
        self.errorMessage = errorMessage

    def __str__(self):
        message = "{} - {} - {}".format(datetime.now(),
                                        self.errorId, self.errorMessage)

        return message

    def toJson(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return self.toJson()
