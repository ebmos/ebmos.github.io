class pizza():
    def __init__(self, mel, gjær, vann, salt):
        self.mel = mel
        self.gjær = gjær
        self.vann = vann
        self.salt = salt

    def ovn(self):
        self.temperatur = 200
        self.tid = 20
        self.bunn_pizza = self.mel+self.gjær+self.vann+self.salt+self.temperatur+self.tid
        return self.bunn_pizza

eske = pizza(0.5,1,0.4, 0.02)

print(eske.ovn())