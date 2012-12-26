def user_theme(request):
    AOR_THEME = 'default.less'
    if request.user.is_authenticated():
        AOR_THEME = request.user.get_profile().theme + '.less'
    return dict(AOR_THEME=AOR_THEME)
