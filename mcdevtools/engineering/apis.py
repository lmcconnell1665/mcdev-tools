import requests

def send_get_request(url):
    """
    Sends a GET request to the provided URL

    :param url: URL to send request to
    :type url: str
    :return: Response object
    """

    response = requests.get(url)

    return response
