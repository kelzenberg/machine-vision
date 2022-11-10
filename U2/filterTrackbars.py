def noopFunc(arg):
    print('(noopFunc)', arg)


sigmaValue = 0.1


def sigmaOnChange(value):
    newValue = (value + 1) / 10

    global sigmaValue
    if sigmaValue == newValue:
        return

    sigmaValue = newValue
    print('(sigma)', sigmaValue)
