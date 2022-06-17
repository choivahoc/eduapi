from application import create_app
from flask_cors import CORS

if __name__ == '__main__':
    app = create_app()
    CORS(app, supports_credentials=True)
    app.run(host=app.config['HOST'],
            port=app.config['PORT'])
