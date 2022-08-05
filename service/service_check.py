import requests
from flask import jsonify


def service_check(request):
    """Function for cousin service testing

    Args:
        request (_type_): Request module

    Returns:
        _type_: _description_
    """
    redirect_url = request.args.get("redirect")
    print("redirect url found", redirect_url)

    if not redirect_url:
        return jsonify({
            "error": "No redirect url found"
        }), 400
    print(request.method)
    res = requests.request(
        url=redirect_url,
        params= request.args,
        data= request.data,
        # json= request.json,
        headers= request.headers,
        method=request.method)
    return res.text, res.status_code
