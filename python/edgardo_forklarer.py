def mammaspizza():
    vann= 0.5
    mel = 0.75
    gjær = 0.5
    ost = 0.75
    tomat = 0.2
    brett = vann+mel+gjær+ost+tomat
    return brett

def ovn():
    temp = 200
    tid = 20
    pizza = mammaspizza()
    return pizza

middag = ovn()
print(middag)
