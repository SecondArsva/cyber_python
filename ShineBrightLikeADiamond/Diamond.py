# Crear clase padre Vehículo herencia, marca, modelo, color, arrancado, parado. Método resumen que muestra los atributos. metodos arrancar y parar.
# Clase concreta que sea Moto, atributo cadenado, metodo ponerCadenado(bool = True)
# Clase concreta que hereda de Moto. No contiene nada adicional.
# Clase padre VehículoEléctrico, attr voltaje, carga rapida bool, metodo muestra de voltaje.
# Otra clase que herede de vehiculo y vehículo eléctrico.

class Vehículo():
    marca = "Unknown"
    modelo = "Unknown"
    color = "Unknown"
    arrancado = False
    apagado = True

    def __init__(this, marca, modelo, color):
        this.marca = marca
        this.modelo = modelo
        this.color = color

    def resumen(this):
        print(f"Marca: {this.marca}\nModelo: {this.modelo}\nColor: {this.color}\nArrancado: {this.arrancado}")

    def arrancar(this):
        this.arrancado = True
        this.apagado = False

    def arrancar(this):
        this.arrancado = False
        this.apagado = True

    def estado(this):
        if (this.arrancado == True):
            return ("Si")
        else:
            return ("No")

class Moto(Vehículo):
    cadenado = False

    def __init__(this, marca, modelo, color):
        super().__init__(marca, modelo, color)

    def resumen(this):
        Vehículo.resumen(this)
        print(f"Cadenado: {this.cadenado}")

    def ponerCadenado(this):
        this.cadenado = True

class Model001(Moto):
    pass

class VehículoEléctrico():
    marca = "Unknown"
    modelo = "Unknown"
    color = "Unknown"
    voltaje = 0
    cargaRápida = False

    def __init__(this, marca, modelo, color, voltaje, cargaRápida):
        this.voltaje = voltaje
        this.cargaRápida = cargaRápida
    
    def resumen(this):
        print(f"Marca: {this.marca}\nModelo: {this.modelo}\nColor: {this.color}\nVoltaje: {this.getVoltaje}\nCarga Rápida: {this.cargaRápida}")

    def getVoltaje(this):
        return (this.voltaje)

class Diamante(Vehículo, VehículoEléctrico):
    pass

def main():
    coche = Vehículo("Metal Gear", "Rex", "Gris")
    moto = Moto("Metal Gear", "Walker", "Gris oscuro")

    print(f"{coche.resumen()}")
    print(f"{moto.resumen()}")

main()
