import tkinter as tk 
from tkinter import *
import qrcode
from PIL import Image, ImageTk
from tkinter import filedialog

# Window Create : 
window = tk.Tk()
window.title(" Text & Link TO QR ")
window.geometry("600x650")
window.resizable(False, False)
window.config(background="#001129")
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)

qr_image = None

def genrate_qr():
    global qr_image

    data = input_entry.get()

    qr_image = qrcode.make(data)   # store image

    img = qr_image.resize((300, 300))
    qr_img = ImageTk.PhotoImage(img)

    qr_label.config(image=qr_img)
    qr_label.image = qr_img

def download_qr():
    if qr_image is None:
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")]
    )

    if file_path:
        qr_image.save(file_path)


# Create Main Frame : 
main_frame = tk.Frame(
    window,
    bg="#1A91A8",
    borderwidth=4,
    relief="ridge",   
)
main_frame.grid(row=0,column=0,padx=15,pady=15,sticky="nsew")
main_frame.grid_columnconfigure(0,weight=1)

# Input Entry Box :
input_entry = tk.Entry(
    main_frame,
    bg="#002948",
    fg="#B3BBC4",
    font=("Times New Roman",14,"bold"),
    borderwidth=2,
    relief="solid",  
)

input_entry.grid(row=0, column=0, padx=20, pady=(30,10), ipadx=10, ipady=10, sticky="ew")

# Genrate QR Button :
genrate_qr_button = tk.Button(
    main_frame,
    bg="#034256",
    fg="#cfd0d1",
    font=("Times New Roman",14,"bold"),
    text="Genrate QR",
    command=genrate_qr,
    borderwidth=2,
    relief="solid",
)
genrate_qr_button.grid(row=1, column=0, padx=20, pady=10, ipady=8, sticky="ew")

# QR LABEL (ADD THIS):
qr_label = Label(
    main_frame,
    bg="#1A91A8",    
    # borderwidth=2,
    # relief="solid",
)
qr_label.grid(row=2, column=0, pady=20)

# Download Button :
download_btn = Button(
    main_frame,
    text="Download QR",
    bg="#539577",
    fg="#000000",
    font=("Times New Roman", 14, "bold"),
    command=download_qr,
    borderwidth=2,
    relief="solid",
)
download_btn.grid(row=3, column=0, padx=20, pady=10, ipady=8, sticky="ew")


# Run Window : 
window.mainloop()