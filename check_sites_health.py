from whois import whois
import requests
import datetime
import sys
import os


def load_urls4check(path):
    with open(path, 'r') as url_server_file:
        url_server_list = url_server_file.read().split()
    return url_server_list


def is_server_respond_with_200(url):
    return requests.get(url).ok


def get_domain_expiration_date(domain_name):
    return whois(domain_name)['expiration_date']


def is_domain_paid(domain_name, period_of_time):
    days_left = get_domain_expiration_date(domain_name) - datetime.datetime.today()
    if days_left > datetime.timedelta(days=period_of_time):
        return True
    return days_left


def main():
    url_server_list = load_urls4check(file_path)
    days_left = 30
    for url in url_server_list:
        site_status = is_server_respond_with_200(url)
        domain_paid = is_domain_paid(url, days_left)
        print('Сервер:{} -  доступен({}) и домен оплачен({})'.format(url, site_status, domain_paid))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = input('Укажите путь к файлу: ')
    if os.path.exists(file_path):
        main()
    else:
        print('Неверный путь к файлу')