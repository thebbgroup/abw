Anti-Bullying Week site
=======================

This is a simple Flask webapp for the Anti-Bullying Week website.

It's mostly static content, but there is a form to sign up for a newsletter.

Getting Started
---------------

1. Clone the repo
```sh
git clone git@github.com:thebbgroup/abw
cd abw
```

2. Get Python and virtualenv set up

  On Windows, you may not have Python and you most likely don't have virtualenv,
  so first, [get Python](http://www.python.org/download/releases/2.7/).

  Next, [download easy_install](http://python-distribute.org/distribute_setup.py) to C:\ and run it with Python:
```sh
python distribute_setup.py
```

  You will probably need to add virtualenv to your path. If you are using Git Bash, you can execute the following:
```sh
export PATH=$PATH:/c/Python27/Scripts
```
  Add that line to the end of your $HOME/.bashrc file too.

  Then install virtualenv:
```sh
easy_install virtualenv
```

3. Setup the virtualenv
```sh
virtualenv venv
. venv/bin/activate
```

4. Install dependencies
```sh
pip install -r requirements.txt
```

5. Run the devserver
```sh
fab run
```

6. Browse to the website
You should be able to see the site running at http://localhost:5000/

7. Hack
