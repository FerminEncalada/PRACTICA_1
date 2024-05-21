from flask import Flask
from flask_cors import CORS
from routes.api import api
from routes.router import router

app = Flask(__name__)
CORS(app)

app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(router)

if __name__ == '__main__':
    app.run(debug=True)
