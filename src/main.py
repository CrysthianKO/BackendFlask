from flask import Flask
from database import engine

app = Flask(__name__)

if __name__ == "__main__":
    app.run()