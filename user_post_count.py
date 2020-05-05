import requests
import json

def test_user_and_posts_count():
    URL = "https://jsonplaceholder.typicode.com/posts"
    # Referance dict to assert
    referance_dict = {1: 10, 2: 10, 3: 10, 4: 10, 5: 10, 6: 10, 7: 10, 8: 10, 9: 10, 10: 10}
    headers = {
	    'Content-Type': "application/json"
	    }

    response = requests.request("GET", URL, headers=headers)
    response_body = json.loads(response.text)

    post_count = {}

    for i in response_body:
        if i['userId'] not in post_count:
            post_count[i['userId']] = 0
        post_count[i['userId']] += 1


    # Asserting lenght and referance dict 

    assert response.status_code == 200
    assert len(response_body) == 100
    assert post_count.items() == referance_dict.items()
    

    post_id = []

    for item in response_body:
        post_id.append(item["id"])

    #converting post_id array to set which can't include duplicate items
    unique_post_ids = set(post_id)

    # Asserting that unique_post_ids count equals to lenght of returned body
    assert len(unique_post_ids) == len(response_body)
