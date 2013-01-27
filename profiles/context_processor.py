def user_theme(request):
    AOR_THEME = 'default.css'
    if request.user.is_authenticated():
        AOR_THEME = request.user.get_profile().theme + '.css'
    return dict(AOR_THEME=AOR_THEME)
