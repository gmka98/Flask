from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from routes import post_routes
from models.post import Post


db = SQLAlchemy()


def create_app(db, Post):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(post_routes)
    return app


app = create_app(db, Post)

if __name__ == '__main__':
    app.run()