import tkinter as tk
from PIL import Image, ImageTk


def display_fullscreen_image(image_path, display_time=5):
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    root.configure(background="black")  # Set background to black

    # Load the image in its natural size
    img = Image.open(image_path)
    photo_img = ImageTk.PhotoImage(img)

    # Calculate position to center the image
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - img.width) // 2
    y = (screen_height - img.height) // 2

    # Display the image
    label = tk.Label(root, image=photo_img, bg="black")
    label.place(x=x, y=y)

    # Close the window after 'display_time' seconds
    root.after(display_time * 1000, root.destroy)

    root.mainloop()
