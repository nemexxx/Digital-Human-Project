# data_analysis/instagram_analysis.py
import json

def run_instagram_analysis():
    # Load the JSON data from the file
    with open("/Users/emelyjunker/Documents/Programming/Digital Human Project/Data/Instagram/your_instagram_activity/likes/liked_posts.json", "r") as file:
        data = json.load(file)

    # Access the "likes_media_likes" key, which holds the list of posts
    posts = data.get("likes_media_likes", [])

    # Count likes per account
    like_counts = {}  # Dictionary to store counts

    # Loop through the posts and count the likes per account
    for post in posts:
        if isinstance(post, dict):
            account = post.get("title", "Unknown")  # Safely get the account name
            like_counts[account] = like_counts.get(account, 0) + 1  # Count occurrences

    # Filter accounts with fewer than 5 likes
    filtered_likes = {account: count for account, count in like_counts.items() if count >= 5}

    # Sort accounts by most likes
    sorted_likes = sorted(filtered_likes.items(), key=lambda x: x[1], reverse=True)

    # Return the result as a dictionary
    return {account: count for account, count in sorted_likes}

# Run the analysis and store the result
instagram_result = run_instagram_analysis()