import json

from data_analysis.config import data_path

def run_instagram_advertiser_analysis():
    # Load the JSON data from the file
    with open(data_path("Instagram", "ads_information", "instagram_ads_and_businesses", "advertisers_using_your_activity_or_information.json"), "r") as file:
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


if __name__ == "__main__":
    for advertiser in run_instagram_advertiser_analysis():
        print(advertiser["advertiser_name"])