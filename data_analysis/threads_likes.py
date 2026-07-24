import json

from data_analysis.config import data_path

def run_threads_analysis():
    # Load the JSON data from the file
    with open(data_path("Instagram", "your_instagram_activity", "threads", "liked_threads.json"), "r") as file:
        data = json.load(file)

    # Access the "text_post_app_media_likes" key, which holds the list of posts
    posts = data.get("text_post_app_media_likes", [])

    # Count likes per account
    like_counts = {}  # Dictionary to store counts

    # Loop through the posts and count the likes per account
    for post in posts:
        if isinstance(post, dict):
            account = post.get("title", "Unknown")  # Safely get the account name
            like_counts[account] = like_counts.get(account, 0) + len(post.get("string_list_data", []))  # Count occurrences

    # Filter accounts with more than 1 like (you can adjust this number if needed)
    filtered_likes = {account: count for account, count in like_counts.items() if count > 1}

    # Sort accounts by most likes
    sorted_likes = sorted(filtered_likes.items(), key=lambda x: x[1], reverse=True)

    # Return the result as a dictionary
    return {account: count for account, count in sorted_likes}


if __name__ == "__main__":
    for account, count in run_threads_analysis().items():
        print(f"{account}: {count} likes")