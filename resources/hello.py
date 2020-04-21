from flask_restful import Resource, reqparse

# Create a new resource that will handle petitions (on /hello/ endpoint)
class Hello(Resource):

    # Checking data sent on body
    ## Must receive and required argument called name type string (default)
    ## If no value will response with help
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        required=True,
        help='This field cannot be blank.')

    # Methog that will handle petition over POST 
    @classmethod
    def post(cls):

        # Reading data from petition body
        data = cls.parser.parse_args()

        # Returning a message: Hello {name}!
        return {'message': 'Hello {}!'.format(data['name'])}