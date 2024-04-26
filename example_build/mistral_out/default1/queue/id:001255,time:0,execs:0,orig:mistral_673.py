
# Inside app.py:
import config

def hello():
    if config.IS_PRODUCTION:
        return "Hello, World!"
    else:
        return "Hello and welcome to development mode!"

if __name__ == "__main__":
    print(hello())
