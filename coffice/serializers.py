from .models import Spot, Comment

from rest_framework import serializers


class SpotsDatatableSerializer(serializers.ModelSerializer):
    google_map_link = serializers.SerializerMethodField('get_full_position')

    def get_full_position(self, obj):
        return 'http://maps.google.com/?q={},{}'.format(obj.latitude, obj.longitude)

    class Meta:
        model = Spot
        fields = ('id', 'city', 'name', 'download_speed', 'price_indication', 'commit_user_name', 'commit_message', 'google_map_link')


class CitySpotsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spot
        fields = ('id', 'city', 'name', 'commit_user_name', 'commit_message')


class SpotsSerializer(serializers.ModelSerializer):
    commit_date = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = Spot
        fields = ('id', 'city', 'name', 'longitude', 'latitude', 'download_speed', 'upload_speed',
          'price_indication', 'bathroom', 'commit_user', 'commit_user_name', 'commit_message', 'commit_date')


class CommentSerializer(serializers.ModelSerializer):
    comment_date = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = Comment
        fields = ('id', 'comment_message', 'comment_user_name', 'comment_user_avatarurl', 'comment_date', 'spot_id', 'comment_user_id', 'comment_mark')
