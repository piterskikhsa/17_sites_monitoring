# Sites Monitoring Utility

The script displays information about the availability of the site.
Displays the site online or not, and the domain payment period has expired or not

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```#!bash

pip install -r requirements.txt # alternatively try pip3

python check_sites_health.py

Укажите путь к файлу: site.txt
Сервер:http://ya.ru -  доступен(True) и домен оплачен(True)
Сервер:http://mail.ru -  доступен(True) и домен оплачен(True)

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
