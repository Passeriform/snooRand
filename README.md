# snooRand
*snooRand fetches a random post from a subreddit. That's it.*

The project is a flask based application using PRAW for reddit parsing.

------

To start using:

-  Create new virtualenv `python -m virtualenv venv`

-  Activate the virtualenv

    -  Windows    `\> . venv/Scripts/activate`
    -  Linux/OSX  `$ . venv/bin/activate`

-  Install dependencies `python -m pip install -r requirements.txt`

-  Create a script application key-secret pair on reddit developer API

-  Modify .env file accordingly

-  Run the application  `python main.py`
