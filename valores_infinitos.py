# Manejo de valores infinitos
import math
from decimal import Decimal

infinito_positivo = float('inf')
print(f'Infinito positivo: {infinito_positivo}')
print(f'¿Es infinito?: {math.isinf(infinito_positivo)}') #True

infinito_negativo = float('-inf')
print(f'Infinito negativo: {infinito_negativo}')
print(f'¿Es infinito?: {math.isinf(infinito_negativo)}') #True

#Infinito con librería math
infinito_positivo = math.inf
print(f'Infinito + con math: {infinito_positivo}')
print(f'¿Es infinito?: {math.isinf(infinito_positivo)}') #True

infinito_negativo = -math.inf
print(f'Infinito - con math: {infinito_negativo}')
print(f'¿Es infinito?: {math.isinf(infinito_negativo)}') #True

#Infinito con librería Decimal
infinito_positivo = Decimal('Infinity')
print(f'Infinito + con Decimal: {infinito_positivo}')
print(f'¿Es infinito?: {math.isinf(infinito_positivo)}') #True

infinito_negativo = Decimal('-Infinity')
print(f'Infinito - con Decimal: {infinito_negativo}')
print(f'¿Es infinito?: {math.isinf(infinito_negativo)}') #True