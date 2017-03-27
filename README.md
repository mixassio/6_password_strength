# Password Strength Calculator

The script is designed to evaluate the complexity of the password.
- Use checks
- Popular passwords
- Presence of letters in upper and lower case
- The presence of numbers
- Symbol Punctuation
- Inclusion in the password of the year
- Include in the password parts of popular passwords

When using the parameter -v decoding is printed, what parameters were involved in the evaluation

# HOW RUN

Example of script launch on Linux, Python 3.5:
RUN on Linux:

usage: password_strength.py [-h] [-v] password

```#!bash

$ python3 password_strength.py -v 'jhykjbL98;'

Password complexity (1 - 10) : 10
not in list+1
character+1
lower+upper+2
number+1
punctuation+1
lenght+1
not year+1
not parts popular pasword+1
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
