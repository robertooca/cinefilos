from src.schemas.forum import Post
from src.db.database import getDB, saveDB

class PostService:

    @staticmethod
    def get_posts_by_topic(topic: str):
        db = getDB()
        posts = []
        for post in db["posts"]:
            if post["topic"] == topic:
                posts.append(post)
        return posts

    @staticmethod
    def get_post_by_id(post_id: str):
        db = getDB()
        for post in db["posts"]:
            if post["id"] == post_id:
                return post
        return None

    @staticmethod
    def get_posts_by_author(author: User):
        db = getDB()
        posts = []
        for post in db["posts"]:
            if post["author"] == author:
                posts.append(post)
        return posts