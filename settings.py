import os
import sys
import tkinter as tk
import pygame
from stats import *

path = getattr(sys, '_MEIPASS', os.getcwd())
os.chdir(path)

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
work_interval = tk.IntVar(value=25)
break_interval = tk.IntVar(value=5)
background_color = ["#EA5455", "#002B5B", "#4E944F", "#865439", "#E30B5C"]
background_color_buttons = []
background_sound = ["sound/rain_sound.mp3", "sound/night_forest.mp3", "sound/sea_sound.mp3", "sound/bird_sound.mp3", "sound/fireplace_sound.mp3"]
background_sound_buttons = []
pygame.mixer.init()
main_sound = pygame.mixer.Sound("sound/beep_sound.mp3")

# Images
settings_image = tk.PhotoImage(file="icons/settings_button.png")
close_image = tk.PhotoImage(file="icons/close_button.png")
statistics_image = tk.PhotoImage(file="icons/statistics_button.png")
tomato_image = tk.PhotoImage(file="images/tomato.png")  # Red
berry_image = tk.PhotoImage(file="images/berry.png")  # Dark blue
pear_image = tk.PhotoImage(file="images/pear.png")  # Green
coconut_image = tk.PhotoImage(file="images/coconut.png")  # Brown
raspberry_image = tk.PhotoImage(file="images/raspberry.png")  # Pink
rain_image = tk.PhotoImage(file="icons/rain_button.png")
forest_image = tk.PhotoImage(file="icons/forest_button.png")
sea_image = tk.PhotoImage(file="icons/sea_button.png")
bird_image = tk.PhotoImage(file="icons/bird_button.png")
flame_image = tk.PhotoImage(file="icons/flame_button.png")
none_image = tk.PhotoImage(file="icons/none_button.png")

# Sounds
bird_sound = pygame.mixer.Sound("sound/bird_sound.mp3")
fireplace_sound = pygame.mixer.Sound("sound/fireplace_sound.mp3")
forest_sound = pygame.mixer.Sound("sound/night_forest.mp3")
sea_sound = pygame.mixer.Sound("sound/sea_sound.mp3")
rain_sound = pygame.mixer.Sound("sound/rain_sound.mp3")
ping_sound = pygame.mixer.Sound("sound/ping_sound.mp3")

# Label text
total_time = total_focus()


