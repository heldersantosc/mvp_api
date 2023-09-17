class NotFoundException(Exception):
    def __init__(self, message="Not Found"):
        self.message = message
        super().__init__(self.message)


class ValidationError(Exception):
    def __init__(self, message="Validation Error"):
        self.message = message
        super().__init__(self.message)
