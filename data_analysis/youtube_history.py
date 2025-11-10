#	1.	YouTube Search Analysis:
#	•	most_searched_keywords, youtube_search_keywords_table, <!-- YouTube Search Data -->
#	•	peak_search_hour_formatted, peak_search_hour, <!-- YouTube Peak Search Hour -->
#	•	monthly_search_trends, youtube_monthly_search_trends, <!-- YouTube Monthly Search Trends -->
#	•	yearly_search_trends, youtube_yearly_search_trends, <!-- YouTube Yearly Search Trends -->

#	2.	YouTube Watch Analysis:
#	•	top_5_watched_channels, youtube_top_5_watched_channels_table, <!-- Top 5 watched youtube channels -->
#	•	most_watched_channels, youtube_watched_channels_table, <!-- Watched youtube channels -->
#	•	most_watched_titles, youtube_watched_titles_table, <!-- Watched youtube titles -->
#	•	peak_watch_hour, peak_watch_hour, <!-- YouTube Peak Watch Hour -->
#	•	monthly_watch_trends, youtube_monthly_watch_trends, <!-- YouTube Monthly Watch Trends -->
#	•	yearly_watch_trends, youtube_yearly_watch_trends, <!-- YouTube Yearly Watch Trends -->


import json
from collections import Counter
from datetime import datetime

def run_youtube_search_analysis():
    # Load YouTube search history JSON file
    with open("/Users/emelyjunker/Documents/Programming/Digital Human Project/data/YouTube/Verlauf/Suchverlauf.json", "r") as file:
        search_data = json.load(file)

    # Initialize counters
    keyword_counter = Counter()
    hours_counter = Counter()
    monthly_trends = Counter()
    yearly_trends = Counter()

    # Process search history
    for entry in search_data:
        if isinstance(entry, dict):
            title = entry.get("title", "")
            search_time = entry.get("time", "")

            # Extract search keywords from the title (removing "Gesucht nach: ")
            if title.startswith("Gesucht nach: "):
                keyword = title.replace("Gesucht nach: ", "").strip()
                keyword_counter[keyword] += 1

            # Convert timestamp to datetime
            try:
                search_datetime = datetime.fromisoformat(search_time.replace("Z", "+00:00"))
                hour = search_datetime.hour
                month_year = search_datetime.strftime("%Y-%m")  # Format: YYYY-MM
                year = search_datetime.strftime("%Y")  # Format: YYYY

                hours_counter[hour] += 1
                monthly_trends[month_year] += 1
                yearly_trends[year] += 1
            except ValueError:
                continue  # Skip invalid dates

    # Get most searched keywords (sorted)
    most_searched_keywords = keyword_counter.most_common()

    # Get peak search hour
    peak_search_hour = hours_counter.most_common(1)[0][0] if hours_counter else None
    peak_search_hour_formatted = datetime.strptime(f"{peak_search_hour}:00", "%H:%M").strftime("%I:%M %p") if peak_search_hour is not None else None

    return {
        "most_searched_keywords": most_searched_keywords,
        "peak_search_hour": peak_search_hour_formatted,
        "monthly_search_trends": sorted(monthly_trends.items(), key=lambda x: x[0]),  # Sorted chronologically
        "yearly_search_trends": sorted(yearly_trends.items(), key=lambda x: x[0])  # Sorted by year
    }


