from datetime import timedelta, datetime

def zaokrozen_zmin(time_input, zmin, operator):
    '''
    zaokroži čas glede na zmin podan v minutah
    Author: Vasja Pavlovič 2017
    '''
    hours, reminder = divmod(time_input.seconds, 3600)
    minutes, seconds = divmod(reminder, 60)
    # koliko je celih 
    x, ostanek = divmod(minutes, zmin)
    if ostanek > 0:
        if operator == "+":
            x = x + 1
        if operator == "-":
            x
    # če je x=6 je potrebno tudi uro povečati +1
    if x == 6:
        hours = hours + 1
    hours = hours
    minutes = zmin * x
    seconds = 0
    zaokrozen_zmin = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    return zaokrozen_zmin

def pretvori_v_ure(time_input):
    '''
    timedelta object pretvori v ure npr. timedelta(hours=x)
    '''
    seconds = time_input.seconds
    skupaj_ur = seconds/3600
    return skupaj_ur