from django.shortcuts import render, HttpResponse, redirect
from .models import User

def index(request):
    User.userManager.login("speros@codingdojo.com","Speros")
    print("Running index method, calling out to User.")
    return HttpResponse(User.userManager.login("speros@codingdojo.com","Speros"))

# # DO NOT PASS THE WHOLE REQUEST OBJECT TO THE MODEL!!!
#     print (type(user))
#     if 'error' in user:
#         pass
#     if 'theuser' in user:
#         pass
#     return HttpResponse("Done running userManager method. Check your terminal console.")

# def index(request):
#     context = {
#         'blogs': Blog.objects.all()
#     }
#     return render(request, 'third_app/index.html', context)

# def blogs(request):
#     n = Blog.objects.create(title=request.POST['title'], blog=request.POST['blog'])
#     print n.id
#     return redirect('/')

# def comments(request, id):
#     blog = Blog.objects.get(id=id)
#     Comment.objects.create(comment=request.POST['comment'], blog=blog)
#     return redirect('/')

    # print(User.objects.all())
    #   # A list of objects (or an empty list)
    # User.objects.create(first_name="mike",last_name="mike",password="1234asdf")
    #   # Creates a user object
    # print(User.objects.all())
    #   # A list of objects (or an empty list)
    # u = User.objects.get(id=1)
    # print(u.first_name)
    # u.first_name = "Joey"
    # u.save()
    # j = User.objects.get(id=1)
    # print(j.first_name)
    #   # Gets the user with an id of 1, changes name and saves to DB, then retrieves again...
    # print(User.objects.filter(first_name="mike"))
    #   # Gets the user with a first_name of 'mike' *** THIS MIGHT NEED TO BE CHANGED ***
    # users = User.objects.raw("SELECT * from third_app_user")
    #   # Uses raw SQL query to grab all users (equivalent to User.objects.all()), which we iterate through below
    # print '*****************'
    # for user in users:
    #     print user.first_name
    # return HttpResponse("ok")


# from django.shortcuts import render
# from .models import User, Post

# # def index(request):
# #     People.objects.create(first_name="me", last_name="mine")
# #     people = People.objects.all()
# #     print (people)
# #     return render(request, 'third_app/index.html') 

# Inside your app's views.py file
