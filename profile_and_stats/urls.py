from django.conf.urls import url, include
from .views import user_profile, update_profile_data, update_position_pref, player_profile, rate_player_or_edit_existing, add_new_image

urlpatterns = [
    url(r'^user_profile/(?P<id>\d+)$', user_profile, name="profile"),
    url(r'^update_profile_data/(?P<id>\d+)$', update_profile_data, name="update_profile"),
    url(r'^add_new_image/(?P<id>\d+)$', add_new_image, name="add_new_image"),
    url(r'^update_position_pref/(?P<id>\d+)$', update_position_pref, name="update_position_pref"),
    url(r'^player_profile/(?P<playerid>\d+)/(?P<groupid>\d+)$', player_profile, name="player-profile"),
    url(r'^rate_player/(?P<player_rated>\d+)$', rate_player_or_edit_existing, name="rate-player"),
]