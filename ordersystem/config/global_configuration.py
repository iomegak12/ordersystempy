import os

from ordersystem.models import CRMSystemError
from ordersystem.utilities import ErrorProvider
from ordersystem.constants import GlobalConstants

ERRORS = [
    {"errorKey": 2, "errorId": "GLOCONF002",
        "errorMessage": "Invalid Mongo Service URI Specified!"},
    {"errorKey": 3, "errorId": "GLOCONF003",
        "errorMessage": "Invalid Mongo Service Port Specified!"},
    {"errorKey": 4, "errorId": "GLOCONF004",
        "errorMessage": "Invalid Mongo Database Information Specified!"},
]


class GlobalConfiguration:
    configuration = {}

    @staticmethod
    def get_configuration():
        isConfigurationNotNull = GlobalConfiguration.configuration is not None
        configurationLength = GlobalConfiguration.configuration.__len__()

        if isConfigurationNotNull and configurationLength > 0:
            return GlobalConfiguration.configuration

        mongoServer = os.environ.get(GlobalConstants.MONGO_SERVER, None)

        if mongoServer is None:
            raise ErrorProvider.get_error(ERRORS, 2)

        mongoPort = os.environ.get(GlobalConstants.MONGO_PORT, None)

        if mongoPort is None:
            raise ErrorProvider.get_error(ERRORS, 3)

        mongoDB = os.environ.get(GlobalConstants.MONGO_DB, None)

        if mongoDB is None:
            raise ErrorProvider.get_error(ERRORS, 4)

        GlobalConfiguration.configuration[GlobalConstants.MONGO_SERVER] = mongoServer
        GlobalConfiguration.configuration[GlobalConstants.MONGO_PORT] = mongoPort
        GlobalConfiguration.configuration[GlobalConstants.MONGO_DB] = mongoDB

        flaskDebug = os.environ.get(GlobalConstants.FLASK_DEBUG, "0")
        GlobalConfiguration.configuration[GlobalConstants.FLASK_DEBUG] = flaskDebug

        return GlobalConfiguration.configuration
