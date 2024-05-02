class Diccionario:
    """
    Clase que representa un diccionario dinámico.
    """

    def __init__(self):
        """
        Inicializa el diccionario.
        """
        self.diccionario = {}

    def agregar_palabra(self, palabra, entradas):
        """
        Agrega una palabra al diccionario con sus entradas.

        Args:
            palabra (str): La palabra que se va a agregar.
            entradas (dict): Un diccionario que contiene las entradas de la palabra.

        Returns:
            None
        """
        self.diccionario[palabra] = entradas

    def mostrar_palabras(self):
        """
        Muestra todas las palabras del diccionario.

        Returns:
            None
        """
        for palabra in self.diccionario:
            print(palabra)

    def mostrar_entradas(self, palabra):
        """
        Muestra todas las entradas de una palabra específica.

        Args:
            palabra (str): La palabra de la que se mostrarán las entradas.

        Returns:
            None
        """
        if palabra in self.diccionario:
            entradas = self.diccionario[palabra]
            for entrada, definicion in entradas.items():
                print(f"{entrada}: {definicion}")
        else:
            print("La palabra no está en el diccionario.")

    def modificar_contenido(self, palabra, entradas_nuevas):
        """
        Modifica el contenido de una palabra en el diccionario.

        Args:
            palabra (str): La palabra cuyo contenido se va a modificar.
            entradas_nuevas (dict): Un diccionario que contiene las nuevas entradas de la palabra.

        Returns:
            None
        """
        if palabra in self.diccionario:
            self.diccionario[palabra].update(entradas_nuevas)
        else:
            print("La palabra no está en el diccionario.")

    def eliminar_contenido(self, palabra, entrada):
        """
        Elimina una entrada específica de una palabra en el diccionario.

        Args:
            palabra (str): La palabra de la que se va a eliminar una entrada.
            entrada (str): La entrada que se va a eliminar.

        Returns:
            None
        """
        if palabra in self.diccionario:
            if entrada in self.diccionario[palabra]:
                del self.diccionario[palabra][entrada]
            else:
                print("La entrada no está en la palabra.")
        else:
            print("La palabra no está en el diccionario.")
