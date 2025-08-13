from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def apps():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SECRET_KEY'] = 'final-production'

    db.init_app(app)
    migrate.init_app(app, db)

    #import blueprint
    from app.routes.register import register_bp
    from app.routes.login import login_bp
    from app.routes.dashboard import dashboard_bp

    #register blueprint
    app.register_blueprint(register_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(dashboard_bp)

    return app