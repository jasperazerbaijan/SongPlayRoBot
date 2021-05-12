import os
API_ID = int(os.getenv("3588368"))
API_HASH = os.getenv("3d64c47cfe8d1cb0fc2cc06f5512298e")
BOT_TOKEN = os.getenv("1696209895:AAGuvZul5t2UoT1NaD37RvqnIiXS6zsZJ-g")
DATABASE_URL = os.getenv("postgres://fyraavjhbspcab:d2b28de5288ab3218a5d80efb810a14a7691e6261df49e1fd70b5e464f69cd5c@ec2-75-101-232-85.compute-1.amazonaws.com:5432/dbejeua9gv7ibk")
OWNER_ID = list({int(x) for x in os.environ.get("940086446", "").split()})
