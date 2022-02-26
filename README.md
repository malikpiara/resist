## Getting Started

**_Prerequisites: Python 3.9.0._**

```shell script
$ git clone https://github.com/malikpiara/resist.git.

$ cd resist-email

$ python3 -m venv venv              # Create a virtual environment.

$ source venv/bin/activate          # Activate your virtual environment.

$ pip install -r requirements.txt   # Install project requirements.

$ export FLASK_ENV=development      # Enable hot reloading, debug mode.

$ flask run
```

The app will only work locally when the debug is enabled due to [Flask-talisman](https://github.com/GoogleCloudPlatform/flask-talisman), which forces all connects to https.

The default content security policy is extremely strict and will prevent loading any resources that are not in the same domain as the application. [Here are some examples on how to change the default policy](https://github.com/GoogleCloudPlatform/flask-talisman#content-security-policy).
