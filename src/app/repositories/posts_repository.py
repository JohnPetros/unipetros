from typing import Dict, List

from database import mysql

from entities.post import Post


class PostsRepository:
    def get_posts(self) -> List[Post]:
        posts = mysql.query(sql="SELECT * FROM posts", is_single=False)

        return [self.__get_post_entity(post) for post in posts]

    def get_posts_count_by_category(self) -> List[Dict]:
        return mysql.query(
            sql="""
                SELECT category, COUNT(category) AS count 
                FROM posts 
                GROUP BY category
                """,
            is_single=False,
        )

    def __get_post_entity(self, post_data: Dict) -> Post:
        return Post(
            id=post_data["id"],
            title=post_data["title"],
            content=post_data["content"],
            category=post_data["category"],
        )
