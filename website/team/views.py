from django.shortcuts import render

def team(requests):
    return render(requests,'team/team_page.html')