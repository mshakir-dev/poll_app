### Poll | Voting App

```
Complete OverView How to Create a Poll and Voting App 
```
First Create a project in your Desire location and then create a <b> Virtual Environment </b>. Virtual environment is a very important feature in python which allow to install the packages completely isolated from other packages. Also it will not install in globally if we have virtual environment setup.

``` How to create a Virtual Environment
Commmand: python -m venv venv 
```

```
Activate the Environment
# Commmand: In windows, we need to run the activate.bat file which is inside the Scripts Folder 
```

```
How to create a Project
# Commmand: django-admin startproject mspollingproject 
```

```
How to create a app
# Command: Now since the project has been created we can use the command manage.py
# Command: python manage.py startapp
```

```
Once the models definintion has been created. Django will require a command which we will or create a migration sort of ready to push it in the admin panel
# Commmand: python manage.py makemigrations
```

```
Migrate the tables and newly created models
# Commmand: python manage.py migrate
```

```
Create a super User
# Commmand: python manage.py createsuperuser 
```

```
Update Admin File in order to show the changes in the Admin Side
```

``` 
Add templates folder inside the main project folder and reference it in the Settings.py file
```

``` 
For each app we have to add the configuration in the settings.py file otherwise it will not work
```

Urls.py File is where we add the route where each functionality needs to go based on the functions which is created in views.py

