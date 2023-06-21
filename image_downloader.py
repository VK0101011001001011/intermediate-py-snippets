import requests

image_url = 'http://example.com/image.jpg'
img_data = requests.get(image_url).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)