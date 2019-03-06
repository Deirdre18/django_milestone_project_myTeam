from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Avg
from .models import UserProfileData, AttributeRating
from groups.models import Group
from .forms import EditProfileForm, EditProfileDOB, EditPositionPref, RatePlayerForm
import json
import datetime

def noAccessToOtherProfiles(request, yourID, requestedID):
    if int(yourID) == int(requestedID):
        return True

def age(bday, d=None):
    if d is None:
        d = datetime.date.today()
    return (d.year - bday.year) - int((d.month, d.day) < (bday.month, bday.day))     

def arePlayersInSameGroup(player,group,user):
    if str(player) in str(group) and str(user) in str(group):
        return True

# Create your views here.
@login_required
def user_profile(request, id):
    """ Users profile page """
    
    # Security check - ensure user is accessing their own logged in profile...
    
    if noAccessToOtherProfiles(request, request.user.pk, id):
        users_profile_data = get_object_or_404(UserProfileData, pk=id)
        
        # If so, collect and aggregate their data to feed back averages...
        
        users_rated_attributes = AttributeRating.objects.filter(
            player_rated=users_profile_data).aggregate(
                avg_gk=Avg('gk_score'), avg_def=Avg('def_score'), avg_move=Avg('movement_score'),
                avg_pass=Avg('passing_score'), avg_fin=Avg('finishing_score')
            )
        
        # Calculate the number of ratings...
        
        len_votes = len(AttributeRating.objects.filter(player_rated=users_profile_data))
        
        total_outfield_scores = 0
        
        if users_rated_attributes["avg_gk"] == None:
            avg_outfield_score = "n / a"
        else:
            for key,value in users_rated_attributes.items():
                if key != "avg_gk":
                    total_outfield_scores += value
        
            avg_outfield_score = total_outfield_scores / (len(users_rated_attributes) - 1 )

        return render(request, 'profile.html', { "profile": users_profile_data, "attributes" : users_rated_attributes, "avg_outfield" : avg_outfield_score, "votes":len_votes })
    else:
        messages.error(request, "We're sorry, you cannot access this page, it's not yours!")
        return redirect(reverse('index'))
    
@login_required
def update_profile_data(request, id):
    
    profile = get_object_or_404(UserProfileData, pk=id)
    
    if request.method == "POST":
        if request.user.pk == id:
            if len(request.POST) > 1:
                form = EditProfileForm(request.POST, instance=profile)
            else:
                form = EditProfileDOB(request.POST, instance=profile)
        
            response_data = {}
            
            if form.is_valid():
                form.save()
                
                response_data['result'] = 'Update successful!'
                
                
                return HttpResponse(json.dumps(response_data),content_type="application/json")
            else:
                print(form.errors)
                return HttpResponse(json.dumps({"ERROR":"Error in updating profile"}), content_type="application/json")
        else:
             return HttpResponse(json.dumps({"ERROR":"Error in updating profile - unauth user"}), content_type="application/json")
    else:
        return redirect(reverse('index'))
        
@login_required
def update_position_pref(request, id):
    profile = get_object_or_404(UserProfileData, pk=id)
    
    if request.method == "POST":
        new_data = {}
        
        new_data["gk_pref"] = profile.gk_pref
        new_data["def_pref"] = profile.def_pref
        new_data["mid_pref"] = profile.mid_pref
        new_data["att_pref"] = profile.att_pref
        
        for key, value in request.POST.items():
            new_data[key] = value
        
        form = EditPositionPref(new_data, instance=profile)
        
        response_data = {}
        
        if form.is_valid():
            form.save()
            
            response_data['result'] = 'Update successful!'
            
            
            return HttpResponse(json.dumps(response_data),content_type="application/json")
        else:
            print(form.errors)
            return HttpResponse(json.dumps({"ERROR":"Error in updating profile"}), content_type="application/json")
    else:
        return redirect(reverse('index'))

@login_required        
def player_profile(request, playerid, groupid):
    
    # Check that the group and player exist...
    
    try:
        common_group = Group.objects.get(pk=groupid)
        player = UserProfileData.objects.get(pk=playerid)
    
        # IF YES... Security check - are the user and the selected player in the same group?
        
        if arePlayersInSameGroup(player.email, common_group.users.all(), request.user.email):
            
            #  If so, the page can be view and ratings can occur...
            
            try:
                my_age = age(player.date_of_birth)
            except:
                my_age = "Not provided"
            
            # This will help prevent a player rating themselves if the are on their own player_profile page
            
            if int(request.user.pk) == int(playerid):
                my_profile_page = True
            else:
                my_profile_page = False
            
            # Retrieve any existing ratings data
            
            try:
                this_rating_instance = AttributeRating.objects.get(rated_by=request.user.pk, player_rated=playerid)
            except:
                this_rating_instance = None
            
            return render(request, 'player-profile.html', { "player" : player, "age" : my_age, "my_profile" : my_profile_page, "groupid" : groupid, "ratings": this_rating_instance })
        else:
            messages.error(request, "Sorry but you are not linked to this player and cannot view their profile")
            return redirect(reverse('group-select'))
            
    except:
        messages.error(request, "Sorry but we can't find what you are looking for!")
        return redirect(reverse('group-select'))

@login_required        
def rate_player_or_edit_existing(request, player_rated):
    
    if request.method == "POST":
        this_user = UserProfileData.objects.get(username=request.user.username)
    
        # Determine whether there is an exisiting record to update or if a new one needs to be made...
        
        try:
            this_rating_instance = AttributeRating.objects.get(rated_by=this_user, player_rated=player_rated)
        except:
            this_rating_instance = None
        
        
        # Prepare data to be added to the database
        
        rating_data = {}
        
        for key, value in request.POST.items():
            rating_data[key] = value
            
        
        rating_data["player_rated"] = player_rated
        rating_data["rated_by"] = this_user
        
        ratings_form = RatePlayerForm(rating_data, instance=this_rating_instance)
        
        if ratings_form.is_valid():
            this_rating_instance = ratings_form.save()
            
            response_data = {}
            response_data['result'] = 'Update successful!'
            
            
            return HttpResponse(json.dumps(response_data),content_type="application/json")
        else:
            print(ratings_form.errors)
            return HttpResponse(json.dumps({"ERROR":"Error in updating ratings"}), content_type="application/json")
        
    else:
        messages.error(request, "You can't do that here")
        return redirect(reverse('group-select'))    
    