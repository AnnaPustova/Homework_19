import requests
import os


url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}


response = requests.get(url, params=params)
response.raise_for_status()  


photos = response.json().get('photos', [])


os.makedirs('mars_photos', exist_ok=True)


for idx, photo in enumerate(photos, start=1):
    img_url = photo['img_src']
    img_data = requests.get(img_url).content
    with open(f'mars_photos/mars_photo{idx}.jpg', 'wb') as handler:
        handler.write(img_data)
    print(f"Downloaded mars_photo{idx}.jpg")

print(f"Number of photos found: {len(photos)}")
