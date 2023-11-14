import requests

# Set up API key and endpoint
api_key = "AIzaSyA2FZKuqoUeOUDRw208Eo_O2wkMsgIRxPM"
search_endpoint = "https://www.googleapis.com/youtube/v3/search"

# Define search parameters
search_params = {
    "part": "snippet",
    "q": "Fortnite",
    "maxResults": 100, # Adjust as needed
    "key": api_key,
}

# Make the search request
search_response = requests.get(search_endpoint, params=search_params)
search_results = search_response.json()

# Extract video IDs
video_ids = [item["id"]["videoId"] for item in search_results["items"]]

# Set up endpoint for video details
video_details_endpoint = "https://www.googleapis.com/youtube/v3/videos"

# Retrieve thumbnail URLs for each video
for video_id in video_ids:
    details_params = {
        "part": "snippet",
        "id": video_id,
        "key": api_key,
    }
    details_response = requests.get(video_details_endpoint, params=details_params)
    details_result = details_response.json()
    
    # Extract thumbnail URL (adjust size as needed)
    thumbnail_url = details_result["items"][0]["snippet"]["thumbnails"]["medium"]["url"]
    print(f"Thumbnail URL for video {video_id}: {thumbnail_url}")