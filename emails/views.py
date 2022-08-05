from bson.json_util import loads, dumps
from django.shortcuts import render
import traceback
from datetime import datetime
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
import pandas as pd

from core import secrets
from utils import mongo

from utils.responses import ok, created, bad_request, unauthorized, internal_server_error, conflict
from users.models import User
from emails.serializers import SendRequestSerializer
import os.path


# Create your views here.
@api_view(['POST'])
@permission_classes((AllowAny,))
def send(request):
    try:
        print(request.data)
        data = {"email": request.data['email'], "password": request.data['password'], "limit": request.data['limit']}
        sendEmail = SendRequestSerializer(data=data)
        if not sendEmail.is_valid():
            return bad_request(data=sendEmail.errors, message='Failed to delete host from whitelist')
        user_data = sendEmail.validated_data

        added_at = datetime.utcnow()
        user_data['added_at'] = added_at

        file = request.FILES['file']
        df = pd.read_csv(file)
        email_reciever = df.to_dict()
        mails_data = [i for i in email_reciever['email'].values()]
        d1 = [{str('email'): b} for n, b in enumerate(email_reciever['email'].values(), start=1)]
        # d2= {ip for n, ip in enumerate(d1, 1)}
        print(d1)
        user_data['receiver'] = mails_data
        mongo_collection = mongo.get_collection(db=secrets.MONGO_DB_01, col=secrets.MONGO_COL_01_A)
        mongo_collection.insert_one(dict(user_data))
        mongo_collection_reciver = mongo.get_collection(db=secrets.MONGO_DB_01, col=secrets.MONGO_COL_01_B)
        mongo_collection_reciver.insert_many(d1)

        return created(data=mails_data, message='Schedule')

    except Exception as err:
        if err.code == 65:
            return conflict(message='Emails alraedy exist')
        else:
            return internal_server_error(message='Failed to add email')