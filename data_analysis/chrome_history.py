#   •	Most Visited Domains: ONLY concentrating on the main domain e.g. instagram, tiktok or google and count the visits on it. Also sorting from highest to lowest.
#	•	Most Frequent Titles: Counting the titles that are the same and sorting them from highest to lowest.
#	•	Peak Browsing Hour: Displays the hour with the most visits.
#	•	Total Browsing Time: Displays the total browsing time in hours

import json
from collections import Counter
from datetime import datetime

def run_chrome_history_analysis():
    # Load Chrome history data from the JSON file
    with open("/Users/emelyjunker/Documents/Programming/Digital Human Project/data/Chrome/verlauf.json", "r") as file:
        history_data = json.load(file)

    # Access the "Browser History" key, assuming it holds the actual visit data
    visits = history_data.get("Browser History", [])

    # Initialize counters for URLs, Titles, and visit times
    url_counter = Counter()
    title_counter = Counter()
    visit_times = []    
    domain_hours_counter = {}  # Dictionary to store hours for each domain

    # Loop through each visit entry in the history
    for visit in visits:
        if isinstance(visit, dict):
            url = visit.get("url", "")  # Get the URL (defaults to empty if not found)
            title = visit.get("title", "")  # Get the title (defaults to empty if not found)
            time_usec = visit.get("time_usec", 0)  # Time in microseconds

            # Count visits by URL and Title
            if url:
                url_counter[url] += 1
                domain = url.split("/")[2]  # Extract domain from URL (e.g., "instagram.com")
                
                # Initialize the domain hour counter if it doesn't exist
                if domain not in domain_hours_counter:
                    domain_hours_counter[domain] = Counter()
                
                # Collect visit times for peak hour analysis
                hour = datetime.utcfromtimestamp(time_usec / 1_000_000).hour  # Convert to hour (24-hour format)
                domain_hours_counter[domain][hour] += 1

            if title:
                title_counter[title] += 1

            # Collect visit times for overall peak hour analysis
            visit_times.append(time_usec)

    # Most Visited Domains:
    most_visited_domains = Counter()
    for url in url_counter:
        domain = url.split("/")[2]  # Extract domain from URL
        most_visited_domains[domain] += url_counter[url]
    
    # Filter out domains with less than 5 visits
    most_visited_domains = {domain: count for domain, count in most_visited_domains.items() if count >= 5}
    most_visited_domains = Counter(most_visited_domains)  # Convert back to Counter to use most_common()

    # Top 5 Most Visited Domains:
    top_5_visited_domains = most_visited_domains.most_common(5)

    # Most Frequent Titles:
    most_frequent_titles = title_counter.most_common()  # Get all titles, sorted by frequency

    # Filter out titles with less than 5 visits
    most_frequent_titles = {title: count for title, count in most_frequent_titles if count >= 5}

    # Top 5 Most Frequent Titles:
    top_5_frequent_titles = list(most_frequent_titles.items())[:5]

    # Peak Browsing Hour (Overall):
    hours_counter = Counter()
    for time in visit_times:
        # Convert microseconds to timestamp and then to hour
        hour = datetime.utcfromtimestamp(time / 1_000_000).hour  # Convert to hour (24-hour format)
        hours_counter[hour] += 1
    
    peak_browsing_hour_overall = hours_counter.most_common(1)[0][0] if hours_counter else None

    # Format the peak browsing hour to AM/PM
    if peak_browsing_hour_overall is not None:
        peak_browsing_hour_overall_formatted = datetime.strptime(f"{peak_browsing_hour_overall}:00", "%H:%M").strftime("%I:%M %p")
    else:
        peak_browsing_hour_overall_formatted = None

    # Return the results
    return {
        "most_visited_domains": sorted(most_visited_domains.items(), key=lambda x: x[1], reverse=True),  # All domains, sorted descending
        "top_5_visited_domains": top_5_visited_domains,  # Top 5 domains
        "most_frequent_titles": sorted(most_frequent_titles.items(), key=lambda x: x[1], reverse=True),  # All titles, sorted descending
        "top_5_frequent_titles": top_5_frequent_titles,  # Top 5 titles
        "peak_browsing_hour_overall": peak_browsing_hour_overall_formatted  # Overall peak hour formatted with AM/PM
    }

# Run the analysis and print the result
chrome_history_result = run_chrome_history_analysis()

# Print the result in a readable format (like a table)
print("Most Visited Domains:")
for domain, count in chrome_history_result["most_visited_domains"]:
    print(f"{domain}: {count} visits")

print("\nTop 5 Most Visited Domains:")
for domain, count in chrome_history_result["top_5_visited_domains"]:
    print(f"{domain}: {count} visits")

print("\nMost Frequent Titles:")
for title, count in chrome_history_result["most_frequent_titles"]:
    print(f"{title}: {count} visits")

print("\nTop 5 Most Frequent Titles:")
for title, count in chrome_history_result["top_5_frequent_titles"]:
    print(f"{title}: {count} visits")

print(f"\nOverall Peak Browsing Hour: {chrome_history_result['peak_browsing_hour_overall']}")