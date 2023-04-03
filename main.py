import tkinter.messagebox
from settings import *
from stats import *

# ---------------------------- SOUND MECHANISM ----------------------------------- #


def set_sound(sound_to_set):
    global main_sound
    main_sound = sound_to_set


def play_sound():
    if main_sound.get_length() <= 1:
        main_sound.play()
    else:
        main_sound.play(loops=work_interval.get())


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(time_sec):
    # Label change
    start_button.config(text="Focus time",
                        background=background,
                        foreground=FONT_COLOR,
                        activebackground=background,
                        activeforeground=FONT_COLOR,
                        command='')
    stat_button.config(image='')
    settings_button.config(image='')

    # Countdown configuration
    counter = root.after(1000, countdown, time_sec - 1)
    minutes, seconds = divmod(time_sec, 60)
    timer = '{:02d}:{:02d}'.format(minutes, seconds)
    countdown_label.config(text=timer)

    # When timer is gone
    if time_sec == 0:
        ping_sound.play()
        root.after_cancel(counter)
        main_sound.stop()
        today_date = datetime.today().strftime('%Y-%m-%d')
        with open("data.csv", 'a') as csvfile:
            csvfile.write(f"{today_date},{work_interval.get()}")
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
        minutes, seconds = divmod(work_interval.get() * 60, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        countdown_label.config(text=timer)
        start_button.config(text="Start",
                            background=FONT_COLOR,
                            foreground=background,
                            activebackground=ACTIVE_BACKGROUND,
                            command=lambda: countdown(work_interval.get() * 60))
        stat_button.config(image=statistics_image)
        settings_button.config(image=settings_image)


# --------------------- FRAME CONFIGURATION -----------------------------#

# settings frame on/off
def settings_click_on():
    main_frame.pack_forget()
    settings_frame.pack()


def settings_click_off():
    settings_frame.pack_forget()
    main_frame.pack()
    countdown_label.config(text=f"{work_interval.get()}:00")


def stat_click_on():
    main_frame.pack_forget()
    stat_frame.pack()


def stat_click_off():
    stat_frame.pack_forget()
    main_frame.pack()
    countdown_label.config(text=f"{work_interval.get()}:00")


def time_label_update(time_sec):
    minutes, seconds = divmod(time_sec, 60)
    timer = '{:02d}:{:02d}'.format(minutes, seconds)
    countdown_label.config(text=timer)


def change_theme(bg_col, image):
    global background

    for widget in main_frame.winfo_children():
        if isinstance(widget, (tk.Label, tk.Frame)) and widget["background"] == background:
            widget.config(background=bg_col)
        if isinstance(widget, tk.Button):
            if widget["background"] == background:
                widget.config(background=bg_col)
            if widget["activebackground"] == background:
                widget.config(activebackground=bg_col)

    for widget in settings_frame.winfo_children():
        if isinstance(widget, (tk.Label, tk.Frame, tkinter.Spinbox)) and widget["background"] == background:
            widget.config(background=bg_col)
        if isinstance(widget, tk.Button):
            if widget["background"] == background:
                widget.config(background=bg_col)
            if widget["activebackground"] == background:
                widget.config(activebackground=bg_col)

    for widget in sound_label.winfo_children():
        if isinstance(widget, tk.Button):
            if widget["background"] == background:
                widget.config(background=bg_col)
            if widget["activebackground"] == background:
                widget.config(activebackground=bg_col)

    for widget in theme_frame.winfo_children():
        if isinstance(widget, tk.LabelFrame):
            if widget["background"] == background:
                widget.config(background=bg_col)

    for widget in stat_frame.winfo_children():
        if isinstance(widget, (tk.Button, tk.Label)):
            if widget["background"] == background:
                widget.config(background=bg_col)
            if widget["activebackground"] == background:
                widget.config(activebackground=bg_col)

    background = bg_col
    start_button.config(foreground=background)
    main_frame.config(background=background)
    settings_frame.config(background=background)
    stat_frame.config(background=background)
    root.config(background=background)
    main_image_label.config(image=image)


# --------------------------- MAIN FRAME SETUP --------------------------------- #
main_frame = tk.Frame(root)
main_frame.pack()
main_frame.config(background=background)

# Main image Label
main_image_label = tk.Label(main_frame,
                            image=tomato_image,
                            background=background)
main_image_label.grid(row=0,
                      column=1,
                      pady=30)

# Countdown Label
countdown_label = tk.Label(main_frame,
                           text=f"{work_interval.get()}:00",
                           font=(FONT_NAME, 60),
                           background=background,
                           foreground=FONT_COLOR)
countdown_label.grid(row=1,
                     column=1)

# Start button
start_button = tk.Button(main_frame,
                         text="Start",
                         foreground=background,
                         background=FONT_COLOR,
                         border=0,
                         width=15,
                         font=(FONT_NAME, 16),
                         command=lambda: [countdown(work_interval.get() * 60), play_sound()])
start_button.grid(row=2,
                  column=1,
                  ipady=5,
                  pady=20)

# Settings Button
settings_button = tk.Button(main_frame,
                            text="",
                            background=background,
                            activeforeground=background,
                            image=settings_image,
                            activebackground=background,
                            border=0,
                            command=settings_click_on)
settings_button.grid(row=3,
                     column=0,
                     sticky='SW',
                     ipadx=20,
                     ipady=20)

# Stat Button
stat_button = tk.Button(main_frame,
                        text="",
                        background=background,
                        activeforeground=background,
                        image=statistics_image,
                        command=stat_click_on,
                        activebackground=background,
                        border=0)
stat_button.grid(row=3,
                 column=2,
                 sticky='SE',
                 pady=(40, 0),
                 ipadx=20,
                 ipady=20)

# --------------------------- SETTINGS FRAME SETUP --------------------------------- #
settings_frame = tk.Frame(root, width=400, height=600, background=background)

# Work length label
work_length_label = tk.Label(settings_frame,
                             text="Work Interval",
                             font=(FONT_NAME, 14),
                             foreground=FONT_COLOR,
                             background=background)
work_length_label.grid(row=1,
                       column=0,
                       sticky='W',
                       pady=(100, 0))

work_length_spinbox = tk.Spinbox(settings_frame,
                                 from_=25,
                                 to=180,
                                 width=5,
                                 background=background,
                                 foreground=FONT_COLOR,
                                 textvariable=work_interval,
                                 command=lambda: print(work_interval.get()))
work_length_spinbox.grid(row=1,
                         column=1,
                         sticky='E',
                         pady=(100, 0))

# Break length label
break_length_label = tk.Label(settings_frame,
                              text="Break",
                              font=(FONT_NAME, 14),
                              foreground=FONT_COLOR,
                              background=background)
break_length_label.grid(row=2,
                        column=0,
                        sticky='W')

break_length_spinbox = tk.Spinbox(settings_frame,
                                  from_=5,
                                  to=15,
                                  width=5,
                                  background=background,
                                  foreground=FONT_COLOR,
                                  textvariable=break_interval,
                                  command=lambda: time_label_update(work_interval.get()))
break_length_spinbox.grid(row=2,
                          column=1,
                          sticky='E')

theme_frame = tk.Frame(settings_frame, background=background)

# color display frame
shop_color_label = tk.LabelFrame(theme_frame,
                                 text="Theme",
                                 labelanchor='n',
                                 background=background,
                                 foreground=FONT_COLOR,
                                 font=(FONT_NAME, 16))
shop_color_label.grid(row=0,
                      column=0,
                      pady=30)

# Create background button
for color in background_color:
    btn = tk.Button(shop_color_label,
                    background=color,
                    activebackground=color,
                    width=5,
                    border=1,
                    relief="ridge")
    btn.grid(row=1,
             column=background_color.index(color) + 1, pady=10)
    background_color_buttons.append(btn)

background_color_buttons[0].config(
    command=lambda: change_theme(background_color[0], tomato_image))
background_color_buttons[1].config(
    command=lambda: change_theme(background_color[1], berry_image))
background_color_buttons[2].config(
    command=lambda: change_theme(background_color[2], pear_image))
background_color_buttons[3].config(
    command=lambda: change_theme(background_color[3], coconut_image))
background_color_buttons[4].config(
    command=lambda: change_theme(background_color[4], raspberry_image))

# Add side padding
background_color_buttons[0].grid_configure(padx=(30, 0))
background_color_buttons[len(
    background_color_buttons) - 1].grid_configure(padx=(0, 30))

# Sounds label
sound_label = tk.LabelFrame(theme_frame,
                            text="Sound",
                            labelanchor='n',
                            background=background,
                            foreground=FONT_COLOR,
                            font=(FONT_NAME, 16))
sound_label.grid(row=2,
                 column=0,
                 pady=30)

# Create background button
for sound in background_sound:
    btn = tk.Button(sound_label,
                    background=background,
                    activebackground=background,
                    border=0)
    background_sound_buttons.append(btn)
    btn.grid(row=3,
             column=background_sound.index(sound) + 1,
             pady=10,
             padx=8)

background_sound_buttons[0].grid_configure(padx=(30, 0))
background_sound_buttons[len(
    background_sound_buttons) - 1].grid_configure(padx=(0, 30))

background_sound_buttons[0].configure(image=none_image)
background_sound_buttons[1].configure(
    image=forest_image, command=lambda: set_sound(forest_sound))
background_sound_buttons[2].configure(
    image=sea_image, command=lambda: set_sound(sea_sound))
background_sound_buttons[3].configure(
    image=bird_image, command=lambda: set_sound(bird_sound))
background_sound_buttons[4].configure(
    image=flame_image, command=lambda: set_sound(fireplace_sound))

# Close button
settings_close_button = tk.Button(settings_frame,
                                  text="",
                                  image=close_image,
                                  background=background,
                                  border=0,
                                  activebackground=background,
                                  command=settings_click_off)
settings_close_button.grid(row=5,
                           columnspan=2,
                           pady=50)
theme_frame.grid(row=4,
                 columnspan=2)

# ------------------------------------- STATISTIC SECTION --------------------------------------- #
stat_frame = tk.Frame(root, width=400, height=600, background=background)

# Focus time section
total_focus_time_label = tk.Label(stat_frame,
                                  text="Total focus time: ",
                                  background=background,
                                  font=(FONT_NAME, 14),
                                  foreground=FONT_COLOR)
total_focus_time_label.grid(row=0,
                            column=0,
                            sticky='W',
                            pady=(50, 0))

total_focus_time = tk.Label(stat_frame,
                            text=total_time,
                            background=background,
                            font=(FONT_NAME, 14, "bold"),
                            foreground=FONT_COLOR)
total_focus_time.grid(row=0,
                      column=1,
                      sticky='E',
                      pady=(50, 0))

# Productive day section
most_productive_day_label = tk.Label(stat_frame,
                                     text="Most productive day: ",
                                     background=background,
                                     font=(FONT_NAME, 14),
                                     foreground=FONT_COLOR)
most_productive_day_label.grid(row=1,
                               column=0,
                               sticky='W')

most_productive_day = tk.Label(stat_frame,
                               text=most_productive(),
                               background=background,
                               font=(FONT_NAME, 14, "bold"),
                               foreground=FONT_COLOR)
most_productive_day.grid(row=1,
                         column=1,
                         sticky='E')
# Plot section
weekday_plot_button = tk.Button(stat_frame,
                                text="Weekday plot",
                                background=background,
                                font=(FONT_NAME, 14),
                                foreground=FONT_COLOR,
                                command=weekday_plot)
weekday_plot_button.grid(row=2,
                         columnspan=2,
                         sticky='WE',
                         pady=(50, 0))

year_plot_button = tk.Button(stat_frame,
                             text="Year plot",
                             background=background,
                             font=(FONT_NAME, 14),
                             foreground=FONT_COLOR,
                             command=year_plot)
year_plot_button.grid(row=3,
                      columnspan=2,
                      sticky='WE',
                      pady=(0, 50))

# Achievements Section


ach3_label = tk.Label(stat_frame,
                      background=background,
                      text="Focused for 100 hours",
                      font=(FONT_NAME, 14))
ach3_label.grid(row=4,
                columnspan=2,
                sticky='WE')

ach4_label = tk.Label(stat_frame,
                      background=background,
                      text="Focused for 300 hours",
                      font=(FONT_NAME, 14))
ach4_label.grid(row=5,
                columnspan=2,
                sticky='WE')

ach5_label = tk.Label(stat_frame,
                      background=background,
                      text="Focused for 500 hours",
                      font=(FONT_NAME, 14))
ach5_label.grid(row=6,
                columnspan=2,
                sticky='WE')

# Close button
stat_close_button = tk.Button(stat_frame,
                              text="",
                              image=close_image,
                              background=background,
                              border=0,
                              activebackground=background,
                              command=stat_click_off)
stat_close_button.grid(row=7,
                       columnspan=2,
                       pady=50)

if is_hours(100, total_time):
    ach3_label.config(foreground=FONT_COLOR)
if is_hours(300, total_time):
    ach4_label.config(foreground=FONT_COLOR)
if is_hours(500, total_time):
    ach5_label.config(foreground=FONT_COLOR)

root.mainloop()
