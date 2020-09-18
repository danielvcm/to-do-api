class ToDoException(Exception):
    def __init__(self, message, status_code=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        else:
            self.status_code = 400

    def to_dict(self):
        response = {
            'message': self.message
        }
        return response