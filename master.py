import os
from data_analysis.instagram_likes import run_instagram_analysis
from data_analysis.threads_likes import run_threads_analysis
from data_analysis.instagram_advertisers import run_instagram_advertiser_analysis
from data_analysis.chrome_history import run_chrome_history_analysis
from data_analysis.youtube_history import run_youtube_search_analysis, run_youtube_watch_analysis

def update_html(filename, start_marker, end_marker, new_data):
    """ Updates a specific section in an HTML file while keeping the structure intact. """
    with open(filename, "r") as file:
        html_content = file.read()

    if start_marker not in html_content or end_marker not in html_content:
        raise ValueError(f"Markers '{start_marker}' and/or '{end_marker}' are missing in {filename}!")

    # Find the content between the markers
    start_index = html_content.find(start_marker)
    end_index = html_content.find(end_marker) + len(end_marker)
    
    # Remove the old data and insert the new data
    old_data = html_content[start_index:end_index]
    updated_content = html_content.replace(old_data, f"{start_marker}\n{new_data}\n{end_marker}")

    with open(filename, "w") as file:
        file.write(updated_content)

def main():
    # Step 1: Run all analyses
    instagram_data = run_instagram_analysis()
    threads_data = run_threads_analysis()
    advertiser_data = run_instagram_advertiser_analysis()
    chrome_data = run_chrome_history_analysis()
    youtube_search_data = run_youtube_search_analysis()  # NEW: Run YouTube search analysis
    youtube_watch_data = run_youtube_watch_analysis()  # NEW: Run YouTube watch analysis

    # Step 2: Prepare HTML data for summary and full tables
    instagram_summary_data = "\n".join(
        f"<tr><td>{account}</td><td>{likes}</td></tr>"
        for account, likes in sorted(instagram_data.items(), key=lambda x: x[1], reverse=True)[:5]
    )
    threads_summary_data = "\n".join(
        f"<tr><td>{account}</td><td>{likes}</td></tr>"
        for account, likes in sorted(threads_data.items(), key=lambda x: x[1], reverse=True)[:5]
    )
    instagram_table = "\n".join(
        f"<tr><td>{account}</td><td>{likes}</td></tr>"
        for account, likes in sorted(instagram_data.items(), key=lambda x: x[1], reverse=True)
    )
    threads_table = "\n".join(
        f"<tr><td>{account}</td><td>{likes}</td></tr>"
        for account, likes in sorted(threads_data.items(), key=lambda x: x[1], reverse=True)
    )
    advertiser_table = "\n".join(
        f"<tr><td>{advertiser['advertiser_name']}</td>"
        for advertiser in advertiser_data
    )

    # Chrome Analysis Formatting
    chrome_domains_table = "\n".join(
        f"<tr><td>{domain}</td><td>{count}</td></tr>"
        for domain, count in sorted(chrome_data["most_visited_domains"], key=lambda x: x[1], reverse=True)
    )
    top_5_chrome_domains_table = "\n".join(
        f"<tr><td>{domain}</td><td>{count}</td></tr>"
        for domain, count in sorted(chrome_data["top_5_visited_domains"], key=lambda x: x[1], reverse=True)
    )
    chrome_titles_table = "\n".join(
        f"<tr><td>{title}</td><td>{count}</td></tr>"
        for title, count in sorted(chrome_data["most_frequent_titles"], key=lambda x: x[1], reverse=True)
    )
    top_5_chrome_titles_table = "\n".join(
        f"<tr><td>{title}</td><td>{count}</td></tr>"
        for title, count in sorted(chrome_data["top_5_frequent_titles"], key=lambda x: x[1], reverse=True)
    )
    peak_browsing_hour = f"<tr><td>Peak Browsing Hour</td><td>{chrome_data['peak_browsing_hour_overall']}</td></tr>"

    # YouTube Search Analysis Formatting
    youtube_search_keywords_table = "\n".join(
        f"<tr><td>{keyword}</td><td>{count}</td></tr>"
        for keyword, count in youtube_search_data["most_searched_keywords"]
    )
    peak_search_hour = f"<tr><td>Peak Search Hour</td><td>{youtube_search_data['peak_search_hour']}</td></tr>"
    
    youtube_monthly_search_trends = "\n".join(
        f"<tr><td>{month}</td><td>{count}</td></tr>"
        for month, count in youtube_search_data["monthly_search_trends"]
    )
    youtube_yearly_search_trends = "\n".join(
        f"<tr><td>{year}</td><td>{count}</td></tr>"
        for year, count in youtube_search_data["yearly_search_trends"]
    )

    # YouTube Watch Analysis Formatting
    youtube_watched_channels_table = "\n".join(
        f"<tr><td>{channel}</td><td>{count}</td></tr>"
        for channel, count in youtube_watch_data["most_watched_channels"]
    )

    youtube_top_5_watched_channels_table = "\n".join(
    f"<tr><td>{channel}</td><td>{count}</td></tr>"
    for channel, count in youtube_watch_data["top_5_watched_channels"]
    )

    youtube_watched_titles_table = "\n".join(
        f"<tr><td>{title}</td><td>{count}</td></tr>"
        for title, count in youtube_watch_data["most_watched_titles"]
    )
    
    peak_watch_hour = f"<tr><td>Peak Watch Hour</td><td>{youtube_watch_data['peak_watch_hour']}</td></tr>"
    
    youtube_monthly_watch_trends = "\n".join(
        f"<tr><td>{month}</td><td>{count}</td></tr>"
        for month, count in youtube_watch_data["monthly_watch_trends"]
    )
    youtube_yearly_watch_trends = "\n".join(
        f"<tr><td>{year}</td><td>{count}</td></tr>"
        for year, count in youtube_watch_data["yearly_watch_trends"]
    )

    # Step 3: Update each HTML file with the new data

    ## Dashboard
    update_html("website/dashboard.html", "<!-- Instagram summary data here -->", "<!-- End of Instagram summary data here -->", instagram_summary_data)
    
    update_html("website/dashboard.html", "<!-- Threads summary data here -->", "<!-- End of Threads summary data here -->", threads_summary_data)
    
    update_html("website/dashboard.html", "<!-- Chrome Top 5 Visited Domains Data -->", "<!-- End of Chrome Top 5 Visited Domains Data -->", top_5_chrome_domains_table)
    update_html("website/dashboard.html", "<!-- Chrome Top 5 Frequent Titles Data -->", "<!-- End of Chrome Top 5 Frequent Titles Data -->", top_5_chrome_titles_table)

    update_html("website/dashboard.html", "<!-- Top 5 watched youtube channels -->", "<!-- End of Top 5 watched youtube channels -->", youtube_top_5_watched_channels_table)
    update_html("website/dashboard.html", "<!-- YouTube Yearly Search Trends -->", "<!-- End of YouTube Yearly Search Trends -->", youtube_yearly_search_trends)
    update_html("website/dashboard.html", "<!-- YouTube Yearly Watch Trends -->", "<!-- End of YouTube Yearly Watch Trends -->", youtube_yearly_watch_trends)

    ## Instagram
    update_html("website/instagram.html", "<!-- Advertisers using Instagram data here -->", "<!-- End of Advertisers using Instagram data here -->", advertiser_table)
    update_html("website/instagram.html", "<!-- Instagram Likes Data -->", "<!-- End of Instagram Likes Data -->", instagram_table)

    ## Threads
    update_html("website/threads.html", "<!-- Threads Likes Data -->", "<!-- End of Threads Likes Data -->", threads_table)

    ## Chrome
    update_html("website/chrome.html", "<!-- Chrome Most Visited Domains Data -->", "<!-- End of Chrome Most Visited Domains Data -->", chrome_domains_table)
    update_html("website/chrome.html", "<!-- Chrome Most Frequent Titles Data -->", "<!-- End of Chrome Most Frequent Titles Data -->", chrome_titles_table)
    update_html("website/chrome.html", "<!-- Chrome Peak Browsing Hour -->", "<!-- End of Chrome Peak Browsing Hour -->", peak_browsing_hour)

    ## YouTube
    
    #YouTube Search Analysis:
    update_html("website/youtube.html", "<!-- YouTube Search Data -->", "<!-- End of YouTube Search Data -->", youtube_search_keywords_table)
    update_html("website/youtube.html", "<!-- YouTube Peak Search Hour -->", "<!-- End of YouTube Peak Search Hour -->", peak_search_hour)
    update_html("website/youtube.html", "<!-- YouTube Monthly Search Trends -->", "<!-- End of YouTube Monthly Search Trends -->", youtube_monthly_search_trends)
    update_html("website/youtube.html", "<!-- YouTube Yearly Search Trends -->", "<!-- End of YouTube Yearly Search Trends -->", youtube_yearly_search_trends)

    #YouTube Watch Analysis:
    update_html("website/youtube.html", "<!-- Top 5 watched youtube channels -->", "<!-- End of Top 5 watched youtube channels -->", youtube_top_5_watched_channels_table)
    update_html("website/youtube.html", "<!-- Watched youtube channels -->", "<!-- End of Watched youtube channels -->", youtube_watched_channels_table)
    update_html("website/youtube.html", "<!-- Watched youtube titles -->", "<!-- End of Watched youtube titles -->", youtube_watched_titles_table)
    update_html("website/youtube.html", "<!-- YouTube Peak Watch Hour -->", "<!-- End of YouTube Peak Watch Hour -->", peak_watch_hour)
    update_html("website/youtube.html", "<!-- YouTube Monthly Watch Trends -->", "<!-- End of YouTube Monthly Watch Trends -->", youtube_monthly_watch_trends)
    update_html("website/youtube.html", "<!-- YouTube Yearly Watch Trends -->", "<!-- End of YouTube Yearly Watch Trends -->", youtube_yearly_watch_trends)


# Step 4: Open the dashboard (assuming Mac, adjust if on Windows)
    os.system("open website/dashboard.html")  # Open in browser (Mac: "open", Windows: "start")

if __name__ == "__main__":
    main()