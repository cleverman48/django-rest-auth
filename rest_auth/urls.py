from django.conf.urls import patterns, url

from rest_auth.views import (
    Login, Logout, UserDetails, PasswordChange,
    PasswordReset, PasswordResetConfirm
)

urlpatterns = patterns(
    '',
    # URLs that do not require a session or valid token
    url(r'^password/reset/$', PasswordReset.as_view(),
        name='rest_password_reset'),
    url(r'^password/reset/confirm/$', PasswordResetConfirm.as_view(),
        name='rest_password_reset_confirm'),
    url(r'^login/$', Login.as_view(), name='rest_login'),
    # URLs that require a user to be logged in with a valid session / token.
    url(r'^logout/$', Logout.as_view(), name='rest_logout'),
    url(r'^user/$', UserDetails.as_view(), name='rest_user_details'),
    url(r'^password/change/$', PasswordChange.as_view(),
        name='rest_password_change'),
)
