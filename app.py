from flask import Flask
from config import BaseConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)
    
    from views.alerts import alert_blueprint
    from views.users import user_blueprint
    from views.main_root import main_root_blueprint
    from views.projects import project_blueprint
    from views.activities import activity_blueprint

    app.register_blueprint(alert_blueprint, url_prefix="/alerts")
    app.register_blueprint(user_blueprint, url_prefix="/users")    
    app.register_blueprint(main_root_blueprint, url_prefix="/")
    app.register_blueprint(project_blueprint, url_prefix="/projects")
    app.register_blueprint(activity_blueprint, url_prefix="/activities")
    
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=5000, debug=True)