class Remote:

    def __init__(self, channel=0, volume=0):
        self.channel = channel
        self.volume = volume

    def channel_up(self):
        self.channel += 1

    def channel_down(self):
        if self.channel <= 0:
            return 0
        if self.channel > 0:
            self.channel -= 1

    def volume_up(self):
        self.volume += 1

    def volume_down(self):
        if self.volume <= 0:
            return 0
        if self.volume > 0:
            self.volume -= 1

    def current_channel_volume(self):
        print(f'CHANNEL: {self.channel}\nVOLUME: {self.volume}')


