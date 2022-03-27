from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from apps.authotp.emails import send_otp_via_email

from apps.authotp.models import User
from apps.authotp.serializers import UserSerializer, VerifyUserSerializers


class RegisterAPI(APIView):

    def post(self, request, *args, **kwargs):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response({
                    'status': status.HTTP_200_OK,
                    'message': 'registration successful. please check your email.',
                    'data': serializer.data
                })
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'something went wrong!',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)


class VerifyOTP(APIView):

    def post(self, request):
        try:
            serializer = VerifyUserSerializers(data=request.data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                user = User.objects.filter(email=email)
                if not user.exists():
                    return Response({
                        'status': status.HTTP_400_BAD_REQUEST,
                        'message': 'something went wrong!',
                        'data': 'invalid email'
                    })
                if user[0].otp != otp:
                    return Response({
                        'status': status.HTTP_400_BAD_REQUEST,
                        'message': 'something went wrong!',
                        'data': 'invalid otp'
                    })
                user = user.first()
                user.is_verified = True
                user.save()
                return Response({
                    'status': status.HTTP_200_OK,
                    'message': 'Verified User Account',
                    'data': {}
                })
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'something went wrong!',
                'data': serializer.errors
            })
        except Exception as e:
            print(e)