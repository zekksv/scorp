from typing import List

import mysql.connector
from .constants import *
import random
from datastructures.Post import Post


def connect_db():
    try:
        cnx = mysql.connector.connect(
            user=MYSQL_USER,
            password=MYSQL_PASS,
            host=MYSQL_HOST,
            database=MYSQL_DB)
        return cnx
    except Exception as e:
        print(e)
        return None


def generate_posts_list():
    random.randint(0, 9)
    general_list = []
    id_cnt = 1
    for i in range(0, 3):
        post_list = []
        for j in range(0, random.randint(1, 5)):
            ph_post = Post(
                id=id_cnt,
                description="Test",
                image="",
                created_at=random.randint(1640000000, 1642958605),
                owner=None,  # using same Post class with question 1 so it should be defined as None
                liked=None  # using same Post class with question 1 so it should be defined as None
            )
            post_list.append(ph_post)
        general_list.append(post_list)

    return general_list


def binary_search_post(arr: List[Post], val: int, start: int, end: int):
    if start == end:
        if arr[start].created_at > val:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = (start + end) // 2

    if arr[mid].created_at < val:
        return binary_search_post(arr, val, mid + 1, end)
    elif arr[mid].created_at > val:
        return binary_search_post(arr, val, start, mid - 1)
    else:
        return mid


def insertion_sort_post(arr: List[Post]):
    for i in range(1, len(arr)):
        val = arr[i].created_at
        j = binary_search_post(arr, val, 0, i - 1)
        arr = arr[:j] + [arr[i]] + arr[j:i] + arr[i + 1:]
    return arr
