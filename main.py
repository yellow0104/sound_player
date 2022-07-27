from tkinter import END, ttk, filedialog
import tkinter as tk
from tkinter import filedialog
import pygame



win = tk.Tk()
win.resizable(False, False)
win.title('music player')



listbox = tk.Listbox(win, selectmode='browser', height=10, width=30)

listbox.pack()





label_frame = tk.LabelFrame(text='music player')
label_frame.pack()
click_counter = 0

list_tuple = list(listbox.curselection())
if list_tuple == []:
    int_tuple = 0
else:
    int_tuple = list_tuple[0]
def listen_music():

    global click_counter,list_tuple,int_tuple
    print(click_counter)
    
    click_counter += 1
    list_listbox = listbox.get(0, END)




    

    pygame.mixer.init()
    pygame.mixer.music.load(list_listbox[int_tuple])


    pygame.mixer.music.play()


    bt_start.config(text='♬')
    if click_counter == 2:
        bt_start.config(text='▶')
        pygame.quit()
        

        print('g')

        click_counter = 0


def addmusic():
    filenames = filedialog.askopenfilenames(initialdir="/", title="Select file",
                                          filetypes=(("mp3", "*.mp3"),))
    for file in filenames:
        listbox.insert(0, file)
def delete_music():
    list_tuple2 = list(listbox.curselection())
    int_tuple2 = list_tuple2[0]
    listbox.delete(int_tuple2)

def add_int_tuple():
    global int_tuple
    print(int_tuple)
    if listbox.size() > int_tuple:
        int_tuple += 1
        listen_music()
def del_int_tuple():
    global int_tuple
    print(int_tuple)
    if int_tuple > 0:
        int_tuple -= 1
        listen_music()

    

label_frame2 = tk.LabelFrame(text='music add')
label_frame2.pack()

bt_add_music = tk.Button(label_frame2, text='add music', padx=10, pady=10, width=10, command=addmusic)
bt_add_music.pack(side='right')

bt_del_music = tk.Button(label_frame2, text='delete music', padx=10, pady=10, width=10, command=delete_music)
bt_del_music.pack(side='right')





bt_left = tk.Button(label_frame, text='◁', padx=10, pady=10, width=10, command=del_int_tuple)
bt_left.pack(side='left')


bt_right = tk.Button(label_frame, text='▷', padx=10, pady=10, width=10, command=add_int_tuple)
bt_right.pack(side='right')


bt_start = tk.Button(label_frame, text='▶', padx=10, pady=10, width=10, command=listen_music)
bt_start.pack(side='right')




win.mainloop()