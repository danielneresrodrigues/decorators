#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 18:26:06 2024

@author: danielneresrodrigues
"""

# =============================================================================
# ============================Logs sem decorator===============================
# =============================================================================

from datetime import datetime

def soma(a, b):
    
    agora = datetime.now()
    resultado = a + b
   
    print(f'\nHorário: {agora}')
    print('Função: soma')
    print(f'Argumentos: {a}, {b}')
    print(f'Resultado: {resultado}\n')
    
    return a + b

def subtrai(a, b):
    
    agora = datetime.now()
    resultado = a - b
    
    print(f'\nHorário: {agora}')
    print('Função: subtrai')
    print(f'Argumentos: {a}, {b}')
    print(f'Resultado: {resultado}\n')
    
    return resultado

resultado_soma = soma(33,67)

resultado_subtracao = subtrai(64,29)

# =============================================================================
# ============================Logs com decorator===============================
# =============================================================================

from datetime import datetime

def log(funcao):
    
    def wrapper(*args, **kwargs):
        
        agora = datetime.now()
        resultado = funcao(*args, **kwargs)
        
        print(f'\nHorário: {agora}')
        print(f'Função: {funcao.__name__}')
        print(f'Argumentos: {args}')
        print(f'Resultado: {resultado}\n')
        
        return resultado
    
    return wrapper

@log
def soma(a, b):
    return a + b

@log
def subtrai(a, b):    
    return a -b

resultado_soma = soma(33,67)

resultado_subtracao = subtrai(64,29)