import requests


def json_from_request(base, endpoint, path="", query=""):
    request = f"{base}{endpoint}{path}{query}"
    response = requests.get(request)
    return_data = []
    data = response.json()
    return_data += data.get("results")
    while data["next"] is not None:
        response = requests.get(data["next"])
        data = response.json()
        return_data += data.get("results")
    return return_data
