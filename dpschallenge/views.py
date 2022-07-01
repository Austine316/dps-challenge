from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# import pandas as pd
import polars as pl

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

        df = pl.read_csv('prediction.csv', has_header=True)

        # print(prediction)

        if serializer.is_valid():
            serializer.save()
            # print(serializer)

            year = int(serializer.data['year'])
            month = int(serializer.data['month'])

            cond = (df['year'] == year) & (
                df['month'] == month)
            result = df[cond].Predictions[0]
            result = {"prediction": round(result, 2)}

            return Response(result)

        return Response(serializer.errors)


# class AccidentVIEW(APIView):
#     def post(self, request, *args, **kwargs):

#         data = {
#             'year': request.data.get('year'),
#             'month': request.data.get('month'),
#         }

#         serializer = AccidentSerializer(data=data)

#         df = pl.read_csv('prediction.csv', has_header=True)

#         if serializer.is_valid():
#             serializer.save()

#             cond = (df['year'] == int(data['year'])) & (
#                 df['month'] == int(data['month']))
#             result = df[cond].Predictions[0]
#             result = {"prediction": round(result, 2)}

#             return Response(result)

#         return Response(serializer.errors)
