import json
from flask import Flask, request
from includes.core_functions import get_posts as get_posts_wrapped
from includes.core_functions import merge_posts as merge_posts_wrapped
from includes.helpers import *
app = Flask(__name__)

@app.route('/merge_posts', methods=['POST'])
def merge_posts():
    if request.method == 'POST':
        #Generating post lists with different lengths
        generated_post_list = generate_posts_list()     #Generating posts to test function
        original_list = merge_posts_wrapped(generated_post_list)

        json_obj = []
        for item in original_list:
            json_obj.append({
                "id": item.id,
                "description": item.description,
                "image": item.image,
                "created_at": item.created_at
            })

        return json.dumps(json_obj)

    else:
        return "Request method is not allowed."

@app.route('/get_posts', methods=['POST'])
def get_posts():
    if request.method == 'POST':

        if (request.get_json() != None):
            data = request.get_json()
            if JSON_USER_ID_KEY not in data.keys():
                return JSON_USER_ID_KEY + " is not provided as request parameter."
            if JSON_POST_IDS_KEY not in data.keys():
                return JSON_POST_IDS_KEY + " is not provided as request parameter."

            answer = get_posts_wrapped(user_id=data[JSON_USER_ID_KEY], post_ids=data[JSON_POST_IDS_KEY])

            print(answer)
            json_obj = []
            for item in answer:
                json_obj.append({
                    "id": item.id,
                    "description": item.description,
                    "owner": {
                        "id": item.owner.id,
                        "username": item.owner.username,
                        "email": item.owner.email,
                        "full_name": item.owner.full_name,
                        "profile_picture": item.owner.profile_picture,
                        "bio": item.owner.bio,
                        "followed": item.owner.followed,
                        "created_at": item.owner.created_at
                    },
                    "image": item.image,
                    "created_at": item.created_at,
                    "liked": item.liked
                })


            return json.dumps(json_obj)
        else:
            return "Provided json body is None. Please make sure your 'Content-Type' property is set to 'application/json' while making request."

    else:
        return "Request method is not allowed."


if __name__ == '__main__':
    app.run()
