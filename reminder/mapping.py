#coding: utf-8
host_url = 'http://127.0.0.1:8000'
site_mapping = {
    "authorization": {
        "url": host_url + "/register/login/",
        "username": "/html/body/form/input[2]",
        "password": "/html/body/form/input[3]",
        "login button": "/html/body/form/button",
    },
}
