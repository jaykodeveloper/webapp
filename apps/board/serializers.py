from rest_framework import serializers
from .models import Board
from django.contrib.auth.models import User

class Base64ImageField(serializers.ImageField):
    """
    based on 
    https://github.com/tomchristie/django-rest-framework/pull/1268
    """
    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        if isinstance(data, six.string_types):
            if 'data:' in data and ';base64,' in data:
                header, data = data.split(';base64,')

            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            file_name = str(uuid.uuid4())[:12]
            file_extension = self.get_file_extension(file_name, decoded_file)
            complete_file_name = "%s.%s" % (file_name, file_extension, )
            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == 'jpeg' else extension

        return extension

# class BoardSerializer(serializers.ModelSerializer):
class BoardSerializer(serializers.HyperlinkedModelSerializer):
    # this needs to have read_only attribute
    # author = serializers.PrimaryKeyRelatedField(
    #     read_only=True, default=serializers.CurrentUserDefault()
    # )
    # author = serializers.HyperlinkedRelatedField(
    #     view_name='users-detail', 
    #     lookup_field='username',
    #     read_only=True, 
    #     default=serializers.CurrentUserDefault()
    # )
    image = Base64ImageField(max_length=None, use_url=True, required=False, allow_null=True)
    author = serializers.ReadOnlyField(source='author.username')
    url = serializers.HyperlinkedIdentityField(
        view_name="board:board-detail",
        read_only=True,
        lookup_field='pk')
    class Meta:
        model = Board
        # fields = ('id', 'author', 'title', 'body', 'image', 'created','updated')
        fields = ('url','id', 'author', 'title', 'body', 'image', 'created','updated')
        view_name='board-detail'
        lookup_field='id'

