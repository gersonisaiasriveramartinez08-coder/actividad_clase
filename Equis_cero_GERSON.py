#equis cero con tkinter_gerson_rivera
import tkinter 


#definir las funciones que se van a usar en el juego
def set_tile(row, column):
    global curr_player

    if board[row][column]["text"] != "":
        return

    board[row][column]["text"] = curr_player

    if curr_player == playerX:
        curr_player = playerO
    else:
        curr_player = playerX

    label.config(text=curr_player + "s turn")

    check_winner()





def check_winner():
#ilas
    for row in range(3):
        if board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"] != "":
            label.config(text=board[row][0]["text"] + " wins!")
            disable_buttons()

#columnas
    for column in range(3):
        if board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"] != "":
            label.config(text=board[0][column]["text"] + " wins!")
            disable_buttons()

#estas son las diagonales
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] != "":
        label.config(text=board[0][0]["text"] + " wins!")
        disable_buttons()

    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] != "":
        label.config(text=board[0][2]["text"] + " wins!")
        disable_buttons()


def disable_buttons():
    for row in range(3):
        for column in range(3):
            board[row][column].config(state="disabled")


def new_game():
    global curr_player
    curr_player = playerX
    label.config(text=curr_player + "s turn")

    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", state="normal")


playerX = "X"
playerO = "O"
curr_player = playerX

board = [[0,0,0 ],
         [0,0,0 ],
         [0,0,0] ]


color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"




#aqui creando la ventana y el frame, y el label que muestra de quien es el turno.
window = tkinter.Tk()
window.title("tic tac toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(
    frame, 
    text=curr_player+"s turn", 
    font=("consolas", 20), 
    background=color_gray, 
    foreground="white"
)
label.grid(row=0, column=0, columnspan=3, sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(
            frame,
            text="",
            font=("consolas", 50, "bold"),
            background=color_gray,
            foreground=color_blue,
            width=4,
            height=1,
            command=lambda row=row, column=column: set_tile(row, column)
        )
        board[row][column].grid(row=row+1, column=column)
        
button = tkinter.Button(
    frame,
    text="restart",
    font=("consolas", 20),
    background=color_gray,
    foreground="white",
    command=new_game
)

button.grid(row=4, column=0, columnspan=3, sticky="we")

frame.pack()




#centrar la ventana en la pantalla
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()

#cosas nuevas que aprendi=
#disable_buttons() es una funcion que desactiva los botones del tablero cuando alguien gana.
#new_game() es otra funion para reiniciar el juego.
#check_winner() es la funcion que revisa si alguien gano, osea revisa cada fila, columna y diagonal para ver si hay tres iguales.
#label.config() es una funcion que cambia el texto del label, en este caso para mostrar de quien es el turno o quien gano.
#label_grid() es una funcion que coloca el label en la ventana, en este caso en la fila 0 y columna 0, y ocupa 3 columnas.


#como dato extra, este proyecto lo hice con ayuda de un tutorial de youtube, me ayudo a comprender la logica que hay detras de un equis cero.
#gracias por ver teacher 