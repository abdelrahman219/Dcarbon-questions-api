# views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

class QuestionListCreateView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


# class AnswerListCreateView(generics.ListCreateAPIView):
    # queryset = Answer.objects.all()
    # serializer_class = AnswerSerializer
    # permission_classes = [AllowAny]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

@api_view(['post'])
@permission_classes([IsAuthenticated])
def AnswerListCreateView( request, *args, **kwargs):
# Ensure the user is authenticated before proceeding
    # if request.user.is_authenticated:
        print(request.data)
        for answer in request.data:
            serializer = AnswerSerializer(data=answer)
            if serializer.is_valid():
                # Set the authenticated user as the answer's user
                serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # else:
        # return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)    



