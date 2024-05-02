from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Print
from asciimatics.renderers import FigletText
from asciimatics.exceptions import ResizeScreenError


class DiccionarioUI:
    def __init__(self):
        self.diccionario = {}

    def portada(self, screen):
        title = FigletText("El Llibre de les Accepcions", font='big')
        effects = [Print(screen, title, screen.height // 2 - 5, align="center")]
        screen.play([Scene(effects)], stop_on_resize=True)

    def mostrar_menu(self, screen):
        menu = FigletText("Menú", font='small')
        options = ["1. Afegir entrada", "2. Mostrar entrada", "3. Modificar entrada", "4. Eliminar entrada"]
        menu_effects = [Print(screen, menu, screen.height // 2 - 5, align="center")]
        for i, option in enumerate(options):
            menu_effects.append(Print(screen, FigletText(option, font='small'), screen.height // 2 - 5 + i + 2, align="center"))
        screen.play([Scene(menu_effects)], stop_on_resize=True)

    def run(self):
        while True:
            try:
                Screen.wrapper(self.portada)
                Screen.wrapper(self.mostrar_menu)
                event = Screen.wrapper(self._get_event)
                if event == ord('1'):
                    self.afegir_entrada()
                elif event == ord('2'):
                    self.mostrar_entrada()
                elif event == ord('3'):
                    self.modificar_entrada()
                elif event == ord('4'):
                    self.eliminar_entrada()
                elif event == ord('q'):
                    break
            except ResizeScreenError:
                pass

    def _get_event(self, screen):
        return screen.get_event()

    def afegir_entrada(self):
        pass

    def mostrar_entrada(self):
        pass

    def modificar_entrada(self):
        pass

    def eliminar_entrada(self):
        pass


if __name__ == "__main__":
    diccionario_ui = DiccionarioUI()
    diccionario_ui.run()
