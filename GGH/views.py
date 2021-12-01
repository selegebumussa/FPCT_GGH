import GGH
from django.shortcuts import render
from .forms import MembershipForm
from .models import Post

# Create your views here.
def base(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'GGH/about.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def injili_umisheni(request):
    return render(request, 'GGH/injili_umisheni.html')
    
def watoto_vijana(request):
    return render(request, 'GGH/watoto_vijana.html')

def sifa_mziki(request):
    return render(request, 'GGH/sifa_mziki.html')
    
def tehama(request):
    return render(request, 'GGH/tehama.html')

def theolojia(request):
        return render(request, 'GGH/theolojia.html')

def wanawake(request):
        return render(request, 'GGH/wanawake.html')

def wanaume(request):
        return render(request, 'GGH/wanaume.html')

def blog(request):
    posts = Post.objects.all()
    return render(request, 'GGH/blog.html', {'posts': posts})

def misheni(request):
    return render(request, 'GGH/misheni.html')

def tunachoamini(request):
    return render(request, 'GGH/tunachoamini.html')

def maadili(request):
    return render(request, 'GGH/maadili.html')

def contact(request):
    return render(request, 'GGH/contact.html')

def membership(request):
    membership_form = MembershipForm()
    return render(request, GGH/membership.html, {'membership_form':form})



    