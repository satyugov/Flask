from flask import Flask

from blog.article.views import article
from blog.user.views import user
from blog.index.views import index
from blog.report.views import report

VIEWS = [
    index,
    user,
    article,
    report
]


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)





# from flask import Flask, Response, session
#
#
# # app = Flask(__name__)
# # app.secret_key = "secret key"
# #
# # @app.route("/")
# # def index():
# #     if 'visits' in session:
# #         session['visits'] = session.get('visits') + 1
# #     else:
# #         session['visits'] = 1
# #     return f"Количество посещений на сайте {session.get('visits')}"
# #
# #
# #
# # @app.route("/del_visit")
# # def del_visit():
# #     session.pop('visits', None)
# #     return 'Данные о посещениях очищены'
# from blog.report.views import report
# from blog.user.views import user
# from blog.article.views import article
#
#
# def create_app() -> Flask:
#     app = Flask(__name__)
#     register_blueprints(app)
#     return app
#
# def register_blueprints(app: Flask):
#     app.register_blueprint(user)
#     app.register_blueprint(report)
#     app.register_blueprint(article)
