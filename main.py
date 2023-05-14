import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification

# Function to block website
def web_block():
    """A function to block websites"""
    website = entry_val.get()
    print(website)
    # Initialize an empty list and append url
    websites = []
    websites.append(website)
    print(websites)
    Ip_address = '127.0.0.1'
    host_path ="C:\Windows\System32\drivers\etc\hosts" 
    with open(host_path, "r+") as file_obj:
        content = file_obj.read()
        for web in websites:
            if web in content:
                pass
            else:
                file_obj.write(f"\n{Ip_address}   {web}")
    # Clear the input field
    entry_val.set("")
                

# Window
window = ttk.Window(themename='darkly')
window.title("Website Blocker App")
# Designate width and height
app_width = 400
app_height = 250

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)
window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

# Label Widget
title_label = ttk.Label(window,
                        text='Enter website URLs',
                        font='Calibri 18 bold',
                        foreground='white',
                        justify='center')
title_label.pack(pady=30)

# Entry Widget
entry_val = tk.StringVar()
entry = ttk.Entry(window, textvariable=entry_val)
entry.pack(padx=20, fill='x')

# Toast Notiification for When Site is blocked
toast_block = ToastNotification(
    title="Notification",
    message="Site has been blocked",
    duration=4000,
    bootstyle='light',
    position = (100, 100, 'n'),    
)

# Button Widget
button_block = ttk.Button(window, text='Block', width=17, command= lambda: [web_block(), toast_block.show_toast()])
button_block.pack(pady=17)


# Run
window.mainloop()