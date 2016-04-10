from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    context = {"grandpa_says":request.GET.get("grandpa_says")}
    return render(request, 'deafgrandpa/index.html', context)


def say(request):
    if request.method == 'POST':
        value = request.POST.get("say_to_grandpa")
        context = {'grandpa_says':value}
        print (context)

        if len(context["grandpa_says"]) > 1:

            for letter in context["grandpa_says"]:
                if letter.islower() == True:
                    return redirect ("/?grandpa_says=What did you say?!")

            return redirect ("/?grandpa_says=Great to hear you!")

        else:
            return redirect ("/?grandpa_says=You didnt even say anything!")


# def index(request):
#     if request.GET.get("post"):
#         context = {
#             "post": request.GET.get("post")
#         }
#     else:
#         context = {
#             "post": "nothing here yet!"
#         }
#     return render(request, 'index.html', context)



