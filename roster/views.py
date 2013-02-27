# Create your views here.

from roster.models import Teams, TeamRoster, Player
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
   
    return render(request, "roster/home.html")
def teamList(request): #list of all sports teams
    team_list = TeamRoster.objects.all()
    paginator = Paginator(team_list, 25) #1st is what to pass in and 2nd is how many to show
    page = request.GET.get('page')
    try:
        teams = paginator.page(page)
    except PageNotAnInteger:
        #If page is not an integer, deliver first page.
        teams = paginator.page(1)
    except EmptyPage:
        #If page is out of range (eg. 9999), deliver last page of results.
        teams = paginator.page(paginator.num_pages)
    return render(request, "roster/team_list.html", {'teams': teams})
#use above as example for the following when I work on this again
def teamRoster(request): #shows list of players
    player_list = Players.objects.all()
    paginator = Paginator(student_list, 25) #1st is what to pass in and 2nd is how many to show
    page = request.GET.get('page')
    players = get_object_or_404(Player, id=pk)
    return render(request, "roster/teamRoster.html", {'players': players})

def players(request, pk): #shows player bio
    #course = Course.objects.order_by('?')[0]
    #name = request.GET['name']
    #try:
     #   student = Student.objects.filter(name__istartswith=name)[0]
    #except:
     #   return render(request, "roster/student.html", {'student': Student(), 'error_message': 'No student exists with the name ' + name})
    #else: 
     #   return render(request, "roster/student.html", {'student': student})
    players = get_object_or_404(TeamMember, id=pk)
    return render(request, "roster/players.html", {'players': players})
