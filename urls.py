from django.urls import path
from . import views
 
urlpatterns = [
    #index path
    path("", views.index, name="index"),
    #for users and or applicants
    path("user_login/", views.user_login, name="user_login"),
    path("signup/", views.signup, name="signup"),
    path("user_homepage/", views.user_homepage, name="user_homepage"),
    path("logout/", views.Logout, name="logout"),
    path("all_jobs/", views.all_jobs, name="all_jobs"),
    path("job_detail/<int:myid>/", views.job_detail, name="job_detail"),
    path("job_apply/<int:myid>/", views.job_apply, name="job_apply"),]