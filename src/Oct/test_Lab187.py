# PASSWORD - i store the password in the framework?

# Env File - .(dot.env)
# How do you store your password or credentials in the framework.
# pip install python-dotenv

from dotenv import load_dotenv
import os


def test_update_req():
    load_dotenv()
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    print(username)
    print(password)
