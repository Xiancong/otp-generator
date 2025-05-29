import os

def get_secret():
    secret = os.getenv("secret")
    if not secret:
        raise EnvironmentError("Secret not found")
    return secret
