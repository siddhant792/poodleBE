from pyasn1.type.univ import Boolean
import pyrebase
import os
import time

from django.conf import settings

import apps.documents.constants as document_constants

firebase = pyrebase.initialize_app(settings.FIREBASE_CONFIG)
storage = firebase.storage()


def current_milli_time():
    return str(round(time.time() * 1000))

def upload_document(user, title, file):
    file_extension = os.path.splitext(str(file))[1]
    path_on_cloud = document_constants.UPLOAD_PATH + str(user) + "/" + title + "-" + current_milli_time() + file_extension
    bucket_token = storage.child(path_on_cloud).put(file)['downloadTokens']
    return storage.child(path_on_cloud).get_url(bucket_token)