from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from .models import Tweet
from .serializers import TweetSerializer, TweetDetailSerializer
from users.models import User


class AllTweetsView(APIView):

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return []

    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TweetDetailSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            tweet = serializer.save(user=request.user)
            return Response(
                TweetDetailSerializer(tweet, context={"request": request}).data
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )


class DetailTweetsView(APIView):

    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "DELETE"]:
            return [IsAuthenticated()]
        return []

    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        tweet = self.get_object(pk)
        serializer = TweetDetailSerializer(tweet, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        tweet = self.get_object(pk)
        serializer = TweetDetailSerializer(
            tweet,
            data=request.data,
            partial=True,
            context={"request": request},
        )
        if serializer.is_valid():
            if tweet.user == request.user:
                updated_tweet = serializer.save()
                return Response(
                    TweetDetailSerializer(
                        updated_tweet, context={"request": request}
                    ).data
                )
        return Response(
            {"detail": "You do not have permission to edit this tweet."}, status=403
        )

    def delete(self, request, pk):
        tweet = self.get_object(pk)
        if tweet.user == request.user:
            tweet.delete()
            return Response(
                {"detail": "Tweet deleted successfully."},
                status=status.HTTP_204_NO_CONTENT,
            )
        return Response(
            {"detail": "You do not have permission to edit this tweet."}, status=403
        )


class UserTweetsView(APIView):

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound("User not found")

        tweets = Tweet.objects.filter(user=user)
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
