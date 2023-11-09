class CustomException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        with open('logs.txt', 'a') as file:
            file.write(msg + '\n')

