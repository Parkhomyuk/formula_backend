from rest_framework import serializers
from games.models import Game, GameCategory, Player, PlayerScore
import games.views

class GameSerializer(serializers.HyperlinkedModelSerializer):
    game_category=serializers.SlugRelatedField(queryset=GameCategory.objects.all(), slug_field='name')
    class Meta:
        model = Game
        fields =('url','game_category','name','release_date', 'played')

class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='game-detail')
    class Meta:
        model = GameCategory
        fields = ('url','pk','name', 'games')


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    game=GameSerializer()
    class Meta:
        model=PlayerScore
        fields=('url', 'pk', 'score', 'score_date', 'game')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)
    gender=serializers.ChoiceField(choices=Player.GENDER_CHOICES)
    gender_description=serializers.CharField(source='ger_gender_display', read_only=True)
    class Meta:
        model= Playerfields=('url', 'name', 'gender', 'gender_description', 'score')        

class PlayerScoreSerializer(serializers.ModelSerializer):
    player = serializers.SlugRelatedField(queryset=Player.objects.all(), slug_field='name')
    class Meta:
        model = PlayerScore
        fields=('url','pk','score','score_date','player','game')        