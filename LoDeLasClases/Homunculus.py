import os

os.system("clear")

class Homunculus:
    _name = "Unknown"
    _limbs = 0
    _fingers = 0
    _color = "Unknown"
    _isAlive = False

    def __init__(this, name, limbs, fingers, color):
        this._name = name
        this._limbs =limbs
        this._fingers = fingers
        this._color = color

    def __str__(this):
        if (this._isAlive == False):
            return(f'El humúnculo "{this._name}" no ha cobrado vida aún.')
        else:
            return(f"Hola me llamo {this._name} y tengo {this._limbs} extremidades, {this._fingers} dedos y soy de color {this._color}. ¡Encantado!")

    def __int__(this):
        pass

    def getName(this):
        return (this._name)
    
    def getLimbs(this):
        return (this._limbs)
    
    def getFingers(this):
        return (this._fingers)
    
    def getColor(this):
        return (this._color)
    
    def getIsAlive(this):
        return (this._isAlive)
    
    def setIsAlive(this):
        this._isAlive = True
    
    def setIsAlive(this, boolean):
        this._isAlive = boolean

    def giveLife(this):
        this.setIsAlive(True)

class SkinLess(Homunculus):

    def __init__(this, name, limbs, fingers, color):
        super().__init__(name, limbs, fingers, color)

    def __str__(this):
        if (this._isAlive == False):
            return(f'El humúnculo "{this._name}" no ha cobrado vida aún.')
        else:
            return(f"Hola me llamo {this._name} y tengo {this._limbs} extremidades, {this._fingers} dedos y soy de color {this._color}. ¡Encantado!\nPor cierto, no tengo piel. ¡Jij!")

def main():
    homunA = Homunculus("Eduardo", 6, 100, "morado")
    homunB = SkinLess("Felipe", 3, 0, "amarillo")

    print(homunA)
    homunA.giveLife()
    print(homunA.getIsAlive())
    print(homunA)

    #print(dir(newClass)) # Esto muestra los atributos y métodos de una clase introducida
    print(homunA._color)

    homunB.giveLife()
    print(homunB)

main()
