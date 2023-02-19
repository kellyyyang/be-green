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

BURGER_URL = "https://static.onecms.io/wp-content/uploads/sites/43/2022/09/26/25473-the-perfect-basic-burger-ddmfs-4x3-1350-1.jpg"
CHICKEN_URL = 'https://tmbidigitalassetsazure.blob.core.windows.net/rms3-prod/attachments/37/1200x1200/Crispy-Fried-Chicken_EXPS_TOHJJ22_6445_DR%20_02_03_11b.jpg'
PORK_URL = 'https://assets.epicurious.com/photos/54e7ad824f77a310045d7835/16:9/w_2000,h_1125,c_limit/EP-201502-Pork-6x4.jpg'

# This is how you authenticate.
metadata = (("authorization", f"Key {API_KEY}"),)


def get_label(input_url):
    ''' input:  input_url, a string representing the input URL
        output: the highest-probability label (name, CO2 emissions)
    '''
    request = service_pb2.PostModelOutputsRequest(

    # This is the model ID of a publicly available food model. You may use any other public or custom model ID.
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

    output = []

    for concept in response.outputs[0].data.concepts:
        output.append(concept.name)
        # print("%12s: %.2f" % (concept.name, concept.value))

    return output

# print(get_label(BURGER_URL))