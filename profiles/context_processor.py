def user_theme(request):
    theme = 'default.css'
    if request.user.is_authenticated():
        theme = request.user.profile.theme + '.css'
    return dict(AOR_THEME=theme)
