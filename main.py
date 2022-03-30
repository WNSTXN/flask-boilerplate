from app import App
from app.routes import initialise_routes


def main():

    initialise_routes()
    App.run(debug=True)


if __name__ == '__main__':
    main()