def run_youtube_watch_analysis():
    # Load YouTube watch history JSON file
    with open("/Users/emelyjunker/Documents/Programming/Digital Human Project/data/YouTube/Verlauf/Wiedergabeverlauf.json", "r") as file:
        watch_data = json.load(file)
    
    # Initialize counters
    channel_counter = Counter()
    title_counter = Counter()
    hours_counter = Counter()
    monthly_trends = Counter()
    yearly_trends = Counter()

    # Process watch history
    for entry in watch_data:
        if isinstance(entry, dict):
            title = entry.get("title", "").replace(" angesehen", "").strip()  # Remove "angesehen"
            channel_info = entry.get("subtitles", [{}])[0]  # Get first channel if available
            channel_name = channel_info.get("name", "Unknown Channel")
            watch_time = entry.get("time", "")

            # Count video titles
            if title:
                title_counter[title] += 1

            # Count channel occurrences
            if channel_name:
                channel_counter[channel_name] += 1

            # Convert timestamp to datetime
            try:
                watch_datetime = datetime.fromisoformat(watch_time.replace("Z", "+00:00"))
                hour = watch_datetime.hour
                month_year = watch_datetime.strftime("%Y-%m")  # Format: YYYY-MM
                year = watch_datetime.strftime("%Y")  # Format: YYYY

                hours_counter[hour] += 1
                monthly_trends[month_year] += 1
                yearly_trends[year] += 1
            except ValueError:
                continue  # Skip invalid dates

    # Filter out channels with fewer than 5 videos
    filtered_channels = {channel: count for channel, count in channel_counter.items() if count >= 5}

    # Get top 5 most watched channels (sorted)
    top_5_watched_channels = sorted(filtered_channels.items(), key=lambda x: x[1], reverse=True)[:5]

    # Get most watched channels (sorted, excluding channels with fewer than 5 views)
    most_watched_channels = sorted(filtered_channels.items(), key=lambda x: x[1], reverse=True)

    # Get most watched video titles (sorted, excluding titles with fewer than 5 views)
    most_watched_titles = [title for title in title_counter.most_common() if title[1] >= 5]

    # Get peak watch hour
    peak_watch_hour = hours_counter.most_common(1)[0][0] if hours_counter else None
    peak_watch_hour_formatted = datetime.strptime(f"{peak_watch_hour}:00", "%H:%M").strftime("%I:%M %p") if peak_watch_hour is not None else None

    return {
        "most_watched_channels": most_watched_channels,
        "top_5_watched_channels": top_5_watched_channels,  # New variable showing the top 5 channels
        "most_watched_titles": most_watched_titles,
        "peak_watch_hour": peak_watch_hour_formatted,
        "monthly_watch_trends": sorted(monthly_trends.items(), key=lambda x: x[0]),  # Sorted chronologically
        "yearly_watch_trends": sorted(yearly_trends.items(), key=lambda x: x[0])  # Sorted by year
    }

# Run analysis
youtube_search_result = run_youtube_search_analysis()
youtube_watch_result = run_youtube_watch_analysis()

# Print Search History results
print("\nMost Searched Keywords:")
for keyword, count in youtube_search_result["most_searched_keywords"]:
    print(f"{keyword}: {count} searches")

print(f"\nPeak YouTube Search Hour: {youtube_search_result['peak_search_hour']}")

print("\nMonthly Search Trends:")
for month, count in youtube_search_result["monthly_search_trends"]:
    print(f"{month}: {count} searches")

print("\nYearly Search Trends:")
for year, count in youtube_search_result["yearly_search_trends"]:
    print(f"{year}: {count} searches")

# Print Watch History Results
print("\nMost Watched Video Titles:")
for title, count in youtube_watch_result["most_watched_titles"]:
    print(f"{title}: {count} views")

print(f"\nPeak YouTube Watch Hour: {youtube_watch_result['peak_watch_hour']}")

print("\nMost Watched Channels (with at least 3 views):")
for channel, count in youtube_watch_result["most_watched_channels"]:
    print(f"{channel}: {count} views")

print("\nMonthly Watch Trends:")
for month, count in youtube_watch_result["monthly_watch_trends"]:
    print(f"{month}: {count} videos watched")

print("\nYearly Watch Trends:")
for year, count in youtube_watch_result["yearly_watch_trends"]:
    print(f"{year}: {count} videos watched")

    print("\nTop 5 Most Watched Channels:")
for channel, count in youtube_watch_result["top_5_watched_channels"]:
    print(f"{channel}: {count} views")