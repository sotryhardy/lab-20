from lab20 import prow

a = input('Wprowadź coś: ')
try:
    assert a == prow(a), 'To nie palindrom'
except AssertionError:
    print('To nie palindrom')
