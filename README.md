ScienceFrontend
===============

Overview
--------

**ScienceFrontend** is a web app that provides an easy-to-use front end system for scientific scripts. It is currently under construction. Check out the progress [here](https://gist.github.com/eddotman/5426562). 

Usage
-----

**ScienceFrontend** is divided into encapsulated scripts which provide easy-to-use interfaces for scientific calculations. Simply browse the "Scripts" section to view all the scripts. 

Contributing
------------

To contribute to **ScienceFrontend**, please take the following steps:

1. Create a fork of the repository.
2. In `sciencefrontend/scripts/`, create your new script file, `your_script.py`.
3. Create the template for your script in `sciencefrontend/templates/` and name it `your_script.html`.
4. Create the Javascript file for your script at `sciencefrontend/static/script/js/`, and name it `your_script.js`.
5. Set up `urls.py` to include your new script. 
6. To test your script, install the Heroku toolbelt and run locally with `foreman start`. You'll need a Postgres database set up too.
7. Manually enter the URL for your script. This will make an entry in the database; from then on, you can access your script via the "scripts" page.
8. Once everything is working, make a pull request.

I would recommend first making sure that the fork is working "as-is" on your local setup before modifying the code. Tweet at [@eddotman](http://twitter.com/eddotman) if these instructions were unclear or if further help is needed.

Technologies
------------

Some of the technologies that are used by ScienceFrontend include:

+ Twitter Bootstrap
+ Gunicorn
+ Django
+ Postgres
+ Heroku
+ Amazon EC2
+ JQuery

Credits
-------

Development of **ScienceFrontend** is maintained by [Edward Kim](http://edwardkim.name). Financial support for development has been provided by the [Canadian Light Source](http://lightsource.ca).
