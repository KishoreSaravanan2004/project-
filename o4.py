import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import random
import tkinter.messagebox as tmsg

app = Tk()
count = 0
comp = 0

def generate():
    global comp
    comp = random.randint(1, 100)

def result():
    global count
    number = userv.get()
    if not number:
        tmsg.showerror('Error', "Please enter a value")
        return
    try:
        n = int(number)
    except ValueError:
        tmsg.showerror('Error', "Invalid input! Enter a number.")
        return

    count += 1
    if count == 10:
        tmsg.showinfo('Game Over', 'You lose the Game!')
        generate()
        count = 0
        show.config(text='😵 You Lost! Try again.' )
        again = tmsg.askyesno("Play Again?", "Do you want to play another round?")
        if again:
            generate()
            count = 0
            userv.set('')
            show.config(text='🎯 New round started!\nGive it another shot! 💪', fg='blue')
        else:
            app.quit()
    elif comp == n:
        score = 11 - count
        tmsg.showinfo('🎉 Win', f'You guessed the right number!\nYour score: {score}')
        show.config(text='✅ You Win! 🥳', fg='green')
        with open('score.txt', 'w') as f:
            f.write(str(score))
        generate()
        tmsg.showinfo('Next Number', 'Click OK to guess another number')
        count = 0
    elif comp > n:
        show.config(text='📉 Too Low 🤏', fg='red')
    else:
        show.config(text='📈 Too High 😅', fg='red')

def restart():
    global count
    count = 0
    generate()
    userv.set('')
    show.config(text='Game restarted! Try a new number 🤗', fg='blue')
    tmsg.showinfo('Reset', "Game reset!")

def call1():
    tmsg.showinfo('About', '🎮 This game is developed by Harini 💖\n\nAll rights reserved ©')

def setup_ui():
    app.title("Number Guessing Game")
    app.geometry("500x600")
    app.configure(bg="#fdf6e3")

    try:
        icon_img = ImageTk.PhotoImage(Image.open("guess.jpeg"))
        app.iconphoto(False, icon_img)
    except Exception as e:
        print("Warning: Could not load icon image:", e)

    Label(app, text='🎯 Number Guessing Game 🎯', font="Helvetica 18 bold",
          bg='#fdf6e3', fg='#333').pack(pady=15)

    # High Score
    global hg, userv
    userv = StringVar()
    try:
        with open('score.txt', 'r') as f:
            hg = f.read()
    except:
        hg = "0"

    hg = hg if hg.isdigit() else "0"
    hg = int(hg)
    hg = max(0, hg)

    Label(app, text=f'🏆 Previous High Score: {hg}', font='Helvetica 10 bold',
          bg='#fdf6e3', fg='#4c4c4c').pack(anchor=E, padx=25, pady=5)

    generate()

    # Entry field
    Label(app, text="Enter your guess (1-100):", font="Helvetica 14",
          bg='#fdf6e3', fg='#4c4c4c').pack(pady=5)

    Entry(app, textvariable=userv, justify=CENTER, relief=FLAT,
          font='Helvetica 18 bold', bg='#e6b019', fg='#333').pack(pady=10)

    # Game Image
    try:
        img1 = Image.open('harini/guess.jpeg')
        img1 = img1.resize((180, 140), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img1)
        logo = Label(app, image=img, bg="#000000")
        logo.image = img
        logo.pack(pady=20)
    except Exception as e:
        print("Logo image failed to load:", e)

    # Submit Button
    try:
        curved_img = Image.open('harini/curved_button.png')
        curved_img = curved_img.resize((150, 50), Image.ANTIALIAS)
        curved_photo = ImageTk.PhotoImage(curved_img)
        submit = Button(app, image=curved_photo, command=result,
                        borderwidth=0, relief=FLAT, bg="#fdf6e3", activebackground='#fdf6e3')
        submit.image = curved_photo
        submit.pack(pady=10)
    except Exception as e:
        print("Could not load curved_button.png:", e)
        Button(app, text="Submit", command=result,
               font='Helvetica 14 bold', relief=GROOVE, bg='#80cbc4', fg='#4c4c4c').pack(pady=10)

    # Result Label
    global show
    show = Label(app, text=' Hii Buddies🦋\n Ready to play! 🎲', font='Helvetica 12 bold',
                 bg='#fdf6e3', fg='#4c4c4c')
    show.pack(pady=10)

    # Footer
    Label(app, text='💖 Developed by Harini 💖', font="Helvetica 14 italic",
          bg='#fdf6e3', fg='tomato').pack(side=BOTTOM, pady=10)

    # Menu Bar with dropdowns
    mymenu = Menu(app)

    # Start Menu
    start_menu = Menu(mymenu, tearoff=0)
    start_menu.add_command(label='Restart', command=restart)
    start_menu.add_separator()
    start_menu.add_command(label='Quit', command=app.quit)
    mymenu.add_cascade(label='Start', menu=start_menu)

    # Options Menu (placeholder)
    options_menu = Menu(mymenu, tearoff=0)
    options_menu.add_command(label='Sound: Coming Soon')
    options_menu.add_command(label='Difficulty: Coming Soon')
    mymenu.add_cascade(label='Options', menu=options_menu)

    # Tools Menu
    tools_menu = Menu(mymenu, tearoff=0)
    tools_menu.add_command(label=f'High Score: {hg}')
    mymenu.add_cascade(label='Tools', menu=tools_menu)

    # About Menu
    about_menu = Menu(mymenu, tearoff=0)
    about_menu.add_command(label='About Game', command=call1)
    mymenu.add_cascade(label='About', menu=about_menu)

    app.config(menu=mymenu)

# Run the app
setup_ui()
app.mainloop()
