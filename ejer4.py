class cuentabancaria():
    def __init__(self,id,titular,fecha,numerocuenta,saldo):
        self.id=id
        self.titular=titular
        self.fecha=fecha
        self.numerocuenta=numerocuenta
        self.saldo=saldo

    
    def retirar(self,dinero):
        if (self.saldo>=dinero):
            self.saldo=self.saldo-dinero
        else:
            print("no puede retirar más dinero del que tiene")

    def ingresar(self, dinero):
        self.saldo=self.saldo+dinero

    
    
    def transferir(self,dinero,cuenta):
        if (self.saldo>=dinero):
            self.saldo=self.saldo-dinero
            cuenta.saldo=cuenta.saldo+dinero
        else:
            print("no puede transferir más dinero del que tiene")

#class plazofijo(cuentabancaria):


#class vip(cuentabancaria):



    