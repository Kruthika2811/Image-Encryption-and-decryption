
from tkinter import *
from tkinter import filedialog, messagebox

# Create the main window
root = Tk()
root.title("Image Encryptor")
root.geometry("300x200")

file_name = ""

def select_file():
    global file_name
    file = filedialog.askopenfile(mode='r', filetype=[('JPG Files', '*.jpg')])
    if file:
        file_name = file.name
        file_label.config(text=f"Selected: {file_name.split('/')[-1]}")

def encrypt_decrypt_image():
    global file_name
    if not file_name:
        messagebox.showerror("Error", "No file selected!")
        return

    key = key_entry.get()
    if not key.isdigit():
        messagebox.showerror("Error", "Key must be a number!")
        return

    try:
        with open(file_name, 'rb') as fi:
            image = bytearray(fi.read())

        key_value = int(key)
        for index, value in enumerate(image):
            image[index] = value ^ key_value  # XOR for both encryption & decryption

        with open(file_name, 'wb') as fi:
            fi.write(image)

        messagebox.showinfo("Success", "Operation completed successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {str(e)}")

# UI Elements
Label(root, text="Enter Key:").pack(pady=5)
key_entry = Entry(root, width=15)
key_entry.pack(pady=5)

file_label = Label(root, text="No file selected", fg="red")
file_label.pack()

Button(root, text="Select Image", command=select_file, bg="lightblue").pack(pady=5)
Button(root, text="Encrypt/Decrypt", command=encrypt_decrypt_image, bg="lightgreen").pack(pady=5)

root.mainloop()
