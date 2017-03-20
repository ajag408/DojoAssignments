from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count
from . import team_maker

def index(request):
	# baseball = League.objects.filter(sport="Baseball")
 #  	print(baseball)
	# context = {
	# 	"leagues": baseball,
	# }


	# leagues = League.objects.filter(name__contains="women")
	# print("QUERY RESULT:", leagues)
	# context = {
	# 	"leagues": leagues
	# }

	# hockey = League.objects.filter(name__contains='hockey')
	# context = {
	# 	"leagues": hockey
	# }

	# not_football = League.objects.exclude(name__contains="football")
 #  	context = {
	# 	'leagues': not_football
	# }

	# conference = League.objects.filter(name__contains='conference')
	# context={
	# 	'leagues': conference
	# }

	# atlantic = League.objects.filter(name__contains='atlantic')
	# context = {
	# 	'leagues': atlantic
	# }

	# dallas = Team.objects.filter(location = 'Dallas')
	# print(dallas)
	# context = {
	# 	'teams': dallas
	# }

	# raptors = Team.objects.filter(team_name = 'Raptors')
	# context={
	# 	'teams': raptors
	# }

	# city = Team.objects.filter(location__contains = 'City')
	# context={
	# 	'teams': city
	# }

	# t_start = Team.objects.filter(team_name__startswith='T')
	# context={
	# 	'teams': t_start
	# }

	# location = Team.objects.all()
	# context ={
	# 	'teams': location
	# }

	# name_reverse = Team.objects.all()
	# context ={
	# 	'teams': name_reverse
	# }

	# cooper = Player.objects.filter(last_name = 'Cooper')
	# context = {
	# 	'players': cooper
	# }

	# joshua = Player.objects.filter(first_name = 'Joshua')
	# context = {
	# 	'players': joshua
	# }

	# exclude = Player.objects.filter(last_name='Cooper').exclude(first_name='Joshua')
	# context={
	# 	'players': exclude
	# }


	# name_or = Player.objects.filter(first_name = 'Alexander')|Player.objects.filter(first_name = 'Wyatt')
	# context={
	# 	'players': name_or
	# }

	# asc = Team.objects.filter(league__name = 'Atlantic Soccer Conference')
	# context ={
	# 	'teams': asc
	# }

	# pcp = Player.objects.filter(curr_team__team_name = 'Penguins')
	# context = {
	# 	'players': pcp
	# }

	# players = Player.objects.filter(curr_team__league__name = 'International Collegiate Baseball Conference')
	# context = {
	# 	'players': players
	# }

	# lo = Player.objects.filter(last_name = 'Lopez', curr_team__league__name = 'American Conference of Amateur Football')
	# context = {
	# 	'players': lo
	# }

	# footballers = Player.objects.filter(all_teams__league__sport = 'Football').distinct()
	# context = {
	# 	'players': footballers
	# }

	# sophia_team = Team.objects.filter(curr_players__first_name = 'Sophia')
	# context = {
	# 	'teams': sophia_team
	# }

	# sophia_league = League.objects.filter(teams__curr_players__first_name = 'Sophia')
	# context={
	# 	'leagues': sophia_league
	# }

	# flo = Player.objects.filter(last_name = 'Flores').exclude(curr_team__location = "Washington", curr_team__team_name = "Roughriders")
	# context = {
	# 	'players': flo
	# }

	# same = Team.objects.filter(all_players__first_name = "Samuel", all_players__last_name = "Evans")
	# context = {
	# 	'teams': same
	# }

	# mtc = Player.objects.filter(all_teams__location = 'Manitoba', all_teams__team_name = 'Tiger-Cats')
	# context = {
	# 	'players': mtc
	# }

	# exes = Player.objects.filter(all_teams__location = 'Wichita').exclude(curr_team__team_name = 'Vikings')
	# context = {
	# 	'players': exes
	# }

	# jg = Team.objects.filter(all_players__first_name = "Jacob", all_players__last_name = "Gray").exclude(curr_players__first_name = 'Jacob', curr_players__last_name = 'Gray')
	# context = {
	# 	'teams': jg
	# }

	# joshua = Player.objects.filter(first_name = 'Joshua', all_teams__league__name = 'Atlantic Federation of Amateur Baseball Players')
	# context = {
	# 	'players': joshua
	# }

	# twelve_up = Team.objects.filter(all_players__gte = 12).distinct()
	# context = {
	# 	'teams': twelve_up
	# }

	final = Player.objects.all().annotate(num_teams = Count('all_teams')).order_by('-num_teams')
	context = {
		'players': final
	}


	# context = {
	# 	"leagues": League.objects.all(),
	# 	"teams": Team.objects.all(),
	# 	"players": Player.objects.all(),
	# }
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
