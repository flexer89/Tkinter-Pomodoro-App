import tkinter as tk
from pygame import mixer

# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.resizable(False, False)
root.geometry("400x600")
background = "#EA5455"
root.config(background=background)

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
ACTIVE_BACKGROUND = "#F9D2D2"
FONT_COLOR = "#FFFFFF"

# ---------------------------- SETTINGS --------------------------------- #
work_interval = tk.IntVar(value=1)
break_interval = tk.IntVar(value=1)
points = tk.IntVar(value=0)
background_color = ["#002B5B", "#4E944F", "#865439", "#E0A526", "#2C3333"]
background_color_buttons = []
background_sound = ["sound/rain_sound.mp3", "sound/night_forest.mp3", "sound/sea_sound.mp3", "sound/bird_sound.mp3", "sound/fireplace_sound.mp3"]
background_sound_buttons = []
bought_color = []
bought_buttons = []
mixer.init()

# Images
settings_image = tk.PhotoImage(file="icons/settings_button.png")
close_image = tk.PhotoImage(file="icons/close_button.png")
shop_image = tk.PhotoImage(file="icons/shop_button.png")
tomato_image = tk.PhotoImage(file="images/tomato.png")  # Red
berry_image = tk.PhotoImage(file="images/berry.png")  # Dark blue
pear_image = tk.PhotoImage(file="images/pear.png")  # Green
coconut_image = tk.PhotoImage(file="images/coconut.png")  # Brown
banana_image = tk.PhotoImage(file="images/banana.png")  # Yellow
blackberries_image = tk.PhotoImage(file="images/blackberry.png")  # Black
rain_image = tk.PhotoImage(file="icons/rain_button.png")
forest_image = tk.PhotoImage(file="icons/forest_button.png")
sea_image = tk.PhotoImage(file="icons/sea_button.png")
bird_image = tk.PhotoImage(file="icons/bird_button.png")
flame_image = tk.PhotoImage(file="icons/flame_button.png")

# Sounds
bird_sound = mixer.Sound("sound/bird_sound.mp3")
fireplace_sound = mixer.Sound("sound/fireplace_sound.mp3")
forest_sound = mixer.Sound("sound/night_forest.mp3")
sea_sound = mixer.Sound("sound/sea_sound.mp3")
rain_sound = mixer.Sound("sound/rain_sound.mp3")

