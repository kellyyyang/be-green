from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc

stub = service_pb2_grpc.V2Stub(ClarifaiChannel.get_grpc_channel())

from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('ALL_SCOPES_API_KEY')
APP_ID = os.getenv('APP_ID')
# SAMPLE_URL = "https://samples.clarifai.com/metro-north.jpg"
SAMPLE_URL = "https://i.natgeofe.com/n/5f35194b-af37-4f45-a14d-60925b280986/NationalGeographic_2731043_4x3.jpg"
BURGER_URL = "https://assets.afcdn.com/recipe/20130627/42230_w1024h1024c1cx1250cy1875.jpg"

# This is how you authenticate.
metadata = (("authorization", f"Key {API_KEY}"),)


def get_label(input_url):
    ''' input:  input_url, a string representing the input URL
        output: the highest-probability label (name, CO2 emissions)
    '''
    request = service_pb2.PostModelOutputsRequest(

    # This is the model ID of a publicly available General model. You may use any other public or custom model ID.
    model_id="9504135848be0dd2c39bdab0002f78e9",
    user_app_id=resources_pb2.UserAppIDSet(app_id=APP_ID),
    inputs=[
        resources_pb2.Input(
            data=resources_pb2.Data(image=resources_pb2.Image(url=input_url))
            )
        ],
    )
    response = stub.PostModelOutputs(request, metadata=metadata)

    if response.status.code != status_code_pb2.SUCCESS:
        print(response)
        raise Exception(f"Request failed, status code: {response.status}")

    for concept in response.outputs[0].data.concepts:
        print("%12s: %.2f" % (concept.name, concept.value))

    output, value = response.outputs[0].data.concepts[0].name, response.outputs[0].data.concepts[0].value

    return (output, value)

get_label(BURGER_URL)
# print(get_label(BURGER_URL))