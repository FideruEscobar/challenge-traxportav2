from app import app


def test_base():
    with app.test_client() as client:
        response = client.get(
            '/prices', query_string={'age': 20, 'date': '2020-05-08', 'type': 'Jour'})
        json_data = response.get_json()

        assert json_data['cost'] == 190


def test_night():
    with app.test_client() as client:
        response = client.get(
            '/prices', query_string={'age': 20, 'date': '2020-05-08', 'type': 'Night'})
        json_data = response.get_json()

        assert json_data['cost'] == 19


def test_child():
    with app.test_client() as client:
        response = client.get(
            '/prices', query_string={'age': 5, 'date': '2020-05-08', 'type': 'Jour'})
        json_data = response.get_json()

        assert json_data['cost'] == 0


def test_elderly():
    with app.test_client() as client:
        response = client.get(
            '/prices', query_string={'age': 65, 'date': '2020-05-08', 'type': 'Jour'})
        json_data = response.get_json()

        assert json_data['cost'] == 143


def test_elderly_on_monday():
    with app.test_client() as client:
        response = client.get(
            '/prices', query_string={'age': 65, 'date': '2023-03-13', 'type': 'Jour'})
        json_data = response.get_json()

        assert json_data['cost'] == 93


def test_elderly_night():
    with app.test_client() as client:
        response = client.get(
            '/prices', query_string={'age': 65, 'date': '2020-05-08', 'type': 'Night'})
        json_data = response.get_json()

        assert json_data['cost'] == 8


def test_holiday():
    with app.test_client() as client:
        response = client.get(
            '/prices', query_string={'age': 20, 'date': '2020-12-25', 'type': 'Jour'})
        json_data = response.get_json()

        assert json_data['cost'] == 190


def test_monday():
    with app.test_client() as client:
        response = client.get(
            '/prices', query_string={'age': 20, 'date': '2020-05-04', 'type': 'Jour'})
        json_data = response.get_json()

        assert json_data['cost'] == 124


def test_error():
    with app.test_client() as client:
        response = client.get(
            '/prices', query_string={'age': 20, 'type': 'jour', 'date': '2023-03-13'})
        json_data = response.get_json()

        assert json_data['error'] == "something failed"


def test_bad_request():
    with app.test_client() as client:
        response = client.get(
            '/prices', query_string={'age': 20, 'type': 'jour'})
        json_data = response.get_json()

        assert json_data['error'] == 'Bad request'
