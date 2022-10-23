
from dataclasses import field
from rest_framework import serializers
import django.contrib.auth.models as modelMain
import models as ModelSub
class Meta:
    field = ["first_name","last_name","password","email","phoneNumber","id"]
    git 