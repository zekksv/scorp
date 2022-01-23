from dataclasses import dataclass


@dataclass
class User:
    id: int
    username: str
    email: str
    full_name: str
    profile_picture: str
    bio: str
    followed: bool
    created_at: int
