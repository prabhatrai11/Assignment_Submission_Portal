from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Assignment
from .serializers import UserSerializer, AssignmentSerializer

@api_view(['POST'])
def register_admin(request):
    request.data['is_admin'] = True
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_admin(request):
    username = request.data.get('username')
    password = request.data.get('password')
    admin = User.objects.filter(username=username, password=password, is_admin=True).first()
    if admin:
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def view_assignments(request, admin_id):
    assignments = Assignment.objects.filter(admin_id=admin_id)
    serializer = AssignmentSerializer(assignments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def accept_assignment(request, id):
    assignment = Assignment.objects.get(id=id)
    assignment.status = 'accepted'
    assignment.save()
    return Response({'message': 'Assignment accepted'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def reject_assignment(request, id):
    assignment = Assignment.objects.get(id=id)
    assignment.status = 'rejected'
    assignment.save()
    return Response({'message': 'Assignment rejected'}, status=status.HTTP_200_OK)

