import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
BACKGROUND = "#EA5455"
ACTIVE_BACKGROUND = "#F9D2D2"
FONT_COLOR = "#FFFFFF"


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(time_sec):
    # Label change
    start_button.config(text="Focus time",
                        background=BACKGROUND,
                        foreground=FONT_COLOR,
                        activebackground=BACKGROUND,
                        activeforeground=FONT_COLOR,
                        command='')
    shop_button.config(image='')
    settings_button.config(image='')

    # Countdown configuration
    counter = root.after(1000, countdown, time_sec - 1)
    minutes, seconds = divmod(time_sec, 60)
    timer = '{:02d}:{:02d}'.format(minutes, seconds)
    countdown_label.config(text=timer)

    # When timer is gone
    if time_sec == 0:
        root.after_cancel(counter)
        break_countdown(break_interval.get() * 60)


def break_countdown(time_sec):
    # Countdown configuration
    counter = root.after(1000, break_countdown, time_sec - 1)
    minutes, seconds = divmod(time_sec, 60)
    timer = '{:02d}:{:02d}'.format(minutes, seconds)

    # Label change
    start_button.config(text="Take a break")
    countdown_label.config(text=timer)

    # When timer is gone
    if time_sec == 0:
        root.after_cancel(counter)

        # Label change
        countdown_label.config(text=work_interval.get())
        start_button.config(text="Start",
                            background=FONT_COLOR,
                            foreground=BACKGROUND,
                            activebackground=ACTIVE_BACKGROUND,
                            command=lambda: countdown(work_interval.get() * 60))
        shop_button.config(image=shop_image)
        settings_button.config(image=settings_image)


# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.resizable(False, False)
root.geometry("400x600")
root.config(background=BACKGROUND)

# ---------------------------- SETTINGS --------------------------------- #
work_interval = tk.IntVar(value=1)
break_interval = tk.IntVar(value=1)
points = tk.IntVar(value=0)


# --------------------- FRAME CONFIGURATION -----------------------------#

# settings frame on/off
def settings_click_on():
    main_frame.pack_forget()
    settings_frame.pack()


def settings_click_off():
    settings_frame.pack_forget()
    main_frame.pack()
    countdown_label.config(text=f"{work_interval.get()}:00")


# shop frame on/off
def shop_click_on():
    main_frame.pack_forget()
    shop_frame.pack()


def shop_click_off():
    shop_frame.pack_forget()
    main_frame.pack()


def time_label_update(time_sec):
    minutes, seconds = divmod(time_sec, 60)
    timer = '{:02d}:{:02d}'.format(minutes, seconds)
    countdown_label.config(text=timer)


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
                           text=f"{work_interval.get()}:00",
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
                         command=lambda: countdown(work_interval.get() * 60))
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
settings_frame = tk.Frame(root, width=400, height=600)
settings_frame.config(background=BACKGROUND)

# Images
close_image = tk.PhotoImage(file="close_button.png")

# Work length label
work_length_label = tk.Label(settings_frame,
                             text="Work Interval",
                             font=(FONT_NAME, 16),
                             foreground=FONT_COLOR,
                             background=BACKGROUND)
work_length_label.grid(row=1,
                       column=0,
                       pady=(100, 0))

work_length_spinbox = tk.Spinbox(settings_frame,
                                 from_=1,
                                 to=180,
                                 width=5,
                                 textvariable=work_interval,
                                 command=lambda: print(work_interval.get()))
work_length_spinbox.grid(row=1,
                         column=1,
                         padx=40,
                         sticky='s')

# Break length label
break_length_label = tk.Label(settings_frame,
                              text="Break",
                              font=(FONT_NAME, 16),
                              foreground=FONT_COLOR,
                              background=BACKGROUND)
break_length_label.grid(row=2, column=0, sticky='W')

break_length_spinbox = tk.Spinbox(settings_frame,
                                  from_=1,
                                  to=15,
                                  width=5,
                                  textvariable=break_interval,
                                  command=lambda: time_label_update(work_interval.get()))
break_length_spinbox.grid(row=2, column=1)

# Close button
settings_close_button = tk.Button(settings_frame,
                                  text="",
                                  image=close_image,
                                  background=BACKGROUND,
                                  border=0,
                                  activebackground=BACKGROUND,
                                  activeforeground=BACKGROUND,
                                  command=settings_click_off)

settings_close_button.grid(row=3,
                           column=0,
                           sticky='E',
                           pady=(330, 0))

# --------------------------- SHOP FRAME SETUP --------------------------------- #
shop_frame = tk.Frame(root, width=400, height=600)
shop_frame.config(background=BACKGROUND)

# Close button
shop_close_button = tk.Button(shop_frame,
                              text="",
                              image=close_image,
                              background=BACKGROUND,
                              border=0,
                              activebackground=BACKGROUND,
                              activeforeground=BACKGROUND,
                              command=shop_click_off)

shop_close_button.pack(anchor='e')

# Points label
points_label = tk.Label(shop_frame,
                        text="My points",
                        background=BACKGROUND,
                        foreground=FONT_COLOR,
                        font=(FONT_NAME, 20))
points_label.pack()

points_amount_label = tk.Label(shop_frame,
                               text=points.get(),
                               background=BACKGROUND,
                               foreground=FONT_COLOR,
                               font=(FONT_NAME, 40))
points_amount_label.pack()



root.mainloop()
