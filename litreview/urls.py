"""
URL configuration for litreview project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
from authentication.forms import CustomLoginForm
import authentication.views
import feed.views
import tickets.views
import follows.views
import reviews.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True,
        authentication_form=CustomLoginForm),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
         name='password_change_done'
         ),
    path('signup/', authentication.views.signup_page, name='signup'),

    path('feed/', feed.views.feed, name='feed'),
    path('self-feed/', feed.views.users_posts_feed, name='self-feed'),

    path('tickets/create/', tickets.views.create_ticket, name='create-ticket'),
    path('tickets/<int:id>/update/', tickets.views.update_ticket, name='update-ticket'),
    path('tickets/<int:ticket_id>/review/', reviews.views.create_review, name='create-review'),

    path('follow-users/', follows.views.follow_users, name='follow-users'),
    path('follow-users/<int:id>/unfollow/', follows.views.unfollow_user, name='unfollow-user'),

    path('reviews/<int:review_id>/update/', reviews.views.update_review, name='update-review'),
    path('reviews/create/', reviews.views.create_review_and_ticket, name='create-review-ticket'),

    path("select2/", include("django_select2.urls")),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
