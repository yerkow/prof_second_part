from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import ProfView, ProfCollegianBodiesView, VizitView, VacationView, AwardsView, SocialPartnershipView, ProfMemberView, ReportView

router = DefaultRouter()
router.register('prof-view', ProfView, basename = 'prof-view')
router.register('prof-member-view', ProfMemberView, basename = 'prof-member-view')
router.register('prof-collegian-bodies-view', ProfCollegianBodiesView, basename = 'prof-collegian-bodies-view')
router.register('vizit-view', VizitView, basename = 'vizit-view')
router.register('vacation-view', VacationView, basename = 'vacation-view')
router.register('report-view', ReportView, basename = 'report-view')
router.register('awards-view', AwardsView, basename = 'awards-view')
router.register('social-partnership-view', SocialPartnershipView, basename = 'social-partnership-view')

urlpatterns = [
    path('token/', obtain_auth_token, name='obtain_token'),
    path('', include(router.urls))
]
