from rest_framework import serializers
from ..models import Note


class NoteSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ('id', )

    def get_username(self, obj):
        return obj.user.username