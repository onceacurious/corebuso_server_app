from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Inquiry, TestUser


class TestUserSerializer(ModelSerializer):
    test_user_count = SerializerMethodField(read_only=True)

    class Meta:
        model = TestUser
        fields = '__all__'

    def get_test_user_count(self, obj):
        count = obj.inquiry_set.count()
        return count


class InquirySerializer(ModelSerializer):
    # staff = TestUserSerializer()

    class Meta:
        model = Inquiry
        fields = '__all__'
