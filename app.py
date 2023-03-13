from src.routes.price import pricesRouting

from src import create_app

app = create_app()
app.register_blueprint(pricesRouting)

app.app_context().push()


if __name__ == '__main__':
    app.run(debug=True)

