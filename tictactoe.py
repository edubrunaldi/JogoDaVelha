from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty, NumericProperty
from kivy.uix.modalview import ModalView
from kivy.uix.label import Label
import random
'''
Este codigo permanece original do site
Parte deste codigo foi tirado do site :
http://cadernodelaboratorio.com.br/2016/05/14/jogo-da-velha-em-kivy-agora-o-computador-joga-com-voce/
Pois o foco não está na implementação do jogo, mas sim na implementação do servidor
As alterações foram:
    -Botao para se conectar com outro jogador
    -Botao para jogar contra ia
        -Tirar a IA do codigo geral para que o jogo busque o comando da IA no servidor

 '''

class GridEntry(Button):
    coords = ListProperty([0, 0])


class TicTacToeGrid(GridLayout):
    status = ListProperty([0, 0, 0,
                           0, 0, 0,
                           0, 0, 0])

    curret_player = NumericProperty(1)

    def __init__(self, *args, **kwargs):
        super(TicTacToeGrid, self).__init__(*args, **kwargs)

        # =======================================================================
        # for row in range(3):
        #     for column in range(3):
        #         grid_entry = GridEntry(
        #                                coords=(row, column))
        #
        #         grid_entry.bind(on_release=self.button_pressed)
        #         self.add_widget(grid_entry)
        # =======================================================================

    def button_pressed(self, button):
        player = {1: "O", -1: "X"}
        colours = {1: (1, 0, 0, 1), -1: (0, 1, 0, 1)}

        row, column = button.coords

        status_index = 3 * row + column
        print(row, column)
        print(status_index)
        self.already_played = self.status[status_index]

        if not self.already_played:
            self.status[status_index] = self.curret_player
            button.text = player[self.curret_player]
            button.background_color = colours[self.curret_player]

            self.curret_player *= -1

        if self.curret_player == -1 and not self.winner:
            self.ai_pressed()
            # self.ai_comprobar()

    def ai_pressed(self):

        player = {1: "O", -1: "X"}
        colours = {1: (1, 0, 0, 1), -1: (0, 1, 0, 1)}

        row, column = self.ai_comprobar()

        # =======================================================================
        # if self.ya_jugado:
        #     self.row_ia, self.column_ia = random.randint(0,2), random.randint(0,2)
        #     self.ya_jugado = False
        #     print "a"
        #      #Hay que poner row y column con self, para
        #     #acceder desde cualquier lugar
        # =======================================================================

        self.status_index = 3 * row + column
        button = self.children[-(self.status_index + 1)]
        self.already_played = self.status[self.status_index]

        if not self.already_played:
            self.status[self.status_index] = self.curret_player
            button.text = player[self.curret_player]
            button.background_color = colours[self.curret_player]
            self.curret_player *= -1

        if self.already_played and not self.winner:
            self.ai_pressed()

    def ai_comprobar(self):
        status = self.status

        lista = [status[0:3],
                 status[3:6],
                 status[6:9],
                 status[0::3],
                 status[1::3],
                 status[2::3],
                 status[::4],
                 status[2:-2:2]]

        # Colocar -2 y comentar el "if" = Modo muy facil
        # Colocar un -2 y no comentar el "if" y ponerlo en -1 = Modo facil
        # Colocar 2 y comentar el "if" = Modo normal
        # Colocar -2 y no comentar el "if" y ponerlo en 2 = Modo dificil

        row, column = self.colocar_numero(-2, lista)
        if row == None and column == None:
            row, column = self.colocar_numero(2, lista)

        if row != None and column != None:
            return row, column
        else:
            row, column = random.randint(0, 2), random.randint(0, 2)
            return row, column

    def colocar_numero(self, resultado, lista):
        for x in range(len(lista)):
            if sum(lista[x]) == resultado:
                print(sum(lista[x]), x)
                # print "con numero", resultado
                if x == 0:
                    # print 0, 1, 2

                    for pos in range(len(lista[x])):
                        if lista[x][pos] == 0 and not self.already_played:
                            print("poner aqui", 0, pos)
                            return 0, pos

                elif x == 1:
                    # print 3, 4, 5

                    for pos in range(len(lista[x])):
                        if lista[x][pos] == 0 and not self.already_played:
                            print("poner aqui", 1, pos)
                            return 1, pos

                elif x == 2:
                    # print 6, 7, 8

                    for pos in range(len(lista[x])):
                        if lista[x][pos] == 0 and not self.already_played:
                            print("poner aqui", 2, pos)
                            return 2, pos

                elif x == 3:
                    # print 0, 3, 6

                    for pos in range(len(lista[x])):
                        if lista[x][pos] == 0 and not self.already_played:
                            print("poner aqui", pos, 0)
                            return pos, 0

                elif x == 4:
                    # print 1, 4, 7

                    for pos in range(len(lista[x])):
                        if lista[x][pos] == 0 and not self.already_played:
                            print("poner aqui", pos, 1)
                            return pos, 1

                elif x == 5:
                    # print 2, 5, 8

                    for pos in range(len(lista[x])):
                        if lista[x][pos] == 0 and not self.already_played:
                            print("poner aqui", pos, 2)
                            return pos, 2

                elif x == 6:
                    # print 0, 4, 8

                    for pos in range(len(lista[x])):
                        if lista[x][pos] == 0 and not self.already_played:
                            print("poner aqui", pos, pos)
                            return pos, pos

                elif x == 7:
                    # print 2, 4, 6

                    for pos in range(len(lista[x])):
                        if lista[x][pos] == 0:
                            if pos == 0 and not self.already_played:
                                print("poner aqui", 0, 2)
                                return 0, 2
                            elif pos == 1 and not self.already_played:
                                print("poner aqui", 1, 1)
                                return 1, 1
                            elif pos == 2 and not self.already_played:
                                print("poner aqui", 2, 0)
                                return 2, 0
        print("ninguno se cumplio")
        return None, None

    def on_status(self, instance, new_value):
        status = new_value

        sums = [sum(status[0:3]),
                sum(status[3:6]),
                sum(status[6:9]),
                sum(status[0::3]),
                sum(status[1::3]),
                sum(status[2::3]),
                sum(status[::4]),
                sum(status[2:-2:2])]

        self.winner = None

        if 3 in sums:
            self.winner = "Os win!"
        elif -3 in sums:
            self.winner = "Xs win!"
        elif 0 not in self.status:
            self.winner = 'Draw...nobody wins!'

        if self.winner:
            popup = ModalView(size_hint=(0.75, 0.5))
            victory_label = Label(text=self.winner, font_size=50)
            popup.add_widget(victory_label)
            popup.bind(on_dismiss=self.reset)
            popup.open()

    # ===========================================================================
    # def on_status_ai(self):
    #     status = self.status
    #
    #     sums = [sum(status[0:3]),
    #             sum(status[3:6]),
    #             sum(status[6:9]),
    #             sum(status[0::3]),
    #             sum(status[1::3]),
    #             sum(status[2::3]),
    #             sum(status[::4]),
    #             sum(status[2:-2:2])]
    #
    #     winner = None
    #
    #     if 3 in sums:
    #         winner = "Os win!"
    #     elif -3 in sums:
    #         winner = "Xs win!"
    #     elif 0 not in self.status:
    #         winner = 'Draw...nobody wins!'
    #
    #     if winner:
    #         popup = ModalView(size_hint=(0.75,0.5))
    #         victory_label = Label(text=winner, font_size=50)
    #         popup.add_widget(victory_label)
    #         popup.bind(on_dismiss=self.reset)
    #         popup.open()
    # ===========================================================================

    def reset(self, *args):
        self.status = [0 for _ in range(9)]

        for child in self.children:
            child.text = ""
            child.background_color = (1, 1, 1, 1)

        self.curret_player = 1


class TicTacToeApp(App):
    def build(self):
        return TicTacToeGrid()


if __name__ == "__main__":
    TicTacToeApp().run()