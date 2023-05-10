import praw
import pymongo
# Set up authentication
reddit = praw.Reddit(
    client_id=" ",
    client_secret=" ",
    user_agent=" "
    )

# Set the URL of the post
url = "https://www.reddit.com/r/Layoffs/comments/12spouo/nordstrom_layed_off_2025_it_workforce_without/'"

# Get the post and its comments
submission = reddit.submission(url=url)
submission.comments.replace_more(limit=None)

# Define a function to traverse and store the comments
def traverse_comments(comments):
    comment_list = []
    for comment in comments:
        comment_data = {
            "commentId": comment.id,
            "comment": comment.body,
            "replies": []
        }
        if comment.replies:
            comment_data["replies"] = traverse_comments(comment.replies)
        comment_list.append(comment_data)
    return comment_list

# Connect to MongoDB
client = pymongo.MongoClient()

db = client["Reddit"]
comments_collection = db["Comments"]
comments_collection.drop()  

# Store the comments in MongoDB
comments_data = {
    "commentId": submission.id,
    "replies": traverse_comments(submission.comments)
}

comments_collection.insert_one(comments_data)
