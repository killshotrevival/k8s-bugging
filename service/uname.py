import subprocess
from flask import jsonify

def uname():
    """_System information check api
    """
    out = subprocess.getoutput("uname -a")
    return jsonify({
        "data" : out
    }), 200
