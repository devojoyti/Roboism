![Build Status](https://travis-ci.com/markroxor/Roboism.svg?token=FzX7CPA4K1qbQP1HdyLt&branch=master)


## RoboISM - Running at [roboism.markroxor.in](roboism.markroxor.in)

RoboISM is the official site of Robotics Club ISM Dhanbad. Well right now it is ![alt tag](https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQpNgHwfZ40zcRFx2AJ-17aoqeQF9xR53Ho-dPXPh7mku_uaETCjg)


####For Newbies: How to run code locally ?
* Clone your code into your PC. Let the folder name be Roboism. 
* Install python 3 in your PC. Preferably in default directory (C:/).
* delete Roboism/myvenv folder if it exists.
* Open Command Prompt/Terminal and cd into the directory (Roboism). <br>
  For Window Users:-
  ```C:\Python34\python -m venv myvenv```<br>
  For Linux Users and OS X Users:-
  ```python3 -m venv myvenv```<br>

* Then do <br>
  For Window Users:- ```myvenv\Scripts\activate```<br>
  For Linux Users and OS X Users:-
  ```source myvenv/bin/activate``` <br>
  Now, you should see a (myvenv) script before cmd commands. <br>
  
* Next, check updates (if any) for pip module by
  ```pip install --upgrade pip```

* After that, do
  ```pip install django```
  
* Next, do 
  ```pip install django_extensions```
  
* After that, do
  ```pip install Pillow```

* After installation is complete, do
  ```python manage.py makemigrations```
  And 
  ```python manage.py migrate```
  And
  ```python manage.py collectstatic```

* Finally, to run a virtual server, do
  ```python manage.py runserver```
  Go to any browser, type this url '127.0.0.1:8000' without quotes. If everything went as planned, you will see the site       locally. <br>
  
* For accessing/modifying users and other data, do 
  ```python manage.py createsuperuser``` and input onscreen details to create a superuser account followed by opening           '127.0.0.1:8000/admin/' in a browser window without quotes and logging in with the newly made superuser.
  
* Make any changes to the code and see the change reflected on the locally hosted site. 


