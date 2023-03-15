from flask import Blueprint, render_template

report = Blueprint("report", __name__, url_prefix="/reports", static_folder="../static")


@report.route("/")
def report_list():
    return render_template(
        "base.html",
        reports=[1,231,4]
    )












# from flask import Blueprint, render_template
#
# report = Blueprint('report', __name__, url_prefix='reports', static_folder='../static')
#
# @report.route('/')
# def report_list():
#     return render_template(
#         'reports/list.html',
#         reports = [1, 2, 3, 4, 5]
#     )
