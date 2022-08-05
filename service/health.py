from datetime import datetime
from flask import jsonify

def health():
    """Health request handler

    Returns:
        _type_: Json response
    """
    return jsonify({
        "health" : "Alive and healthy",
        "time" : datetime.now().strftime("%Y/%m/%d %H:%M")
    }), 200
