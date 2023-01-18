from os import environ as env


class Config:
    """
    Summary
    -------
    Static class for configuration

    Attributes
    ----------
    URI (str) : database URI
    SQLALCHEMY_DATABASE_URI (str) : database URI
    SQLALCHEMY_TRACK_MODIFICATIONS (bool) : if True, Flask-SQLAlchemy will track modifications
    SECRET_KEY (str) : secret key for session management
    PORT (int) : port to serve the application on
    HOST (str) : host to serve the application on
    """
    URI = str(env.get('DATABASE_URL', 'postgresql://localhost/'))
    SQLALCHEMY_DATABASE_URI = URI.replace('postgres://', 'postgresql://', 1) if URI.startswith('postgres://') else URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = env.get('SECRET_KEY')
    PORT = int(env.get('PORT', 5000))
    HOST = str(env.get('HOST', '0.0.0.0'))
