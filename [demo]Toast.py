from android import Toast
m=input('Message: ')
bg=input('Background color: ')
fg=input('Foreground color: ')
#color argument can be a standard name(i.e. 'red', 'grey') or 6/8 digit value(i.e.'#FF0000' or '#FFFF0000'), where order is (AA)RRGGBB.(AA means transparency.)
a=Toast(m,bg,fg)
a.pos='top'
#'pos' argument can be one of the following: 'top', 'middle', 'bottom'.
#Invalid arguments will revert to default value(grey, white, middle).
a.show()
