from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.user.views import get_user_name

article = Blueprint("article", __name__, url_prefix="/article", static_folder="../static")

ARTICLES = {
    1: {
        "title": "Wonderful Kindom",
        "text": "Once upon a time",
        "author": 2
    },
    2: {
        "title": "Time for dream",
        "text": "In fantastic world",
        "author": 3
    },
    3: {
        "title": "Sun in garden",
        "text": "More times ago",
        "author": 1
    },

}


@article.route("/")
def article_list():
    return render_template(
        "articles/list.html",
        articles=ARTICLES
    )


@article.route("/<int:pk>")
def get_article(pk: int):
    if pk in ARTICLES:
        article_raw = ARTICLES[pk]
    else:
        raise NotFound("Article id:{}, not found".format(pk))
    title = article_raw["title"]
    text = article_raw["text"]
    author = get_user_name(article_raw["author"])
    return render_template(
        "articles/details.html",
        title=title,
        text=text,
        author=author
    )















# from flask import Blueprint, render_template
# from werkzeug.exceptions import NotFound
#
#
# from blog.user.views import get_user_name
#
# article = Blueprint('article', __name__, url_prefix='/article', static_folder='../static')
#
# ARTICLES = {
#     1: {'name': 'Age of Empires',
#         'text': 'text_text',
#         'author': 2
#         },
#
#
#     2: {'name': 'Myst',
#         'text': 'text_text_text ',
#         'author': 3
#     },
#
#     3:{
#         'name': 'Dayz world',
#         'text': 'textZ',
#         'author': 1
#     }
#
# }
# @article.route('/')
# def article_list():
#     return render_template(
#         'articles/list.html',
#         articles = ARTICLES
#     )
#
#
# @article.route('/<int:pk>')
# def get_article(pk: int):
#     if pk in ARTICLES:
#         article_raw = ARTICLES[pk]
#     else:
#         raise NotFound(f'Article id {pk}, not found')
#     name = article_raw['name']
#     text = article_raw['text']
#     author = get_user_name(article_raw['author'])
#     return render_template(
#         'articles/details.html',
#         name=name,
#         author=author
#     )