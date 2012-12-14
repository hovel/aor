import HTMLParser
from datetime import datetime
import re
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django_phpBB3.models import (User as phpbb3User, Forum as phpbb3Forum,
                                  Topic as phpbb3Topic, Post as phpbb3Post)
from django_phpBB3.utils import phpbb_html2bbcode
from pybb.models import Category, Forum, Topic, Post
from pytils.translit import slugify


class Command(BaseCommand):
    help = 'Migration phpbb3 to pybbm'

    def handle(self, *args, **options):
        self.migrate_users()
        self.migrate_categories()
        self.migrate_forums()
        self.mirgate_topics()

    def migrate_users(self):
        for user in phpbb3User.objects.iterator():
            new_user, created = User.objects.get_or_create(username=slugify(user.username_clean)[:20])
            if created:
                new_user.email = user.email
            new_user.set_unusable_password()
            new_user.save()
#                Profile.objects.create(user=new_user)

    def migrate_categories(self):
        for forum in phpbb3Forum.objects.filter(parent=0):
            Category.objects.create(name=forum.forum_name)

    def migrate_forums(self):
        for forum in phpbb3Forum.objects.exclude(parent=0):
            category = Category.objects.get(name=forum.parent)
            Forum.objects.create(category=category, name=forum.forum_name,
                description=forum.forum_desc)

    def mirgate_topics(self):
#        for topic in phpbb3Topic.objects.iterator():
        for topic in phpbb3Topic.objects.all()[:300]:
            forum = Forum.objects.get(name=topic.forum.forum_name)
            try:
                user = User.objects.get(username= slugify(topic.first_poster_name))
                closed = topic.status==1 and True or False
                created = datetime.fromtimestamp(topic.time)
                updated = datetime.fromtimestamp(topic.last_post_time)
                parser = HTMLParser.HTMLParser()
                title = parser.unescape(topic.title)
                new_topic = Topic.objects.create(forum=forum, name=title, user=user)
                new_topic.created = created
                new_topic.updated = updated
                new_topic.closed = closed
                new_topic.save()
                self.migrate_posts(topic, new_topic)
            except User.DoesNotExist:
                pass

    def migrate_posts(self, topic, new_topic):
        posts = phpbb3Post.objects.filter(topic=topic)
        for post in posts:
            try:
                user = User.objects.get(username= slugify(post.poster.username_clean))
                created = datetime.fromtimestamp(post.time)
                updated = post.edit_time and datetime.fromtimestamp(post.edit_time) or None
                body = phpbb_html2bbcode(post.text)
                parser = HTMLParser.HTMLParser()
                body = parser.unescape(body)
                body = re.sub(':'+post.bbcode_uid, '', body)
#                body = clean_bbcode(post.text)
                Post.objects.create(topic=new_topic, user=user, created=created,
                    updated=updated, user_ip=post.poster_ip, body=body)
            except User.DoesNotExist:
                pass