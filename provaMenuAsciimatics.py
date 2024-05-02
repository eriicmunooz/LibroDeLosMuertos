#Josep he intentat fer el menu amb la llibreria d'asciimatics però quan presiono la tecla per seleccionar una de les opcions del menu s'hem queda pillat.
#He buscat per tot arreu i no he pogut trobar la solució, et deixo el codi que he fet per si te'l vols mirar.

from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Print
from asciimatics.renderers import FigletText
from asciimatics.exceptions import ResizeScreenError, StopApplication
from diccionario import Diccionario

class Menu:
    def __init__(self):
        self.diccionario = Diccionario()

    def mostrar_menu(self, screen):
        while True:
            screen.clear()
            effects = [Print(screen, FigletText("El llibre de les Accepcions", font='big'), int(screen.height / 2 - 14))]
            menu_options = [
                "1. Afegir entrada",
                "2. Mostrar entrada",
                "3. Modificar entrada",
                "4. Eliminar entrada",
                "q. Sortir"
            ]
            for i, option in enumerate(menu_options):
                effects.append(Print(screen, FigletText(option, font='small'), int(screen.height / 2 - 6 + i * 4))) #i * 4 per fer mes ampli la separació de les opcions
            screen.play([Scene(effects, -1)])

            event = screen.get_event()
            if event:
                if event.key_code in [ord('q'), ord('Q')]:
                    raise StopApplication("User requested exit")
                elif event.key_code == ord('1'):
                    self.afegir_entrada()
                elif event.key_code == ord('2'):
                    self.mostrar_entrada()
                elif event.key_code == ord('3'):
                    self.modificar_entrada()
                elif event.key_code == ord('4'):
                    self.eliminar_entrada()
                screen.refresh()

    def run(self):
        try:
            Screen.wrapper(self.mostrar_menu)
        except ResizeScreenError:
            pass
        except StopApplication:
            pass

    # Remaining methods are unchanged

if __name__ == "__main__":
    menu = Menu()
    menu.run()