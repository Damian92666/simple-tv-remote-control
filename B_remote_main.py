from B_remote import Remote

if __name__ == '__main__':

    remote = Remote()
    remote.current_channel_volume()

    while True:

        type = input("""Witamy w smart TV:
Kanał do przodu wybierz '>'
Kanał do tyłu wybierz '<'
Zwiększ głośność wybierz '+'
Zmniejsz głośność wybierz '-'
Wyłącz TV wybierz '*'
Kanał losowy wybierz '#'
""")

        if type == '>':
            remote.channel_up()
        if type == '<':
            remote.channel_down()
        if type == '+':
            remote.volume_up()
        if type == '-':
            remote.volume_down()
        if type == '#':
            remote.random_channel()
        if type == '*':
            remote.turn_off_tv()

        remote.current_channel_volume()
