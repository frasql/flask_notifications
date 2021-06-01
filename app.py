from flask import Flask
from config import BaseConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    
    from views.alerts import alert_blueprint
    from views.users import user_blueprint
    from views.main_root import main_root_blueprint

    app.register_blueprint(alert_blueprint, url_prefix="/alerts")
    app.register_blueprint(user_blueprint, url_prefix="/users")    
    app.register_blueprint(main_root_blueprint, url_prefix="/")
    
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=5000, debug=True)