from django.contrib import admin
from pybb.admin import TopicReadTrackerAdmin, ForumReadTrackerAdmin
from pybb.models import ForumReadTracker, TopicReadTracker

admin.site.register(TopicReadTracker, TopicReadTrackerAdmin)
admin.site.register(ForumReadTracker, ForumReadTrackerAdmin)