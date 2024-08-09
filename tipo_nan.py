import math
from decimal import Decimal

# Un tipo nan "Not a number" proviene de operaciones matemáticas

# Con el constructor de la clase Float
a = float('Nan') #No es case sensitive, sirve Nan, nan, NaN
print(f'a con float: {a}')
print(f'¿a es nan?: {math.isnan(a)}') #preguntarse si es nan

# Con el constructor de la clase Decimal
a = Decimal('NAn') #No es case sensitive, sirve Nan, nan, NaN
print(f'a con math: {a}')
print(f'¿a es nan?: {math.isnan(a)}') #preguntarse si es nan