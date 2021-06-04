
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from app.tasks import do_work


class TaskApiView(APIView):
    permission_classes = [AllowAny]

    def get( self,request,*args,**kwargs ):
        res = do_work.delay("hello")
        print(res)
        response = {
            "message" : "success"
        }
        return Response(response,status=status.HTTP_200_OK)