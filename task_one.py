"""
----------------------
PROBLEM STATEMENT
----------------------


The Star Wars API lists 82 main characters in the Star Wars saga.

For the first task, we would like you to use a random number generator
that picks a number between 1-82.

Using these random numbers you will be pulling 15 characters
from the API using Python.


"""
import random
import json
import requests


def generate_15_random_numbers():
    """produces 15 random numbers"""

    i = 1
    result = []
    while i <= 15:
        result.append(random.randint(1, 83))
        i += 1
    return result


def get_url(resource_id):
    home_url = "https://swapi.dev"
    relative_url = "/api/people/{}"
    absolute_url = home_url + relative_url.format(resource_id)
    return absolute_url


if __name__ == "__main__":
    """
   HOME-URL :: https://swapi.dev
   relative-URL:: /api/people/1

   URL
   https://swapi.dev/api/people/1/

   """

    resources = generate_15_random_numbers()
    print(f"[ INFO ] produced {len(resources)} random resource ids in range(1, 83).")

    data = []
    for resource_id in resources:
        print(f"[ INFO ] fetching data for resource_id {resource_id}...")
        url_ = get_url(resource_id)
        res = requests.get(url_)
        res_json = res.text
        res_dict = json.loads(res_json)
        data.append(res_dict.get("name"))

    print(data)
