class Televisao:
    def __init__(self):
        self.ligada = False

    def power(self):
        if self.ligada:
            self.ligada = False
            self.canal  = 5
        else:
            self.ligada = True

    def aumeta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1
print(__name__)
if __name__ == '__main__':
    televisao = Televisao()
    print('Televisão está ligada? {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada? {}'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada? {}'.format(televisao.ligada))
    print('Canal -> {}'.format(televisao.canal))
    televisao.power()
    print('Televisão está ligada? {}'.format(televisao.ligada))
    televisao.aumeta_canal()
    televisao.aumeta_canal()
    print('Canal -> {}'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal -> {}'.format(televisao.canal))