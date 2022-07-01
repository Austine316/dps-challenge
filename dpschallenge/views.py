from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# import pandas as pd

from apiapp.serializers import AccidentSerializer
from apiapp.models import Accident


class AccidentVIEW(APIView):
    # def get(self, request, *args, **kwargs):
    #     data = {
    #         'username': 'admin',
    #         'years_active': 10
    #     }
    #     return Response(data)

    def post(self, request, *args, **kwargs):
        serializer = AccidentSerializer(data=request.data)

        # prediction = pd.read_csv('./prediction.csv')

        # print(prediction)

        if serializer.is_valid():
            serializer.save()
            # print(serializer)

            # year = int(serializer.data['year'])
            # month = int(serializer.data['month'])

            # cond = (prediction['year'] == year) & (
            #     prediction['month'] == month)
            # result = prediction[cond].Predictions.values[0]
            # result = {"prediction": result}

            return Response(serializer.data)

        return Response(serializer.errors)
