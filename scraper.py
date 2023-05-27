
import praw
import csv
from datetime import datetime

reddit = praw.Reddit(
    client_id='',
    client_secret='',
    user_agent='',
)


subreddit_name = ''



csv_filename = 'reddit_data.csv'
csv_file = open(csv_filename, 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Type','Date', 'Author','Title', 'Content', 'Number of Comments', 'Score'])


subreddit = reddit.subreddit(subreddit_name)
posts = subreddit.new(limit= None)

for post in posts:
    content_type = 'post'
    post_title = post.title
    post_content = post.selftext
    post_date = datetime.utcfromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S')
    try:
        post_author = post.author.name
    except:
        pass
    num_comments = post.num_comments
    post_score = post.score
    post.comments.replace_more(limit=None)
    comments = post.comments.list()
    csv_writer.writerow([content_type, post_date, post_author, post_title, post_content, num_comments, post_score])

    for comment in comments:
        comment_score = comment.score
        content_type = 'comment'
        comment_date = datetime.utcfromtimestamp(comment.created_utc).strftime('%Y-%m-%d %H:%M:%S')
        try:
            comment_author = comment.author.name
        except:
            pass
        comment_data = comment.body
        csv_writer.writerow([content_type, comment_date, comment_author,'', comment_data, '',comment_score])

csv_file.close()
~                
