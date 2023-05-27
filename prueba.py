import re




numero = 'a9.9'

patron = r'^[0-9]+.[0-9]+$|[0-9]+$'
if bool(re.match(patron,numero)):
    print('es numero')
else:
    print('no es numero')