from flask import Blueprint, request, abort, make_response
from src.utils.util import output_json
from src.functions.price import get_ticket_price

pricesRouting = Blueprint('pricesRouting', __name__)


@pricesRouting.errorhandler(400)
def not_found(error):
    return make_response(output_json({'error': 'Bad request'}), 400)


@pricesRouting.errorhandler(500)
def internal_server_error(error):
    return make_response(output_json({'error': 'something failed', 'message': str(error)}), 500)


@pricesRouting.route('/prices', methods=["GET"])
def prices():
    v_type = request.args.get('type')
    age = request.args.get('age')
    date = request.args.get('date')
    if v_type and age and date:
        payload = {
            'type': str(v_type),
            'age': int(age),
            'date': str(date)
        }
    else:
        abort(400)
    try:
        response = get_ticket_price(payload)
        if 'error' in response.json:
            abort(500)
    except Exception as e:
        print(e)
        abort(500)

    return make_response(response, 200)
