from rest_framework import serializers
from battle.models import *


class BattleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Battle
        fields = ['id', 'name', 'tag1', 'tag2', 'num_typo1', 'num_typo2', 'avg_length1', 'avg_length2', 'frequency1', 'frequency2', 'start_time', 'end_time', 'status']
        read_only_fields = ('num_typo1', 'num_typo2', 'avg_length1', 'avg_length2', 'frequency1', 'frequency2', 'status')

