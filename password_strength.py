import argparse
import re
import getpass

def get_user_password():
    password = getpass.getpass(prompt='Enter password: ')
    return password

def check_blacklist(password):
    rating = 0
    list_rating = []
    file_bl = open('passw_black_list.txt', 'r')
    black_list = [line.strip() for line in file_bl]
    file_bl.close()
    if password in black_list:
        list_rating += ['Very bad password']
    else:
        rating += 2
        list_rating += ['Not in black list +2',]
    #check part popular password
    for pasw in black_list:
        if password.find(str(pasw)) > 0:
            rating -= 1
            list_rating += ['parts popular pasword -1']
            break
    return rating, list_rating

def check_char(password):
    status_pasw = 0
    list_success = []
    #check character
    if re.findall('([a-zA-Z])', password) != []:
        status_pasw += 1
        list_success.append('character+1')
    #check on upper and lower case
    is_upp = set()
    is_low = set()
    for letter in password:
        is_low.add(letter.islower())
        is_upp.add(letter.isupper())
    if True in is_low and True in is_upp:
        status_pasw += 2
        list_success.append('lower+upper+2')
    #check number
    if re.findall('(\d+)', password) != []:
        status_pasw += 1
        list_success.append('number+1')
    #check punctuation
    if re.findall('[^\w\s]', password) != []:
        status_pasw += 1
        list_success.append('punctuation +1')
    return status_pasw, list_success

def check_len(password):
    if len(password) >= 6:
        return 1, ['lenght +1'] 
    else:
        return 0, []

def check_year(password):
    status_pasw = 1 
    list_success = []   
    for year in range(1950,2017):
        if password.find(str(year)) > 0:
            status_pasw -= 1
            list_success.append('year -1')
            break
    return status_pasw, list_success

def get_password_strength(password):
    status_sum, list_sum = map(lambda a, b, c, d: a + b + c + d, check_blacklist(password), check_char(password), check_len(password), check_year(password))
    print('Password complexity (1 - 10) : {}'.format(status_sum))
    print('---------------------------------')
    for deposit in list_sum:
        print(deposit)



if __name__ == '__main__':
    password = get_user_password()
    get_password_strength(password)
