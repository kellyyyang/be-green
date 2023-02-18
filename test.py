
import requests

image_url = "http://t0.gstatic.com/licensed-image?q=tbn:ANd9GcQkrjYxSfSHeCEA7hkPy8e2JphDsfFHZVKqx-3t37E4XKr-AT7DML8IwtwY0TnZsUcQ"

img_data = requests.get(image_url).content
with open('static/media/imgs.jpg', 'wb') as handler:
    handler.write(img_data)