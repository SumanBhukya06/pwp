class Bank:
    def roi(self):
        return 0
class XBank(Bank):
    def roi(self):
        return 10.5
class YBank(Bank):
    def roi(self):
        return 12.5
x=XBank()
print(x.roi())

y=YBank()
print(y.roi())
