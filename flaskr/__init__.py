import os

from flask import Flask


def create_app(test_config=None):
    """
    Create and configure the app.
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "flaskr.sqlite"),
    )

    if not test_config:
        # Load the instance configuration, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # Load the test configuration if passed in
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Simple page thet says hello
    @app.route("/hello")
    def hello():
        return "Hello, World!"

    return app
