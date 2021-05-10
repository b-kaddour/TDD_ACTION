"""
Module bouteille.py
"""


class Bouteille:
    """
    Class Bouteille
    """

    def __init__(self, name, quantity_max, durability):
        self.name = name
        self.quantity_max = quantity_max
        self.quantity = 0
        self.durability = durability

    def __str__(self):
        return f"[Bouteille : {self.name} d'une contenance de {self.quantity_max} qui contient {self.quantity} litre et d'une durabilité de {self.durability}"

    def fill_in(self, how_many):
        """
        Action de remplir le contenant
        :param how_many:
        :return true/false:
        """
        # Durabilité?
        if self.durability > 0:
            # Contenant n'est pas déjà plein ?
            if self.quantity != self.quantity_max:
                self.quantity += how_many
                # ça déborde ?
                if self.quantity > self.quantity_max:
                    self.durability -= 0.5
                    how_many = self.quantity_max - self.quantity
                    self.quantity = self.quantity_max
                    # On prévient tout de même
                    if how_many > 1:
                        print(f'{how_many}L ont été perdu car la bouteille ne pouvait pas en contenir plus ')
                    else:
                        print(f'{how_many}L a été perdu car la bouteille ne pouvait pas en contenir plus ')
                    return True
            else:
                print(f'{self.name} déjà pleine !')
                return False
        else:
            print(f'{self.name} est cassé(e)')
            return False

    def drink(self, how_many):
        """
        Action de boire le contenu du contenant
        :param how_many:
        :return true / false:
        """
        # Durabilité ?
        if self.durability > 0:
            if self.quantity > 0:
                self.durability -= 1
                if how_many > self.quantity:
                    return False
                else:
                    self.quantity -= how_many
                    return True
            else:
                print('Boisson vide !')
                return False

        else:
            print(f'{self.name} est cassé(e)')
            return False