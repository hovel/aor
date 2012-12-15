from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.utils.translation import ugettext_lazy as _
from news.models import News


class AuthorListFilter(SimpleListFilter):
    title = _('authors')
    parameter_name = 'author'

    def lookups(self, request, model_admin):
#        authors = map(lambda x: (x,x), News.objects.all().values_list('user').distinct())
        authors = dict(News.objects.values_list('user__pk', 'user__username')).items()
        return authors

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(user=self.value())
        return queryset



class NewsAdmin(admin.ModelAdmin):
    list_display =('title', 'user', 'source', 'created', 'changed')
    date_hierarchy = 'created'
    search_fields = ('title', 'text', 'source')
    list_filter = (AuthorListFilter,)
    readonly_fields = ('text_html',)

admin.site.register(News, NewsAdmin)
