import subprocess
import sys
from pathlib import Path


def _ensure_dependencies():
    try:
        import flask  # noqa: F401
        import flask_socketio  # noqa: F401
        import flask_sqlalchemy  # noqa: F401
        import flask_wtf  # noqa: F401
        import gevent  # noqa: F401
        import geventwebsocket  # noqa: F401
    except ImportError:
        req = Path(__file__).resolve().parent / "requirements.txt"
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(req)])


_ensure_dependencies()
from gevent import monkey
monkey.patch_all()
from flask import *
from flask_socketio import *
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler
app = Flask(__name__)
socketio = socketIO(app)
db = SQLAlchemy(app)
CSRFProtect(app)

@app.route()
def index():
    return render_template("index.html")
    
if __name__ == "__main__":
    server = WSGIServer(("0.0.0.0", 80), app, handler_class=WebSocketHandler)