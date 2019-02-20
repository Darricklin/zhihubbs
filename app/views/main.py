from flask import Blueprint,request,current_app
# from app.models import
main = Blueprint("main",__name__)
@main.route('/',methods=['get'])
def index():
    return 'hello world'
