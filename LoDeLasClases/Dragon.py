import os

class Dragon():
    __name = "Unknown"
    __dragonType = "Unknown"
    __age = 0

    def __init__(this, name, dragonType, age):
        this.__name = name
        this.__dragonType = dragonType
        this.__age = age

    def getName(this):
        return (this.__name)
    def getAge(this):
        return (this.__age)
    def getDragonType(this):
        return (this.__dragonType)
    def categorizeByAge(this):
        if (this.__age < 50):
            return ("infante")
        if (this.__age > 250):
            return ("anciano")
        else:
            return ("adulto")
    
    def __str__(this):
        return(f"{this.__name}: Dragón {this.categorizeByAge()} de tipo {this.__dragonType}")

def main():
    os.system("clear")
    paarthurnax = Dragon("Paarthurnax", "Greybeard", 7000)
    desdentao = Dragon("Desdentao'", "Furia Nocturna", 15)

    print(paarthurnax)
    print(desdentao)

main()
