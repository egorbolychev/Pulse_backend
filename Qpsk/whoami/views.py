import random

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def whoami(request):
    """
    Shows who you are
    """
    if request.method == 'GET':
        who_list = ["sweetest", "cutest", "finest", "coolest"]

        return Response({"response": f"You're the {random.choice(who_list)} creature on earth"}, status=status.HTTP_200_OK)
