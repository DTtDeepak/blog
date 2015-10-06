# Blog

This is blog application written in django framework. 
It is currently live as [my personal blog at bansalvarun.me!](bansalvarun.me) 

Instructions for setup
------------

- Clone the project

        git clone https://github.com/bansalvarun/audioDownloader.git 
        cd blog

- Add a secret key for this application in "settings_secret.py" (create a new file) in myblog directory as:

        SECRET_KET = "YOUR KEY"

      *You can create a new django project to get a secret key or probably use one from your any other django app.

- Install the project's runtime requirements

    *use of virtualenv is recommended

        pip install -r requirements.txt


- Setup Database

        python manage.py syncdb

    It will ask you to create a superuser, go  head make one.

        python manage.py makemigrations
        python manage.py migrate

- To run the server 
    
        python manage.py runserver

- Your blog app is running at 

        localhost:8000

   Open it in any web-browser.
    
- To log into admin panel

        localhost:8000/admin
    You can use your superuser login credentials here.





Issues
------------

Please report any bugs or requests that you have using the GitHub issue tracker!


**Author is not liable for any misuse; Use carefully!
