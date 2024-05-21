from flask import Flask
from routes.api import api
from routes.router import router

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(router)

if __name__ == "__main__":
    app.run(debug=True)
