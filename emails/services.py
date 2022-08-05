import psycopg2
import pymongo
import json

from bson import json_util
from bson.json_util import dumps, loads
from psycopg2 import sql
from utils import mongo, postgres
from core import secrets, settings


def get_user_call():
    conn = mongo.get_collection(db=secrets.MONGO_DB_04, col=secrets.MONGO_COL_04_A)

    count = conn.count_documents({})
    cursor = conn.find({}, {'_id': 0, 'app_package_name': 1, 'app_name': '$app_name',
                            'app_version_name': '$app_version_name',
                            'app_version_code': '$app_version_code', 'app_source': '$app_source', 'app_uid': '$app_uid',
                            'suspicious_declared_at': '$suspicious_declared_at', 'permissions': '$permissions',
                            'app_package_version_hkey': '$app_package_version_hkey'})
    apps = loads(dumps(cursor))

    for ele in apps:
        permission = []
        for x in ele['permissions']:
            permission.append({'permission': x})
            ele['permissions'] = permission

    data = {
        'list': apps,
        'count': count
    }

    return data

