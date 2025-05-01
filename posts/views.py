from django.shortcuts import render, redirect, get_object_or_404
from .models import Posts
import json
from django.http import JsonResponse

def ui(request):
    username = request.session.get('username')
    posts = Posts.objects.all()
    return render(request, 'posts/post.html',{"posts":posts})

def add_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        post = request.POST.get('text')
        name = request.session.get('username')
        if title and post and name:
            Posts.objects.create(title=title,
                                 post=post,
                                 name=name)
            return redirect('post_ui')
        else:
            error = "Both title and text are required."
            posts = Posts.objects.all()
            return render(request, 'posts/post.html', {'error': error, 'posts':posts})

def get_posts(_):
    post = list(Posts.objects.values())
    return JsonResponse(post, safe=False)

def delete_posts(request, post_id):
    username = request.session.get('username')
    if not username:
        return redirect('login')
    post = get_object_or_404(Posts,id=post_id)
    if post.name == username:
        post.delete()
        return redirect('post_ui')
    else:
        error = "hop beybi"
        posts = Posts.objects.all()
        return render(request, 'posts/post.html', {'error': error,'posts':posts})

def logout(request):
    request.session.flush()
    return redirect('login')

#TODO add remember Login
#Finde way to get username once
#Find way to change obj value from view without give argument to render
#X scroll bug
# Delete edit log out and others look like its please change with button
# if user try to dlete or edit a post that not he made it, please change obj boreder color to red
# and add error message correct position, and try not give error message with render
# try change error text message from view and sav e and redirect
# dont render when click button if  not nessary
# when click to delte please ask again do you want to delete
# add a menu bar , all posts, my posts
# settings button where will be, log out, change mode light and dark, and delete account
# str function title
def edit_post(request, post_id):
    username = request.session.get('username')
    post = get_object_or_404(Posts, id=post_id)
    if post.name != username:
        error = "hop beybi"
        posts = Posts.objects.all()
        return render(request, 'posts/post.html', {'error': error,'posts':posts})
    if request.method == 'POST':
        new_title = request.POST.get('title')
        new_text = request.POST.get('text')
        if new_title and new_text:
            post.title = new_title
            post.post = new_text
            post.save()
            return redirect('post_ui')
    return render(request, 'posts/edit_post.html', {'post': post})
    


