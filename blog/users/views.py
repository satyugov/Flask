from flask import Blueprint, render_template, redirect
from werkzeug.exceptions import NotFound

user = Blueprint('users', __name__, url_prefix='/users', static_folder='../static')

USERS = {
    1: {'name': 'Ivan'},
    2: {'name': 'Pyotr'},
    3: {'name': 'Nik'},
}

@user.route('/')
def user_list():
    return render_template(
        'users/list.html',
        users=USERS
    )

# @user.route('/<int:pk>')
# def get_user(pk: int, redirect=None):
#     try:
#         user_name = USERS[pk]
#     except KeyError:
#         raise NotFound(f'User id {pk} not found')
#         # return redirect('/users/')
#     return render_template(
#         'users/details.html',
#         user_name=user_name
#     )

@user.route('/<int:pk>')
def get_user(pk: int):
    if pk in USERS:
        user_raw = USERS[pk]
    else:
        raise NotFound(f'user id: {pk}, not found')
    return render_template(
        'users/details.html',
        user_name=user_raw['name']
    )

@user.route('/<int:pk>')
def get_user_name(pk: int, user_name=None):
    if pk in USERS:
        user_mame = USERS[pk]['name']
    else:
        raise NotFound(f'User id: {pk}, not found')
    return user_name
