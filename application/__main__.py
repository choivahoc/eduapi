from application import create_app

if __name__ == '__main__':
    #abc
    app = create_app()
    app.run(host=app.config['HOST'],
            port=app.config['PORT'])
