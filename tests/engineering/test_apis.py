from mcdevtools.engineering import apis


def test_send_get_request():

    response = apis.send_get_request('https://google.com')

    assert response.ok == True
