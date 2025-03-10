import os
import shutil
from PIL import Image, ImageTk
import tkinter as tk

# Define the paths to the folders
general_folder = "/Users/liuyuhan/Desktop/Asian_Indian_classify/Indian/indian_2000"
folder1 = "/Users/liuyuhan/Desktop/Asian_Indian_classify/Indian/Non_Indian"
folder2 = "/Users/liuyuhan/Desktop/Asian_Indian_classify/Indian/Unclear_Unsure"

# Ensure the target folders exist
os.makedirs(folder1, exist_ok=True)
os.makedirs(folder2, exist_ok=True)

# Create a Tkinter window
root = tk.Tk()
root.title("Image Sorter")

# Create a label to display the image
image_label = tk.Label(root)
image_label.pack()

# List to store image paths
image_paths = []
current_image_index = 0

def load_images():
    """Load all images from the general folder."""
    global image_paths
    image_paths = [
        os.path.join(general_folder, filename)
        for filename in os.listdir(general_folder)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))
    ]

def display_image(image_path):
    """Display the image in the Tkinter window."""
    img = Image.open(image_path)
    img.thumbnail((1600, 1200))  # Resize the image to fit the window
    img_tk = ImageTk.PhotoImage(img)
    image_label.config(image=img_tk)
    image_label.image = img_tk  # Keep a reference to avoid garbage collection

def move_image(image_path, destination_folder):
    """Move the image to the specified folder."""
    shutil.move(image_path, os.path.join(destination_folder, os.path.basename(image_path)))

def on_key_press(event):
    """Handle key press events."""
    global current_image_index
    if event.char == 'n':
        move_image(image_paths[current_image_index], folder1)
        current_image_index += 1
    elif event.char == 'u':
        move_image(image_paths[current_image_index], folder2)
        current_image_index += 1
    elif event.keysym == 'space':
        current_image_index += 1

    # Display the next image or close the window if no more images
    if current_image_index < len(image_paths):
        display_image(image_paths[current_image_index])
    else:
        root.destroy()

# Load images and display the first one
load_images()
if image_paths:
    display_image(image_paths[current_image_index])
else:
    print("No images found in the general folder.")
    root.destroy()

# Bind key press events
root.bind('<Key>', on_key_press)

# Start the Tkinter event loop
root.mainloop()