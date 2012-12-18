import HTMLParser
from datetime import datetime
from django.contrib.comments import Comment
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.db.models import Q
import re
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from django_phpBB3.models import (User as phpbb3User, Forum as phpbb3Forum,
                                  Topic as phpbb3Topic, Post as phpbb3Post)
from django_phpBB3.utils import phpbb_html2bbcode
from pybb.models import Category, Forum, Topic, Post
from pytils.translit import slugify
from drupango.models import (Node as DrupalNode, Comments as DrupalComments, )
from html2bbcode import HTML2BBCode


class Command(BaseCommand):
    help = 'Migration phpbb3 to pybbm'

    def handle(self, *args, **options):
    #        self.migrate_users()
    #        self.migrate_categories()
    #        self.migrate_forums()
    #        self.mirgate_topics()
#        self.migrate_news()
        self.migrate_blogs()

    def migrate_users(self):
        for user in phpbb3User.objects.iterator():
            new_user, created = User.objects.get_or_create(
                username=slugify(user.username_clean)[:20])
            if created:
                new_user.email = user.email
            new_user.set_unusable_password()
            new_user.date_joined = user.registration_datetime()
            new_user.last_login = user.lastvisit_datetime()
            new_user.save()

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
                user = User.objects.get(
                    username=slugify(topic.first_poster_name))
                closed = topic.status == 1 and True or False
                created = datetime.fromtimestamp(topic.time)
                updated = datetime.fromtimestamp(topic.last_post_time)
                parser = HTMLParser.HTMLParser()
                title = parser.unescape(topic.title)
                new_topic = Topic.objects.create(forum=forum, name=title,
                    user=user)
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
                user = User.objects.get(
                    username=slugify(post.poster.username_clean))
                created = datetime.fromtimestamp(post.time)
                updated = post.edit_time and datetime.fromtimestamp(
                    post.edit_time) or None
                body = phpbb_html2bbcode(post.text)
                parser = HTMLParser.HTMLParser()
                body = parser.unescape(body)
                body = re.sub(':' + post.bbcode_uid, '', body)
                #                body = clean_bbcode(post.text)
                Post.objects.create(topic=new_topic, user=user,
                    created=created,
                    updated=updated, user_ip=post.poster_ip, body=body)
            except User.DoesNotExist:
                pass

    def migrate_news(self):
        print "Forum list:"
        for forum in Forum.objects.all():
            print "%s: %s" % (forum.pk, forum.name)
        forum = raw_input('Choice forum id or enter new forum name:')
        try:
            forum = Forum.objects.get(pk=forum)
        except:
            category = Category.objects.all()[0]
            forum = Forum.objects.create(name=forum, category=category)
        pages = DrupalNode.objects.filter(Q(type='page') | Q(type='story'))
        parser = HTML2BBCode()
        for page in pages:
            user = User.objects.get(username=slugify(page.user.name) or 'zeus')
            topic = Topic.objects.create(
                forum=forum,
                user=user,
                name=page.title,
                created=page.created_date,
                updated=page.changed_date,
            )
            Post.objects.create(
                user=user,
                topic=topic,
                body=parser.feed(page.revision.body),
                created=page.created_date,
                updated=page.changed_date,
            )
            self.migrate_comments(page, topic)

    def migrate_blogs(self):
        print "Forum list:"
        for forum in Forum.objects.all():
            print "%s: %s" % (forum.pk, forum.name)
        forum = raw_input('Choice forum id or enter new forum name:')
        try:
            forum = Forum.objects.get(pk=forum)
        except:
            category = Category.objects.all()[0]
            forum = Forum.objects.create(name=forum, category=category)
        pages = DrupalNode.objects.filter(type='blog')
        parser = HTML2BBCode()
        for page in pages:
            try:
                user = User.objects.get(username=slugify(page.user.name))
            except:
                user = User.objects.get(username='zeus')
            topic = Topic.objects.create(
                forum=forum,
                user=user,
                name=page.title,
                created=page.created_date,
                updated=page.changed_date,
            )
            Post.objects.create(
                user=user,
                topic=topic,
                body=parser.feed(page.revision.body),
                created=page.created_date,
                updated=page.changed_date,
            )
            self.migrate_comments(page, topic)

    def migrate_comments(self, node, topic):
        parser = HTML2BBCode()
        comments = DrupalComments.objects.filter(node=node)
        for comment in comments:
            try:
                user = User.objects.get(username=slugify(comment.user.name))
            except:
                user = User.objects.get(username='zeus')
            Post.objects.create(
                user=user,
                topic=topic,
                body=parser.feed(comment.comment),
                created=comment.timestamp_date,
            )
