class CustomException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        msg = args[0] if args else kwargs.get('msg', '')
        with open('logs.txt', 'a') as file:
            file.write(msg + '\n')

try:

    raise CustomException("Це повідомлення буде додано до logs.txt")

except CustomException as e:
    print(f"Помилка: {e}")
   

