from battle.models import Battle
from battle.serializers import BattleSerializer
from rest_framework import generics, viewsets
from rest_framework import permissions
from rest_framework.decorators import detail_route


class BattleViewSet(viewsets.ModelViewSet):
    """
    Creates / Returns Battle's details in JSON format.\n
    Allowd methods: get, post, head, delete

    Accepts the following POST parameters:\n
        Required: name, hash tag1, hash tag2, start time, end time\n
    Returns the created battle or battle list.    

    You can get the battle result comparing matching fields like num_typo1 and num_typo2 for criteria of number of typos, avg_length1 and avg_length2 for criteria of longer tweets, frequency1 and frequency2 for criteria of more frequent tweets.
    """
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    http_method_names = ['get', 'post', 'head', 'delete']

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
