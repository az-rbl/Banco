import threading

class cuenta():
    def __init__(self, no_cuenta, saldo =0) -> None:
         self.no_cuenta = no_cuenta
         self.saldo = saldo
         self.lock = threading.Lock()
         
    def __str__(self):
        return f"Numero de cuenta: {self.no_cuenta}, Saldo: {self.saldo}"
         
    def retiro(self, cantidad):
        with self.lock:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
            else:
                print("saldo insuficiente")
                return -1
        
    def deposito(self, cantidad):
        with self.lock:
            self.saldo += cantidad
    
    def transferencia(self,cuenta_deposito, cantidad):
        e=self.retiro(cantidad)
        if e!=-1:
            cuenta_deposito.deposito(cantidad)
        print(self, cuenta_deposito)
        
        
def realizar_deposito(cuenta, cantidad):
    cuenta.deposito(cantidad)
    
def realizar_retiro(cuenta, cantidad):
    cuenta.retiro(cantidad)
    
def realizar_transferencia(cuenta, destino, cantidad):
    cuenta.transferencia(destino,cantidad)    


if __name__=='__main__':
    cuentas={"C123":cuenta("C123", 1000),"C124":cuenta("C124", 100), "C125":cuenta("C125", 100)}
    
    threads = []
    for _ in range(5):
        t = threading.Thread(target=realizar_transferencia, args=(cuentas["C123"], cuentas["C124"], 100))
        threads.append(t)
        t.start()


    for t in threads:
        t.join()
        
