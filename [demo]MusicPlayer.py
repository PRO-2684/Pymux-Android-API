from android import MediaPlayer as Player
print('''Command:
    .play(path='')
    .pause
    .stop
    .info
    .exit''')
while True:
    i=input('Player.')
    if i=='exit':break
    j='' if i.endswith(')') else '()'
    print(eval('Player.'+i+j),end='')
