import os
import sys
sys.path.insert(0,os.path.abspath('../'))

print("to jest skrypt główny języka python w projekccie dokumentacja")

"""
to jest opis ogólny skryptu głowngo
program - dokumentacja
przygotowany przez Marcin Albiniak
"""

'''
drugi komemntarz
niedokumentacyjny
'''

class Testowa:
    """
    Klasa testowa
    służy do przetestowania dokumentacji A
    """
    def __init__(self):
        self.x = 100

def to_funkcja(a):
    """
    analiza funkcji
    :param a: wartość zadana
    :return: dziesięciokrotność a
    """
    return a*10
