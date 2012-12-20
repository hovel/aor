def user_theme(request):
    if request.user.is_authenticated:
        AOR_THEME = request.user.get_profile().theme
    else:
        AOR_THEME = 'default'
    return dict(AOR_THEME=AOR_THEME)
