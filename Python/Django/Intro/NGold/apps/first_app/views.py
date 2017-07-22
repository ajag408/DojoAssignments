from django.shortcuts import render, redirect
import random, time, datetime
# Create your views here.
def index(request):
    if 'activity' not in request.session:
        request.session['activity'] = ""
    if 'earning' not in request.session:
        request.session['earning'] = 0


    return render(request, "first_app/index.html")

def process_money(request, word):

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

    if word == 'farm':
        temp_earn = random.randrange(10, 21)
        request.session['earning']+=temp_earn
        request.session['activity'] += "Earned " +str(temp_earn)+ " golds from the farm! ("+ st + ")\n"
    elif word == 'cave':
        temp_earn = random.randrange(5, 11)
        request.session['earning']+=temp_earn
        request.session['activity'] += "Earned " +str(temp_earn)+ " golds from the cave! ("+ st +")\n"
    elif word == 'house':
        temp_earn = random.randrange(2, 6)
        request.session['earning']+=temp_earn
        request.session['activity'] += "Earned " +str(temp_earn)+ " golds from the house! ("+st+")\n"
    elif word == 'casino':
        temp_earn = random.randrange(-50, 51)
        request.session['earning']+=temp_earn
        if temp_earn<0:
            request.session['activity'] += "Lost " +str(temp_earn)+ " golds! ("+st+")\n"
        else:
            request.session['activity'] += "Earned " +str(temp_earn)+ " golds from the casino! ("+st+")\n"
    return redirect('/')
