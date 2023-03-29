import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
BACKGROUND = "#EA5455"
ACTIVE_BACKGROUND = "#F9D2D2"
FONT_COLOR = "#FFFFFF"


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(time_sec):
    start_button.grid_forget()
    root.after(1000, countdown, time_sec - 1)
    minutes, seconds = divmod(time_sec, 60)
    timer = '{:02d}:{:02d}'.format(minutes, seconds)
    countdown_label.config(text=timer)


# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.resizable(False, False)
root.config(background=BACKGROUND)


# --------------------- FRAME CONFIGURATION -----------------------------#

# Toggle settings frame
def settings_click_on():
    main_frame.pack_forget()
    settings_frame.pack()


# Toggle shop frame
def shop_click_on():
    main_frame.pack_forget()
    shop_frame.pack()


# --------------------------- MAIN FRAME SETUP --------------------------------- #
main_frame = tk.Frame(root)
main_frame.pack()
main_frame.config(background=BACKGROUND)

# Images
tomato_image = tk.PhotoImage(file="tomato.png")
settings_image = tk.PhotoImage(file="settings_button.png")
shop_image = tk.PhotoImage(file="shop_button.png")

# Tomato Label
tomato_label = tk.Label(main_frame,
                        image=tomato_image,
                        background=BACKGROUND)
tomato_label.grid(row=0,
                  column=1,
                  sticky='EW',
                  pady=30)

# Countdown Label
countdown_label = tk.Label(main_frame,
                           text="25:00",
                           font=(FONT_NAME, 60),
                           background=BACKGROUND,
                           foreground=FONT_COLOR)
countdown_label.grid(row=1,
                     column=1)

# Start button
start_button = tk.Button(main_frame,
                         text="Start",
                         foreground=BACKGROUND,
                         background=FONT_COLOR,
                         activeforeground=BACKGROUND,
                         activebackground=ACTIVE_BACKGROUND,
                         border=0,
                         width=15,
                         font=(FONT_NAME, 16),
                         command=lambda: countdown(1500))
start_button.grid(row=2,
                  column=1,
                  ipady=5,
                  pady=20)

# Settings Button
settings_button = tk.Button(main_frame,
                            text="",
                            background=BACKGROUND,
                            activeforeground=BACKGROUND,
                            image=settings_image,
                            activebackground=BACKGROUND,
                            border=0,
                            command=settings_click_on)
settings_button.grid(row=3,
                     column=0,
                     sticky='SW',
                     ipadx=20,
                     ipady=20)

# Shop Button
shop_button = tk.Button(main_frame,
                        text="",
                        background=BACKGROUND,
                        activeforeground=BACKGROUND,
                        image=shop_image,
                        activebackground=BACKGROUND,
                        border=0,
                        command=shop_click_on)
shop_button.grid(row=3,
                 column=2,
                 sticky='SE',
                 pady=(40, 0),
                 ipadx=20,
                 ipady=20)


# --------------------------- SETTINGS FRAME SETUP --------------------------------- #
settings_frame = tk.Frame(root)
settings_frame.config(background="#F3F3F3")

# Test Label
test_settings = tk.Label(settings_frame, text="Settings", font=("Arial", 20))
test_settings.pack()


# --------------------------- SHOP FRAME SETUP --------------------------------- #
shop_frame = tk.Frame(root)
shop_frame.config(background="#F3F3F3")

# Test Label
test_shop = tk.Label(shop_frame, text="Shop", font=("Arial", 20))
test_shop.pack()

root.mainloop()
