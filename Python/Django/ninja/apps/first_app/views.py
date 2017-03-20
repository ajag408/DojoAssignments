from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def almighty(request):
    return render(request, 'first_app/all_four.html')

def solo(request, color):
    print color
    if color == 'blue':
        context= {
                'color': 'first_app/images/leo_blue.gif'
               }
    elif color == 'orange':
        context= {
                'color': 'first_app/images/michael_orange.gif'
               }
    elif color == 'red':
        context= {
                'color': 'first_app/images/raph_red.jpg'
               }
    elif color == 'purple':
        context= {
                'color': 'first_app/images/don_purp.gif'
               }
    else:
        context= {
                'color': 'first_app/images/megfox.jpg'
               }
    return render(request, 'first_app/solo.html', context)



    # 'orange': 'first_app/images/michael_orange.gif',
    #
    # 'red': 'first_app/images/raph_red.jpg',
    #
    # 'purple': 'first_app/images/don_purp.gif',
    #
    # 'blue': 'first_app/images/leo_blue.gif',
