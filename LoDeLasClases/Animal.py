class Weapon():
    _dmg = 0

    def __init__(this, dmg):
        this._dmg = dmg

class Hammer(Weapon):
    def __init__(this):
        super().__init__(50)
    

class Creature():
    _name = "Unknown"
    _hp = 0
    
    def __init__(this, name, hp):
        this._name = name
        this._hp = hp

    def take_damage(self, amount):
        self._hp -= amount
        if self._hp < 0:
            self._hp = 0
    


class Ogre(Creature):

    _weapon = "Unknown"

    def __init__(this, name, weapon):
        super().__init__(name, 100)
        if (weapon == "hammer"):
            this._weapon = Hammer()
        else:
            this._weapon = Weapon(3)

    def __str__(this):
        return(f"{this._name} hp: {this._hp} dmg {this._weapon._dmg}")

    def attack(self, target):
        print(f"{self._name} ataca a {target._name} con daño {self._weapon._dmg}")
        target.take_damage(self._weapon._dmg)
        print(f"Estado de {target._name}: {target._hp} hp restantes")


def main():
    ogro1 = Ogre("99ijukip", "hammer")
    ogro2 = Ogre("Kron", "")

    print(ogro1)
    print(ogro2)

    ogro1.attack(ogro2)
    ogro2.attack(ogro1)
    ogro1.attack(ogro2)

main()