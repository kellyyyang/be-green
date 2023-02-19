import requests

def create_image(url):
    img_data = requests.get(url).content
    # with open('static/media/imgs/imgs.jpg', 'wb') as handler:
    #     handler.write(img_data)

    with open('tmp/imgs.jpg', 'wb') as handler:
        handler.write(img_data)