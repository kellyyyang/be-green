import requests

def create_image(url):
    img_data = requests.get(url).content
    # with open('static/media/imgs/imgs.jpg', 'wb') as handler:
    #     handler.write(img_data)

    with open('tmp/imgs.jpg', 'wb') as handler:
        handler.write(img_data)


create_image("https://i.natgeofe.com/n/5f35194b-af37-4f45-a14d-60925b280986/NationalGeographic_2731043_4x3.jpg")