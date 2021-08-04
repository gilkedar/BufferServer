
class ApplicationServerError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ErrorInvalidInput(ApplicationServerError):
    def __init__(self, message):
        ApplicationServerError.__init__(self, message)


class ErrorCallingExecutionServer(ApplicationServerError):
    def __init__(self, message):
        ErrorCallingExecutionServer.__init__(self, message)

