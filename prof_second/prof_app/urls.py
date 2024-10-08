from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import ProfView, ProfCollegianBodiesView, VizitView, VacationView, AwardsView, SocialPartnershipView, ProfMemberView, ReportView

router = DefaultRouter()
router.register('prof-view', ProfView, name = 'prof-view')
router.register('prof-member-view', ProfMemberView, name = 'prof-member-view')
router.register('prof-collegian-bodies-view', ProfCollegianBodiesView, name = 'prof-collegian-bodies-view')
router.register('vizit-view', VizitView, name = 'vizit-view')
router.register('vacation-view', VacationView, name = 'vacation-view')
router.register('report-view', ReportView, name = 'report-view')
router.register('awards-view', AwardsView, name = 'awards-view')
router.register('social-partnership-view', SocialPartnershipView, name = 'social-partnership-view')

urlpatterns = [
    path('token/', obtain_auth_token, name='obtain_token'),
    path('', include(router.urls))
]