from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
import logging
import socket
from flask import jsonify, redirect, request
import pprint
from ibcntr.DB import rData
from ibcntr import app

bats = Blueprint('bats', __name__)

pp = pprint.pp
logger = logging.getLogger(__name__)
rds = rData(
      url=app.config['REDIS_URL']
    , logger=logger
    )
# ------------------------------ ROUTES bats    
@bats.route("/bats")
def index():
    rds.get_bats()
    return render_template("bats.tpl", ibs=rds.bats, title='Состояние заданий на перезагрузку ИБ', images=app.config['CONF_IMAGES'], user=current_user)

@bats.route("/on/<bat>")
def bat_on(bat):
    hostname = _get_remote(request)
    rds.switch(bat, True, remote=hostname, userid=current_user.id)
    return  redirect("/bats")

@bats.route("/off/<bat>")
def bat_off(bat):
    hostname = _get_remote(request)
    rds.switch(bat, False, remote=hostname, userid=current_user.id)
    return redirect("/bats")

@bats.route("/q/<bat>")
def rquery(bat):
    return rds.rquery(bat)
    
@bats.route("/initialize_db_fast")
def init_db():
    rds._init_db()
    return redirect("/")

@bats.route("/log/<bat>")
def log_ib_loading(bat):
    rds.log_ib_loading(bat)
    return ""

@bats.route("/info")
@bats.route("/help")
def help():
    from ibcntr.mock import help
    return help

# ------------------------------

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.tpl'), 404

@app.errorhandler(500)
def internal_error(error):
    print('-----------ERROR---------', error)
    return render_template('500.tpl'), 500

# ------------------------------
@app.context_processor
def utility_processor():
    def format_date(dt):
        import datetime
        # app.logger.debug(f'got "{dt}":({type(dt)}) parameter for formatting')
        if dt is None or str(dt) == '' or dt == '0': 
            return "0001-01-01 0:0"
        return datetime.datetime.fromisoformat(dt).strftime("%d-%m-%y %H:%M")
    def on_off(state: str):
        return "отключен" if (state=="off") else "включен"
    return {"format_date":format_date, "on_off":on_off}
    def user_name(id):
      pass

def _get_remote(request):
    _ip = request.remote_addr
    if not _ip=="":
        try:
            hostname = socket.gethostbyaddr(_ip)
            remote = hostname[0].split('.')[0]
        except socket.herror:
            remote = _ip
    else:
        remote = "<>"
    return remote
