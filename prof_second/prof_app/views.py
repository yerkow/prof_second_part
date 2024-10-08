import os
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import default_storage
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import generics
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import openpyxl
from .models import Prof, ProfCollegianBodies, ProfMember, Awards, Vacation, Report, Vizit, SocialPartnershipAgreements
from .serializer import ProfCollegianBodiesSerializer, ProfMemberSerializer, ProfSerializer, AwardsSerializer, VacationSerializer, VizitSerializer, ReportSerializer, SocialPartnershipAgreementsSerializer

class ProfView(viewsets.ModelViewSet):
    queryset = Prof.objects.all()
    serializer_class = ProfSerializer
    lookup_field = "id"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["industry", "higher_union_org", "union_name", "union_type", "bin", "chairman_name"]

class ProfMemberView(viewsets.ModelViewSet):
    queryset = ProfMember.objects.all()
    serializer_class = ProfMemberSerializer
    lookup_field = "id"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name", "union_ticket_number", "gender", "birth_date", "position", "role", "education", "awards", "vacation"]

class ProfCollegianBodiesView(viewsets.ModelViewSet):
    queryset = ProfCollegianBodies.objects.all()
    serializer_class = ProfCollegianBodiesSerializer
    lookup_field = "id"

class AwardsView(viewsets.ModelViewSet):
    queryset = Awards.objects.all()
    serializer_class = AwardsSerializer
    lookup_field = "id"

class VacationView(viewsets.ModelViewSet):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer
    lookup_field = "id"

class ReportView(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    lookup_field = "id"

class VizitView(viewsets.modelViewSet):
    queryset = Vizit.objects.all()
    serializer_class = VizitSerializer
    lookup_field = "id"

class SocialPartnershipView(viewsets.ModelViewSet):
    queryset = SocialPartnershipAgreements.objects.all()
    serializer_class = SocialPartnershipAgreementsSerializer
    lookup_field = "id"

class UploadProfMembers(APIView):
    def post(self, request, *args, **kwargs):
        # Получаем prof_id из query параметра
        prof_id = request.query_params.get('prof_id')

        if not prof_id:
            return Response({'error': 'prof_id query parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Проверяем существование объекта Prof
        try:
            prof = Prof.objects.get(id=prof_id)  # Поиск объекта Prof по его id
        except Prof.DoesNotExist:
            return Response({'error': f'Prof with id {prof_id} does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        # Получаем файл из запроса
        file = request.FILES.get('file')

        if not file:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Загружаем и читаем Excel файл
            wb = openpyxl.load_workbook(file)
            sheet = wb.active

            for row in sheet.iter_rows(min_row=2, values_only=True):  # Начинаем со второй строки (с пропуском заголовков)
                photo = row[0]
                name = row[1]
                union_ticket_number = row[2]
                gender = row[3]
                birth_date = row[4]
                position = row[5]
                role = row[6]
                education = row[7]
                total_work_experience = row[8]
                org_work_experience = row[9]
                union_membership_date = row[10]
                awards = row[11]
                vacation = row[12]
                phone = row[13]
                email = row[14]

                # Создание объекта ProfMember
                ProfMember.objects.create(
                    prof_id=prof,  # Используем объект Prof из query параметра
                    photo=photo,
                    name=name,
                    union_ticket_number=union_ticket_number,
                    gender=gender,
                    birth_date=birth_date,
                    position=position,
                    role=role,
                    education=education,
                    total_work_experience=total_work_experience,
                    org_work_experience=org_work_experience,
                    union_membership_date=union_membership_date,
                    awards=awards,
                    vacation=vacation,
                    phone=phone,
                    email=email,
                )

            return Response({'message': 'Data uploaded successfully'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)