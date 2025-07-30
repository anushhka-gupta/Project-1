from django.urls import path,include
from .import views,user_views,advisor_views
urlpatterns = [
    path("",views.home,name="home"),
    path("about/",views.about_us,name="about_us"),
    path("contact/",views.contact_us,name="contact_us"),
    path("user_reg/",user_views.user_reg,name="user_reg"),
    path("user_login/",user_views.user_login,name="user_login"),
    path("user_home/",user_views.user_home,name="user_home"),
    path("user_feedback/",user_views.user_feedback,name="user_feedback"),
    path("advisor_login/",advisor_views.advisor_login,name="advisor_login"),
    path("user_logout/",user_views.user_logout,name="user_logout"),
    path("all_feedback/",views.all_feedback,name="all_feedback"),
    path("services/",views.services,name="services"),
    path("advisors/",user_views.advisors,name="advisors"),
]
