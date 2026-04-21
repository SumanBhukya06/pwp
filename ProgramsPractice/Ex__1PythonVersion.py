import sys
class Ver:
    def sys_version(self):
        print(sys.version.split()[0])
vobj=Ver()
vobj.sys_version()

class first:
    s="Hello world"
    def fw(self):
        print(self.s.split()[0])
vobj1=first()
vobj1.fw()