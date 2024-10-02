from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TeamSerializer
from .models import TeamModel


# Create your views here.
class TeamViews(APIView):
    def get(self, request):
        teams = TeamModel.objects.filter(name__icontains= "")
        serializer = TeamSerializer(teams, many=True)
        return Response({"message": "Teams get request successful", "teams": serializer.data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        incoming_data = request.data
        serializer = TeamSerializer(data=incoming_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Teams post request successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        try:
            team = TeamModel.objects.get(pk=id)
        except TeamModel.DoesNotExist:
            return Response({"message": "Data not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TeamSerializer(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Teams put request successful"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            team = TeamModel.objects.get(pk=id)
        except TeamModel.DoesNotExist:
            return Response("message", "Data does not exist", status=status.HTTP_404_NOT_FOUND)
        team.delete()
        return Response({"message": "Team data deleted successfully"},status=status.HTTP_204_NO_CONTENT)
