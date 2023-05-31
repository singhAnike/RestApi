from studata.models import STUDENT
from studata.serializers import StudentSerializer
from rest_framework.parsers import JSONParser 
from rest_framework.renderers import JSONRenderer
import io
import json


def run():
    # Serialization
    obj=STUDENT.objects.all()
    choice= str(input('enter your choice s/d-:'))
    if choice == "s":
        serialized_data= StudentSerializer(obj, many=True).data
        print(serialized_data)

    elif choice == "d" :
        # Desirialization
        serialized_data= StudentSerializer(obj, many=True).data
        byte_data= JSONRenderer.render(serialized_data)
        # byte_data= serialized_data.encode()
        jsontonormal= io.BytesIO(byte_data)
        Normaldata = JSONParser().parse(jsontonormal)
        print(Normaldata)
    else:
        print("!!! Invalid Choice !!!")



    