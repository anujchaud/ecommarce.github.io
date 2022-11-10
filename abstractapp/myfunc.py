def cart1(request):
    request.session["user"]='hello'
    print(request.session['user'])