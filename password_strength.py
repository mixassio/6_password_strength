import re
import getpass
import requests

def get_user_password():
    password = getpass.getpass(prompt='Enter password: ')
    return password

def check_blacklist(password):
    rating = 0
    list_rating = []
    # я создал блэк лист из 15000 паролей в гугл-доксе
    url_blacklist = 'https://docs.google.com/spreadsheets/d/1B3t1Oi8E5vD311Wog8BCZXao92rPfOaNZ3DFvTcuL9M/pub?output=csv'
    black_list = requests.get(url_blacklist)
    for black_password in black_list.text.split('\r\n'):
        if black_password == password:
            list_rating += ['Very bad password']
            break
    else:
        rating += 2
        list_rating += ['Not in black list +2',]
    #check part popular password
    for black_password in black_list.text.split('\r\n'):
        if password.find(str(black_password)) > 0:
            rating -= 1
            list_rating += ['parts popular pasword -1']
            break
    return rating, list_rating

def check_char(password):
    rating = 0
    list_success = []
    #check character
    if re.findall('([a-zA-Z])', password) != []:
        rating += 1
        list_success.append('character+1')
    #check on upper and lower case
    is_upp = set()
    is_low = set()
    for letter in password:
        is_low.add(letter.islower())
        is_upp.add(letter.isupper())
    if True in is_low and True in is_upp:
        rating += 2
        list_success.append('lower+upper+2')
    #check number
    if re.findall('(\d+)', password) != []:
        rating += 1
        list_success.append('number+1')
    #check punctuation
    if re.findall('[^\w\s]', password) != []:
        rating += 1
        list_success.append('punctuation +1')
    return rating, list_success

def check_len(password):
    if len(password) >= 6:
        return 1, ['lenght +1'] 
    else:
        return 0, []

def check_year(password):
    rating = 1
    list_success = []   
    for year in range(1950,2017):
        if password.find(str(year)) > 0:
            rating -= 1
            list_success.append('year -1')
            break
    return rating, list_success

def get_password_strength(password):
    rating_sum, list_sum = map(lambda check_blacklist, check_char, check_len, check_year:
                               check_blacklist + check_char + check_len + check_year,
                               check_blacklist(password), check_char(password), check_len(password), check_year(password))
    print('Password complexity (1 - 10) : {}'.format(rating_sum))
    print('---------------------------------')
    for deposit in list_sum:
        print(deposit)



if __name__ == '__main__':
    password = get_user_password()
    get_password_strength(password)
