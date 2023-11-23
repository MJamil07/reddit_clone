
from rest_framework import serializers
from history.models import History


class HistorySerialzier(serializers.ModelSerializer):
      class Meta:
            model = History
            fields = '__all__'
