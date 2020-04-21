import os
from flask import Flask
from flask_restful import Api

# Importing endpoint resources
from resources.hello import Hello

# Create an instance of the Flask and Flask-RESTful API
app = Flask(__name__)
api = Api(app)

# Connect Resource with Endpoint
api.add_resource(Hello, '/hello/')

# Running app only if is called from app entrypoint
## Getting port from OS or using default 5000
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1',port=int(os.environ.get('PORT', 5000)))