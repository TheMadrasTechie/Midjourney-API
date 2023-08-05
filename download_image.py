import requests
import json
import os
from PIL import Image
from io import BytesIO
import time

def fetch_and_store_image(tsk_id):

    time.sleep(15)  # Sleep for 10 seconds at the beginning

    # Post request
    url = "https://api.midjourneyapi.io/v2/result"
    headers = {
        "Authorization": "API_key",  # Replace 'API_key' with your actual API key
        "Content-Type": "application/json"
    }
    data = {
        "taskId": tsk_id
    }

    while True:  # Keep trying until successful
        response = requests.post(url, headers=headers, data=json.dumps(data))

        # If request is successful
        if response.status_code == 200:
            json_response = response.json()

            # Get imageURL from the response
            image_url = json_response.get("imageURL")

            # If imageURL is not None, get the image
            if image_url is not None:
                response = requests.get(image_url)
                img = Image.open(BytesIO(response.content))

                # Check if midjourney_images directory exists, if not, create it
                if not os.path.exists('midjourney_images'):
                    os.makedirs('midjourney_images')

                # Save the image
                img.save(os.path.join('midjourney_images', f'{data["taskId"]}.jpg'))

                print("Image has been downloaded and stored.")
                break  # Exit the loop once the image has been downloaded and stored

        # If request is not successful or imageURL is None, sleep for 5 seconds before trying again
        time.sleep(5)


