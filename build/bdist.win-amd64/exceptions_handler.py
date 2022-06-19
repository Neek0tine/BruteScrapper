class BrutescrapException(RuntimeError):
    pass


class BrutescrapWindowException(BrutescrapException):
    def __init__(self, message):
        message += " (%s)" % WinError()
        super(BrutescrapWindowException, self).__init__(message)


class BrutescrapTimeoutException(BrutescrapException):
    pass
