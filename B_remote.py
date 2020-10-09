# klikając '+' zwiększam głośność
# klikając '-' zmniejszam głośność
# klikając '>' kanał do przodu
# klikając '<' kanał do tyłu
# klikając '*' wyłączam tv
# kanały są od 1 do 50 w tym od 10 do 12 oraz od 22 do 24 niedostępne
# losowy kanał '#'

import random

class Remote:

    def __init__(self, channel=1, volume=15):
        self.channel = channel
        self.volume = volume
        self.channel_up_max = 1

    def channel_up(self):
        if self.channel == 9:
            self.channel += 3
        if self.channel == 21:
            self.channel += 3
        if self.channel == 50:
            self.channel = 0
        self.channel += 1

    def channel_down(self):
        if self.channel == 25:
            self.channel -= 3
        if self.channel == 13:
            self.channel -= 3
        if self.channel == 1:
            self.channel = 50
        elif self.channel > 0:
            self.channel -= 1

    def volume_up(self):
        if self.volume == 50:
            return 50
        self.volume += 1

    def volume_down(self):
        if self.volume <= 0:
            return 0
        elif self.volume > 0:
            self.volume -= 1

    def turn_off_tv(self):
        exit()

    def random_channel(self):
        self.channel = random.randint(1, 50)

    def current_channel_volume(self):
        print(f'Obecny kanał to: {self.channel}\nObecna głośność to: {self.volume}')
