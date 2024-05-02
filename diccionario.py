class Diccionario:
    """
    Clase per definir un diccionari.
    """

    def __init__(self):
        """
        Inicialitzem el diccionari i cridem la instància de la clase de diccionari
        """
        self.vocabulario = {}

    def agregar_palabra(self, paraula, entrada):
        """
        Funció per afegir paraules al diccionari vinculades a una entrada.

        Variables:
        paraula (string): La palabra que s'introduirà.
        entrada (string): La entrada que fa referència a la paraula, com una descripció..
        """
        if paraula in self.vocabulario:
            self.vocabulario[paraula].append(entrada)
        else:
            self.vocabulario[paraula] = [entrada]

    def mostrar_palabras(self):
        """
        Mostra les paraules que has introduit en el sistema dle diccionari.
        """
        print("Paraules actuals del diccionari:")
        for paraula in self.vocabulario:
            print("--> ", paraula)

    def mostrar_entradas(self, paraula):
        """
        Mostra les paraules amb la seva 

        Variables:
        paraula (string): La palabra de la cual mostrar las entradas.
        """
        if paraula in self.vocabulario:
            print("Entrades per la paraula '{}' :".format(paraula))
            for entrada in self.vocabulario[paraula]:
                print("-", entrada)
        else:
            print("La paraula '{}' no hi és en el diccionari, prova un altre.".format(paraula))

    def modificar_entrada(self, paraula, i, novaEntrada):
        """
        Selecciona una entrada mitjançant l'index i demana la nova entrada.

        Variables:
        paraula (string): Paraula que vols modificar
        i (integer): Index de l'entrada.
        novaEntrada (string): La nova entrada a introduir al sistema dle diccionari.
        """
        if paraula in self.vocabulario and i < len(self.vocabulario[paraula]):
            self.vocabulario[paraula][i] = novaEntrada
            print("La entrada '{}' per la paraula '{}' ha sigut modificada amb èxit.".format(novaEntrada, paraula))
        else:
            print("No s'ha pogut modificar la entrada. La paraula '{}' no existeix".format(paraula))

    def eliminar_paraula(self, paraula):
        """
        Elimina una paraula amb la seva entrada corresponent.

        Parameters:
        paraula (string): La palabra que vols suprimir.
        """
        if paraula in self.vocabulario:
            del self.vocabulario[paraula]
            print("La palabra '{}' ha sigut suprimida amb èxit.".format(paraula))
        else:
            print("La palabra '{}' no hi és en el diccionari.".format(paraula))

    def eliminar_entrada(self, paraula, i):
        """
        Elimina una entrada introduida mitjançant un index buscant la posició.

        Parameters:
        paraula (string): La paraula que conté la entrada.
        i (integer): L'index on es troba l'entrada.
        """
        if paraula in self.vocabulario and i < len(self.vocabulario[paraula]):
            del self.vocabulario[paraula][i]
            print("La entrada en la posició {} per la paraula '{}' ha sigut suprimida amb èxit.".format(i, paraula))
        else:
            print("No s'ha pogut eliminar l'entrada. La paraula '{}' no existeix.".format(paraula))



