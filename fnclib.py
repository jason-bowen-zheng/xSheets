# data/fnclib.py
# function library

from datatype import *
import math
import random

# Math function #

def math_abs(x):
    # abs(x)
    if isinstance(x, data_num):
        return ['NUM', math.fabs(x)]
    else:
        return ['ERR', 'value error']

def math_acos(x):
    # acos(x)
    if isinstance(x, data_num):
        return ['NUM', math.acos(x)]
    else:
        return ['ERR', 'value error']

def math_asin(x):
    # asin(x)
    if isinstance(x, data_num):
        return ['NUM', math.asin(x)]
    else:
        return ['ERR', 'value error']

def math_atan(x):
    # atan(x)
    if isinstance(x, data_num):
        return ['NUM', math.atan(x)]
    else:
        return ['ERR', 'value error']

def math_atan2(y, x):
    # atan2(y, x)
    if isinstance(x, data_num) and isinstance(x, data_num):
        return ['NUM', math.atan2(y,x)]
    else:
        return ['ERR', 'value error']

def math_ceil(x):
    # ceil(x)
    if isinstance(x, data_num):
        return ['NUM', math.ceil(x)]
    else:
        return ['ERR', 'value error']

def math_cos(x):
    # cos(x)
    if isinstance(x, data_num):
        return ['NUM', math.cos(x)]
    else:
        return ['ERR', 'value error']

def math_degrees(x):
    # degrees(x)
    if isinstance(x, data_num):
        return ['NUM',  math.degrees(x)]
    else:
        return ['ERR',  'value error']

def math_exp(x):
    # exp(x)
    if isinstance(x, data_num):
        return ['NUM', math.exp(x)]
    else:
        return ['ERR', 'value error']

def math_E():
    # E()
    return ['NUM', math.e]

def math_floor(x):
    # floor(x)
    if isinstance(x, data_num):
        return ['NUM', math.floor(x)]
    else:
        return ['ERR', 'value error']

def math_mod(x, y):
    # mod(x, y)d
    if isinstance(x, data_num) and isinstance(y, data_num):
        return ['NUM', math.fmod(x, y)]
    else:
        return ['ERR', 'value error']

def math_pow(x, y):
    # pow(x, y)
    if isinstance(x, data_num) and isinstance(x, data_num):
        return ['NUM', math.pow(x, y)]
    else:
        return ['ERR', 'value error']

def math_PI():
    # PI()
    return ['NUM', math.pi]

def math_radians(x):
    # radians(x)
    if isinstance(x, data_num):
        return ['NUM', math.radians(x)]
    else:
        return ['ERR', 'value error']

def math_rand():
    # rand()
    return ['NUM', random.random()]

def math_round(x, n=None):
    # round(x, [n])
    if isinstance(x, data_num) and (isinstance(n, int) or (n == None)):
        return ['NUM', round(x, n)]
    else:
        return ['ERR', 'value error']

def math_sin(x):
    # sin(x)
    if isinstance(x, data_num):
        return ['NUM', math.sin(x)]
    else:
        return ['ERR', 'value error']

def math_sqrt(x):
    # sqrt(x)
    if isinstance(x, data_num) and (x >= 0):
        return ['NUM', math.sqrt(x)]
    else:
        return ['ERR', 'value error']

def math_tan(x):
    if isinstance(x, data_num):
        return ['NUM', math.tan(x)]
    else:
        return ['ERROR', 'value error']

def math_TAU():
    # TAU()
    # PI is wrong, use TAU!
    return ['NUM', math.tau]

# Str function #

def str_find(s, text, start=None, end=None):
    # find(s, [start, [end]])
    if isinstance(s, data_str) and isinstance(text, str) and (isinstance(start, int) or (start == None)) and (isinstance(end, int) or (end == None)):
        return ['NUM', s.find(text, start, end)]
    else:
        return ['ERR', 'value error']

def str_format(text, *value):
    # format(text, value1, value2, ...)
    try:
        if isinstance(text, str):
            return ['STR', text % value]
        else:
            return ['ERR', 'value error']
    except:
        return ['ERR', 'argument error']
    else:
        pass

def str_len(s):
    # len(s)
    if isinstance(s, str):
        return ['NUM', len(s)]
    else:
        return ['ERR', 'value error']

def str_slice(s, start, end=None):
    # slice(s, start, [end])
    if isinstance(s, str) and isinstance(start, int) and (isinstance(end, int) or (end == None)):
        if (start > 0) and (start < len(s) - 1):
            return ['STR', s[start:end]]
        elif (start < 0) and (start < -len(s)):
            return ['STR', s[start:end]]
        else:
            return ['ERR', 'index error']
    else:
        return ['ERR', 'value error']

# Run function #

def run_function(fname, *args):
    # fname(*args)
    try:
        # Math function #
        if   fname == 'abs':
            return math_abs(*args)
        elif fname == 'acos':
            return math_acos(*args)
        elif fname == 'asin':
            return math_asin(*args)
        elif fname == 'atan':
            return math_atan(*args)
        elif fname == 'atan2':
            return math_atan2(*args)
        elif fname == 'ceil':
            return math_ceil(*args)
        elif fname == 'cos':
            return math_cos(*args)
        elif fname == 'exp':
            return math_exp(*args)
        elif fname == 'E':
            return math_E(*args)
        elif fname == 'degrees':
            return math_degrees(*arg)
        elif fname == 'floor':
            return math_floor(*args)
        elif fname == 'mod':
            return math_mod(*args)
        elif fname == 'pow':
            return math_pow(*args)
        elif fname == 'PI':
            return math_PI(*args)
        elif fname == 'radians':
            return math_radians(*args)
        elif fname == 'rand':
            return math_rand(*args)
        elif fname == 'round':
            return math_round(*args)
        elif fname == 'sin':
            return math_sin(*args)
        elif fname == 'sqrt':
            return math_sqrt(*args)
        elif fname == 'tan':
            return math_tan(*args)
        elif fname == 'TAU':
            return math_TAU(*args)
        # Str function #
        elif fname == 'find':
            return str_find(*args)
        elif fname == 'format':
            return str_format(*args)
        elif fname == 'len':
            return str_len(*args)
        elif fname == 'slice':
            return str_slice(*args)
        else:
            return ['ERR', 'function not found']
    except:
        return ['ERR', 'argument error']