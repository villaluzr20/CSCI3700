# CSCI3700
## Let's get setup!
First, we need to install a Python 3 virtual environment with:
```
sudo apt-get install python3-venv
```

Create a virtual environment:
```
python3 -m venv venv
```

You need to activate the virtual environment when you want to use it:
```
source python_venv/bin/activate
```

Now that the virtual environment is activated, use the Python package manager 'pip' to install Flask
```
(venv) $ pip install Flask
```
We'll use the flask command to run the application, but before that, we need to communicate with the application and use the 'FLASK_APP' environment variable:
```
(venv) $ export FLASK_APP=uniquefruits.py
(venv) $ flask run
```
On the browser, it should either show "Success!" Or error message from PostgreSQL
when accessed on a Flask server with 127.0.0.1:5000/api/update_basket_a.
