import requests
import os
from urllib.parse import urlparse, parse_qs

# Set up API key and endpoints
api_key = "AIzaSyA2FZKuqoUeOUDRw208Eo_O2wkMsgIRxPM"
search_endpoint = "https://www.googleapis.com/youtube/v3/search"
video_details_endpoint = "https://www.googleapis.com/youtube/v3/videos"

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

# Create a directory to save thumbnails
output_directory = "thumbnails"
os.makedirs(output_directory, exist_ok=True)

# Retrieve thumbnail URLs for each video and download
for video_id in video_ids:
    details_params = {
        "part": "snippet",
        "id": video_id,
        "key": api_key,
    }
    details_response = requests.get(video_details_endpoint, params=details_params)
    details_result = details_response.json()

    # Extract "high" quality thumbnail URL
    thumbnail_url = details_result["items"][0]["snippet"]["thumbnails"]["high"]["url"]

    # Parse the thumbnail URL to get the filename
    thumbnail_filename = os.path.join(output_directory, os.path.basename(urlparse(thumbnail_url).path))

    # Download the thumbnail
    with open(thumbnail_filename, 'wb') as thumbnail_file:
        thumbnail_file.write(requests.get(thumbnail_url).content)

    print(f"High-quality thumbnail for video {video_id} downloaded: {thumbnail_filename}")