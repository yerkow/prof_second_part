from rest_framework import serializers
from .models import ProfMember, Prof, ProfCollegianBodies, Report, Vacation, Vizit, Awards, SocialPartnershipAgreements

class ProfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prof
        fields = "__all__"

class ProfMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfMember
        fields = "__all__"

class ProfCollegianBodiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfCollegianBodies
        fields = "__all__"

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"

class VacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = "__all__"

class VizitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vizit
        fields = "__all__"

class AwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awards
        fields = "__all__"

class SocialPartnershipAgreementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialPartnershipAgreements
        fields = "__all__"