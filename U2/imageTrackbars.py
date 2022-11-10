def noopFunc(arg):
    print('(noopFunc)', arg)


filterValue = 0


def filterOnChange(value):
    global filterValue
    if filterValue == value:
        return

    filterValue = value
    print('(filterOnChange)', filterValue)
