from tkinter import *
from tkinter import filedialog
root = Tk()
root.title("Mp3 Player")
root.geometry("500x400")
playList=Listbox(root,bg="black",fg="blue",width=60,selectbackground="green",selectforeground="grey")
playList.pack(pady=20)

bck_btn_img=PhotoImage(file="Images/backward.png")
fwd_btn_img=PhotoImage(file="Images/forwards.png")
ply_btn_img=PhotoImage(file="Images/play.png")
ps_btn_img=PhotoImage(file="Images/pause.png")
stp_btn_img=PhotoImage(file="Images/stop.png")

def add_song():
    song = filedialog.askopenfilename(initialdir="audio/" ,filetype=(("mp3 files","*mp3"),))
    song=song.replace("C:/Users/shahw/Desktop/Mp3Player/audio/","")
    song=song.replace(".mp3","")
    playList.insert(END,song)
def add_many_song():
    songs = filedialog.askopenfilenames(initialdir="audio/" ,filetype=(("mp3 files","*mp3"),))
    for song in songs:
        song=song.replace("C:/Users/shahw/Desktop/Mp3Player/audio/","")
        song=song.replace(".mp3","")
        playList.insert(END,song)
def delete_song():
    playList.delete(ANCHOR)
def delete_all_song():
    playList.delete(0,END)
control_frme = Frame(root)
control_frme.pack(pady=20)

back_button=Button(control_frme, image=bck_btn_img, borderwidth=0)
forword_button=Button(control_frme,image=fwd_btn_img ,borderwidth=0)
play_button=Button(control_frme,image=ply_btn_img,borderwidth=0)
pause_button=Button(control_frme,image=ps_btn_img,borderwidth=0)
stop_button=Button(control_frme,image=stp_btn_img,borderwidth=0)

back_button.grid(row=0 , column=0,padx=10)
forword_button.grid(row=0 , column=1,padx=10)
play_button.grid(row=0 , column=2,padx=10)
pause_button.grid(row=0 , column=3,padx=10)
stop_button.grid(row=0 , column=4,padx=10)

my_menu=Menu(root)
root.config(menu=my_menu)

add_song_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Add Song", menu=add_song_menu)

add_song_menu.add_command(label="Add_one_Song", command=add_song)
add_song_menu.add_command(label="Add_Many_Song", command=add_many_song)

delete_song_menu=Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Delete Song", menu=delete_song_menu)
delete_song_menu.add_command(label="Delete a Song",command=delete_song)
delete_song_menu.add_command(label="Delete all Song",command=delete_all_song)

root.mainloop()
