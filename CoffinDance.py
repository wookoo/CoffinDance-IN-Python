from winsound import Beep
import time
def do (time=200):
    Beep(261,time)
def do_sharp (time=200):
    Beep(277,time)
def rae (time=200):
    Beep(293,time)
def rae_sharp (time=200):
    Beep(311,time)
def me (time=200):
    Beep(329,300)
def fa (time=time):
    Beep(349,300)
def fa_sharp (time=200):
    Beep(369,time)
def sol (time=200):
    Beep(392,time)
def sol_sharp (time=200):
    Beep(415,time)
def ra (time=200):
    Beep(440,time)
def ra_shar (time=200):
    Beep(446,time)
def si (time=200):
    Beep(493,time)

def high_do (time=200):
    Beep(523,time)
def high_do_sharp (time=200):
    Beep(554,time)

def high_rae (time=200):
    Beep(587,time)
def high_rae_sharp (time=200):
    Beep(622,time)
def high_me (time=200):
    Beep(659,time)
def high_fa (time=200):
    Beep(698,time)
def high_fa_sharp (time=200):
    Beep(739,time)
def high_sol (time=200):
    Beep(783,time)
def high_sol_sharp (time=200):
    Beep(830,time)
def high_ra (time=200):
    Beep(880,time)
def high_ra_sharp (time=200):
    Beep(932,time)
def high_si (time=200):
    Beep(987,time)


def main_melody():
    fa_sharp()
    time.sleep(0.2)
    fa_sharp()
    high_do_sharp()
    si()
    time.sleep(0.2)
    ra()
    time.sleep(0.2)
    sol_sharp()
    time.sleep(0.2)
    sol_sharp()
    sol_sharp()
    si()
    time.sleep(0.2)
    ra()
    sol_sharp()
    fa_sharp()
    time.sleep(0.2)
    fa_sharp()
    high_ra()
    high_sol_sharp()
    high_ra()
    high_sol_sharp()
    high_ra()

    fa_sharp()
    time.sleep(0.2)
    fa_sharp()
    high_ra()
    high_sol_sharp()
    high_ra()
    high_sol_sharp()
    high_ra()

def sub_melody():
    for i in range(4):
        ra(200)

    for i in range(4):
        high_do_sharp(200)

    for i in range(4):
        si(200)
    for i in range(4):
        high_me(200)

    for i in range(12):
        high_fa_sharp(200)

    si(200)
    ra(200)
    sol_sharp(200)
    me(200)


main_melody()
main_melody()
main_melody()
sub_melody()
main_melody()
main_melody()
main_melody()
sub_melody()
