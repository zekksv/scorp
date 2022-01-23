from typing import List
from datastructures.Post import Post
from datastructures.User import User
from .helpers import *

def get_posts(user_id: int, post_ids: List[int]) -> List[Post]:
    post_ids_prepared = ','.join(list(map(str, post_ids)))

    cnx = connect_db()
    final_array = []
    if cnx != None:
        connection = cnx.cursor()
        query = "SELECT * FROM post WHERE id IN ({post_ids})"
        connection.execute(query.format(post_ids=post_ids_prepared))
        for data_item in connection:
            # Querying post owner data
            query_for_post_owner = "SELECT * FROM user WHERE id = %s"
            cnx_post_owner = connect_db()
            connection_for_post_owner = cnx_post_owner.cursor()
            connection_for_post_owner.execute(query_for_post_owner, (str(data_item[2]),))
            post_owner_db_data = connection_for_post_owner.fetchone()
            connection_for_post_owner.close()
            cnx_post_owner.close()

            # Querying if the provided user follows post owner
            query_for_follow_info = "SELECT * FROM follow WHERE follower_id = %s AND following_id = %s"
            cnx_follow_info = connect_db()
            connection_for_follow_info = cnx_follow_info.cursor()
            connection_for_follow_info.execute(query_for_follow_info, (str(user_id), str(post_owner_db_data[0])))
            follow_info_db_data = connection_for_follow_info.fetchone()
            connection_for_follow_info.close()
            cnx_follow_info.close()

            # Querying if current user liked the post
            query_for_post_like = "SELECT * FROM likes WHERE post_id = %s AND user_id = %s"
            cnx_post_like = connect_db()
            connection_for_post_like = cnx_post_like.cursor()
            connection_for_post_like.execute(query_for_post_like, (str(data_item[0]), user_id,))
            post_like_db_data = connection_for_post_like.fetchone()
            connection_for_post_like.close()
            cnx_post_like.close()

            if follow_info_db_data == None:
                is_followed = False
            else:
                is_followed = True

            if post_like_db_data == None:
                is_liked = False
            else:
                is_liked = True

            post_owner = User(
                id=post_owner_db_data[0],
                username=post_owner_db_data[1],
                email=post_owner_db_data[2],
                full_name=post_owner_db_data[3],
                profile_picture=post_owner_db_data[4],
                bio=post_owner_db_data[5],
                created_at=post_owner_db_data[6],
                followed=is_followed
            )
            post_item = Post(
                id=data_item[0],
                description=data_item[1],
                owner=post_owner,
                image=data_item[3],
                created_at=data_item[4],
                liked=is_liked
            )
            final_array.append(post_item)

        connection.close()
        cnx.close()


    return final_array


def merge_posts(list_of_posts: List[List[Post]]) -> List[Post]:
    list_of_posts = [x for l in list_of_posts for x in l]           #merging arrays into one
    result = insertion_sort_post(list_of_posts)                     #applying binary insertion
    return result