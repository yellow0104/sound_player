from tkinter import END, ttk, filedialog
import tkinter as tk
from tkinter import filedialog
import pygame
import shutil
import os





win = tk.Tk()
win.resizable(False, False)
win.title('music player')



listbox = tk.Listbox(win, selectmode='browser', height=10, width=30)

listbox.pack()



add_or_del = False


label_frame = tk.LabelFrame(text='music player')
label_frame.pack()
click_counter = 0

list_tuple = list(listbox.curselection())
if list_tuple == []:
    int_tuple = 0
else:
    int_tuple = list_tuple[0]
def listen_music():

    global click_counter,list_tuple,int_tuple,add_or_del
    print(click_counter)
    

    list_tuple = list(listbox.curselection())
    if list_tuple == []:
        int_tuple = 0
    else:
        if add_or_del == False:
            int_tuple = list_tuple[0]
        elif add_or_del == True:
            print('int_tuple:' + str(int_tuple))
            add_or_del = False
            pass

    
    click_counter += 1
    list_listbox = listbox.get(0, END)




    

    pygame.mixer.init()
    pygame.mixer.music.load('usefulpg/sound_zip/' + list_listbox[int_tuple])


    pygame.mixer.music.play()


    bt_start.config(text='♬')
    if click_counter == 2:
        bt_start.config(text='▶')
        pygame.quit()
        

        print('g')

        click_counter = 0

def importcommand():
    listbox.delete(0, END)
    file_list = os.listdir('usefulpg/sound_zip/')
    for file in file_list:
        listbox.insert(0, file)
importcommand()
def addmusic():
    filenames = filedialog.askopenfilenames(initialdir="/", title="Select file",
                                          filetypes=(("mp3", "*.mp3"),))
    for file in filenames:
        print(file)
        file_name = file.split('/')
        file_name = list(reversed(file_name))[0]
        shutil.move(rf'{file}', rf'usefulpg/sound_zip/{file_name}')
    importcommand()
        
        
def delete_music():
    file_list = os.listdir('usefulpg/sound_zip/')

    list_tuple2 = list(listbox.curselection())
    int_tuple2 = list_tuple2[0]
    os.remove('usefulpg/sound_zip/' + file_list[int_tuple2])
    importcommand()


def add_int_tuple():
    global int_tuple, add_or_del 
    print(int_tuple)
    print('size:' + str(listbox.size()))
    if listbox.size() > int_tuple+1:
        print('h')

        int_tuple += 1
        print(int_tuple)
        listen_music()
        add_or_del = True
        
    else:
        print('f')
def del_int_tuple():
    global int_tuple, add_or_del
    print(int_tuple)
    if int_tuple > 0:
        print('i')
        int_tuple -= 1
        listen_music()
        add_or_del = True
    else:
        print('f')

    

label_frame2 = tk.LabelFrame(text='music add')
label_frame2.pack()

bt_add_music = tk.Button(label_frame2, text='add music', padx=10, pady=10, width=10, command=addmusic)
bt_add_music.pack(side='right')

bt_del_music = tk.Button(label_frame2, text='delete music', padx=10, pady=10, width=10, command=delete_music)
bt_del_music.pack(side='right')

bt_refresh_music = tk.Button(label_frame2, text='refresh', padx=10, pady=10, width=10, command=importcommand)
bt_refresh_music.pack(side='right')





bt_left = tk.Button(label_frame, text='◁', padx=10, pady=10, width=10, command=del_int_tuple)
bt_left.pack(side='left')


bt_right = tk.Button(label_frame, text='▷', padx=10, pady=10, width=10, command=add_int_tuple)
bt_right.pack(side='right')


bt_start = tk.Button(label_frame, text='▶', padx=10, pady=10, width=10, command=listen_music)
bt_start.pack(side='right')




win.mainloop()
