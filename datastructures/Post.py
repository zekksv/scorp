from dataclasses import dataclass
from datastructures.User import User
@dataclass
class Post:
    id: int
    description: str
    owner: User
    image: str
    created_at: int
    liked: bool