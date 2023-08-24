from django.shortcuts import render
from .serializers import StudentSerializer,optionserializer
from rest_framework.generics import ListAPIView
from .models import Student
import json
import os
import pandas as pd
from api.models import DataFrameStorage
from djangoproj.settings import BASE_DIR

def home_view(request):
    data_f()
    return render(request,'home.html')

class StudentList(ListAPIView):
    queryset = Student.objects.all()    
    serializer_class = StudentSerializer
    
class optionList(ListAPIView):
    queryset = DataFrameStorage.objects.all()
    serializer_class = optionserializer

def data_f():
    data = pd.read_csv(os.path.join(BASE_DIR,'py_prog/data/expiry.csv'))
    df = pd.DataFrame(data)
    serialized_data = df.to_json(orient='split', indent = 4)
    # print(serialized_data)
    df_storage = DataFrameStorage(data=serialized_data)
    df_storage.save()
    # df_storage = DataFrameStorage.objects.first()
    # if df_storage:
    #     deserialized_data = json.loads(df_storage.data)
    #     df = pd.read_json(deserialized_data)
    #     # print(df)
    # return 




