# Deaf Grandpa

##### Description

* Welcome to your first attempt at web development. Say hi to your deaf old Grandpa! 
* Well, don't say *'hi'*. Say *'HI GRANDPA'*. He can't hear so well.
* You have been provided with some starter code. 
* If you enter your phrase in lower case your Grandpa will respond with *'What, I can't hear you Sonny!*
* If you enter your phrase in upper case, he should repeat what you said and then insult you with something funny.
* Make sure to run your server and test your code in action
	* `python3 manage.py runserver`
	* 127.0.0.1:8000

##### Objectives

***The Main Page***

* Your starter code has a form built out for you
* You will need to extend it so grandpa will say something back
* Remember there are three parts to this page
	* `views.py` can take a request, store values, and pass values to a template, and respond with a template
	* `templates` are the html file that you will render for the end user. They can be found in `deafgrandpa/templates/deafgrandpa/*.html`
	* `url dispatch` - This is where the routing is done - it receives requests and tries to match the urls using regex. Take a look at `deafgrandpa/urls.py`

***The Form Submission***

* Remember forms have two attributes
	* Action - You'll see an action in the form that leads to `/say`
	* Method can be GET or POST- Remember what each one does? You'll need POST for this assignment
* Since the form already has an action and method completed we will have to post data to `/say`
* Create a route in urls.py that will go to `/say` and create a corresponding function in the `views.py`
* DO NOT forget all view functions take a request as an argument
* You will find the data the user sent in a dictionary stored at `request.POST`.
* We don't want to render on a POST route
* Instead we can redirect to a route with GET (We did not cover redirect in class, you will have to research this)
	* POST should only be sending data to the server
	* GET is used to retrieve information
	* [Read more about GET and POST at w3schools](http://www.w3schools.com/tags/ref_httpmethods.asp).
* Redirect may look something like

```
return redirect('/?grandpasays=I can't hear you Sonny!')
```

***FINAL STEP***

* Figure out how to get the contents of this query string and pass it into the rendered template. You will find resources on render and redirect below. The Django documentation is less accessible than we would all like, so read carefully.

#### Resources

[Django URL Dispatcher](https://docs.djangoproject.com/en/stable/topics/http/urls/)  
[Writing Views](https://docs.djangoproject.com/en/stable/topics/http/views/)  
[Django Forms API](https://docs.djangoproject.com/en/stable/ref/forms/api/)  
[Render and Redirect](https://docs.djangoproject.com/en/stable/topics/http/shortcuts/)
