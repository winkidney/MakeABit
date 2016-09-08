import os

from cmdtree import command, entry
from django.core.management.utils import get_random_secret_key


HERE = os.path.abspath(os.path.dirname(__file__))
LOCAL_SETTINGS = os.path.join(HERE, "sentence/local_settings.py")


@command()
def gen_secret_key():
    print(get_random_secret_key())


@command()
def gen_production_setting():
    if os.path.exists(LOCAL_SETTINGS):
        print("file existed")
        return
    key = get_random_secret_key()

    tpl ="""
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{key}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1']
""".format(key=key)

    with open(LOCAL_SETTINGS, "w") as fp:
        fp.write(tpl)


if __name__ == "__main__":
    entry()