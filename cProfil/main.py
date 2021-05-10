"""
Trouver 100 nombres premiers aléatoires entre 2 et 1000
Un nombre premier est un nombre entier naturel (non nul) qui admet exactement 2 diviseurs distincts : 1 et lui-même.
"""
import random
import cProfile


def guess():
    """
    Renvoie un nombre aléatoire entre 2 et 2000
    :return int(2,1000):
    """
    return random.randint(2, 2000)


def is_premier(x):
    """
    Check si le nombre est un nombre premier
    :param x:
    :return:
    """
    for i in range(x):
        for j in range(x):
            if i * j == x:
                return False
    return True

def is_premier2(x):
    """
    Check si le nombre est un nombre premier
    :param x:
    :return:
    """
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


def trouver_premiers(num):
    premier = []
    for i in range(num):
        p = guess()
        while not is_premier(p):
            p = guess()
        premier += [p]
    return premier

trouver_premiers(100)
#cProfile.run('print(trouver_premiers(100))')

