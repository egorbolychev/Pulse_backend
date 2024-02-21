from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def whoami(request):
    """
    Shows who you are
    """
    if request.method == 'GET':
        return Response({"response": "You're the sweetest creature on earth"}, status=status.HTTP_200_OK)
