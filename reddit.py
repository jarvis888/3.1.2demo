# users, comments, posts
import pandas


class User:
    def __init__(self, user_id, num_posts, reputation, mod_status, can_post):
        self.username = user_id
        self.num_posts = num_posts
        self.reputation = reputation
        self.mod_status = mod_status
        self.can_post = can_post

    def post_topic(self, title, tags, description):
        topic = Topic(title, tags, description)
        return topic


class Topic:
    def __init__(self, title, tags, description):
        self.title = title
        self.tags = tags
        self.description = description


sarah = User(99, 0, 0, True, True)
sarah.post_topic(
    "smoothies",
    ["food", "healthy"],
    "smoothies are the best. love smoothies. can't get enough smoothies.",
)
