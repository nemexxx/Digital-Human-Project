import json
def run_instagram_advertiser_analysis():
    # Load the JSON data from the file
    with open("/Users/emelyjunker/Documents/Programming/Digital Human Project/data/Instagram/ads_information/instagram_ads_and_businesses/advertisers_using_your_activity_or_information.json", "r") as file:
        data = json.load(file)

    # Access the "ig_custom_audiences_all_types" key which holds the list of advertisers
    advertisers = data.get("ig_custom_audiences_all_types", [])

    # Extract advertiser information
    advertiser_info = []
    for advertiser in advertisers:
        name = advertiser.get("advertiser_name", "Unknown")
        
        advertiser_info.append({
            "advertiser_name": name,
        })

    # Return the advertiser information
    return advertiser_info

# Run the analysis and store the result
advertiser_result = run_instagram_advertiser_analysis()