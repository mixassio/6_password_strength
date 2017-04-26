import re
import getpass
import requests


def get_user_password():
    password = getpass.getpass(prompt='Enter password: ')
    return password


def download_password_black_list():
    url_blacklist = 'https://docs.google.com/spreadsheets/d/1B3t1Oi8E5vD311Wog8BCZXao92rPfOaNZ3DFvTcuL9M/pub?output=csv'
    black_list = requests.get(url_blacklist)
    return black_list.text.split('\r\n')


def check_blacklist(password):
    black_list = download_password_black_list()
    for black_password in black_list:
        if black_password == password:
            break
    else:
        return True

def check_character(password):
    if re.findall('([a-zA-Z])', password):
        return True


def check_upper_lower(password):
    is_upp = False
    is_low = False
    for letter in password:
        if letter.islower() and not is_low: 
            is_low = True
        elif letter.isupper()and not is_upp: 
            is_upp = True
        if is_upp and is_low: 
            return True


def check_number(password):
    if re.findall('(\d+)', password):
        return True


def check_punctuation(password):
    if re.findall('[^\w\s]', password):
        return True


def check_len(password):
    if len(password) >= 6:
        return True
        

def check_year(password): 
    for year in range(1950,2017):
        if str(year) in password:
            return True


def get_password_strength(password):
    rating_sum = 0
    list_sum = []
    rating = {'check_blacklist': {'status': check_blacklist(password), 'weigth': 2, 'text': 'Not in black list +2'},
              'check_character': {'status': check_character(password), 'weigth': 1, 'text': 'character+1'},
              'check_upper_lower': {'status': check_upper_lower(password), 'weigth': 2, 'text': 'lower+upper+2'},
              'check_number': {'status': check_number(password), 'weigth': 1, 'text': 'number+1'},
              'check_punctuation': {'status': check_punctuation(password), 'weigth': 1, 'text': 'punctuation +1'},
              'check_len': {'status': check_len(password), 'weigth': 1, 'text': 'lenght +1'},
              'check_year': {'status': check_year(password), 'weigth': -1, 'text': 'year -1'}}
    for check, value in rating.items():
        if value['status']:
            rating_sum += value['weigth']
            list_sum.append(value['text'])
    return rating_sum, list_sum


def pretty_print(rating_sum, list_sum):
    print('Password complexity (1 - 10) : {}'.format(rating_sum))
    print('---------------------------------')
    for deposit in list_sum:
        print(deposit)


if __name__ == '__main__':
    password = get_user_password()
    rating_sum, list_sum = get_password_strength(password)
    pretty_print(rating_sum, list_sum)