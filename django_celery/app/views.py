
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status


class TaskApiView(APIView):
    permission_classes = [AllowAny]

    def get( self,request,*args,**kwargs ):
        response = {
            "message" : "success"
        }
        return Response(response,status=status.HTTP_200_OK)