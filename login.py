#!/usr/bin/env python3

from HduSrunLogin.LoginManager import LoginManager

def auto_login(username:str, pasword:str):
    lm = LoginManager()
    lm.login(
        username=username,
        password=pasword
    )