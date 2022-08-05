from flask import Flask, request

from service.health import health
from service.service_check import service_check
from service.uname import uname

app = Flask(__name__)

@app.route('/health')
def health_check():
    """Simple health check request handler

    Returns:
        json: Json response
    """
    return health()


@app.route('/service', methods=['GET', 'POST'])
def service_check_support():
    """Service check function, that can be use to redirect the call to a different service

    Returns:
        json: Json response
    """
    return service_check(request)

@app.route("/uname")
def uname_support():
    """Simple uname check request handler

    Returns:
        json: Json response
    """
    return uname()


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8131)
