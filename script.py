from board import *
import sbs

class TicTacToe:
    missionState = "blank"
    board = Board()

    def render(sim):
        state =  TicTacToe.board.check_winner()

        if state == EndGame.UNKNOWN:
            sbs.send_gui_clear(0)
            TicTacToe.missionState = "mission_options"
            for index, p in enumerate(TicTacToe.board.grid):
                x = (index % 3) * 10 + 30
                y = index//3  * 10 + 30
                if p == Turn.X_TURN:
                    sbs.send_gui_text(0, "X", f"x{index+1}", x, y, x+10,y+10)
                elif p == Turn.O_TURN:
                    sbs.send_gui_text(0, "O", f"o{index+1}", x, y, x+10,y+10)
                else:
                    sbs.send_gui_button(0, f"{index+1}", f"{index}", x, y, x+10,y+10)
        elif state == EndGame.X_WINS:
            sbs.send_gui_clear(0)
            sbs.send_gui_text(0, "X WINS ", "text", 50, 50, 60,60)
            sbs.send_gui_button(0, f"Play Again", f"replay", 80, 80, 90,90)
        elif state == EndGame.O_WINS:
            sbs.send_gui_clear(0)
            sbs.send_gui_text(0, "O WINS ", "text", 50, 50, 60,60)
            sbs.send_gui_button(0, f"Play Again", f"replay", 80, 80, 90,90)
        elif state == EndGame.DRAW:
            sbs.send_gui_clear(0)
            sbs.send_gui_text(0, "DRAW", "text", 50, 50, 60,60)
            sbs.send_gui_button(0, f"Play Again", f"replay", 80, 80, 90,90)



    def update(sim , message_tag, clientID):
        if "replay" == message_tag:
            TicTacToe.board.clear()
        else:
            slot = int(message_tag)
            TicTacToe.board.set_grid(slot)



def  HandlePresentGUI(sim):
    TicTacToe.render(sim)

########################################################################################################
def  HandlePresentGUIMessage(sim, message_tag, clientID):
    TicTacToe.update(sim, message_tag, clientID)