from ordersystem.models import CRMSystemError


class ErrorProvider:
    def get_error(errors, errorId):
        errorInfo = None

        for error in errors:
            if error["errorKey"] == errorId:
                errorInfo = error
                break

        return CRMSystemError(errorInfo["errorId"], errorInfo["errorMessage"])
