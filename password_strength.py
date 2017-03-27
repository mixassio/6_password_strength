import argparse
import re

def create_parser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('password')
    parser.add_argument ('-v', '--valuation', action='store_const', const=True)
    return parser

def get_password_strength(password):
    status_pasw = 1
    list_success = []
    # check popular pasword
    popular_pasw = ['123456', '123456789', 'qwerty', '111111', '1234567', '666666', '12345678', '7777777', '123321',
                    '654321', '1234567890', '123123', '555555', 'vkontakte', 'gfhjkm', '159753', '777777',
                    'TempPassWord', 'qazwsx', '1q2w3e', '1234', '112233', '121212', 'qwertyuiop', 'qq18ww899',
                    '987654321', '12345', 'zxcvbn', 'zxcvbnm', '999999', 'samsung', 'ghbdtn', '1q2w3e4r', '1111111',
                    '123654', '159357', '131313', 'qazwsxedc', '123qwe', '222222', 'asdfgh', '333333', '9379992',
                    'asdfghjkl', '4815162342', '12344321', '88888888', '11111111', 'knopka', '789456', 'qwertyu',
                    '1q2w3e4r5t', 'iloveyou', 'vfhbyf', 'marina', 'password', 'qweasdzxc', '10203', '987654', 'yfnfif',
                    'cjkysirj', 'nikita', '888888', 'vfrcbv', 'k.,jdm', 'qwertyuiop[]', 'qwe123', 'qweasd', 'natasha',
                    '123123123', 'fylhtq', 'q1w2e3', 'stalker', '1111111111', 'q1w2e3r4', 'nastya', '147258369',
                    '147258', 'fyfcnfcbz', '1234554321', '1qaz2wsx', 'andrey', '111222', '147852', 'genius', 'sergey',
                    '7654321', '232323', '123789', 'fktrcfylh', 'spartak', 'admin', 'test', '123', 'azerty', 'abc123',
                    'lol123', 'easytocrack1', 'hello', 'saravn', 'holysh!t', 'Test123', 'tundra_cool2', '456',
                    'dragon', 'thomas', 'killer', 'root', '1111', 'pass', 'master', 'aaaaaa', 'monkey', 'daniel',
                    'asdasd', 'e10adc3949ba59abbe56e057f20f883e', 'changeme', 'computer', 'jessica', 'letmein',
                    'mirage', 'loulou', 'lol', 'superman', 'shadow', 'admin123', 'secret', 'administrator', 'sophie',
                    'kikugalanetroot', 'doudou', 'liverpool', 'hallo', 'sunshine', 'charlie', 'parola', '100827092',
                    'michael', 'andrew', 'password1', 'fuckyou', 'matrix', 'cjmasterinf', 'internet', 'hallo123',
                    'eminem', 'demo', 'gewinner', 'pokemon', 'abcd1234', 'guest', 'ngockhoa', 'martin', 'sandra',
                    'asdf', 'hejsan', 'george', 'qweqwe', 'lollipop', 'lovers', 'q1q1q1', 'tecktonik', 'naruto',
                    'password12', 'password123', 'password1234', 'password12345', 'password123456', 'password1234567',
                    'password12345678', 'password123456789', '000000', 'maximius', '123abc', 'baseball1', 'football1',
                    'soccer', 'princess', 'slipknot', '11111', 'nokia', 'super', 'star', '666999', '12341234',
                    '1234321', '135790', '159951', '212121', 'zzzzzz', '121314', '134679', '142536', '19921992',
                    '753951', '7007', '1111114', '124578', '19951995', '258456', 'qwaszx', 'zaqwsx', '55555', '77777',
                    '54321', 'qwert', '22222', '33333', '99999', '88888', '66666']
    if password in popular_pasw:
        return status_pasw#Popular passwords have index 1 and are not checked further
    else:
        status_pasw += 1
        list_success.append('not in list+1')
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
        list_success.append('punctuation+1')
    if len(password) > 6:
        status_pasw += 1
        list_success.append('lenght+1')
    #check include year
    status_pasw += 1
    list_success.append('not year+1')
    for year in range(1950,2017):
        if password.find(str(year)) > 0:
            status_pasw -= 1
            list_success.append('year-1')
            break
    # Checking the parts of popular passwords
    status_pasw += 1
    list_success.append('not parts popular pasword+1')
    for pasw in popular_pasw:
        if password.find(str(pasw)) > 0:
            status_pasw -= 1
            list_success.append('parts popular pasword-1')
            break
    return status_pasw, list_success



if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()

    status_pasw, list_success = get_password_strength(namespace.password)
    print('Password complexity (1 - 10) : {}'.format(status_pasw))
    if namespace.valuation:
        for valuation in list_success:
            print(valuation)
