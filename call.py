from twilio.rest import Client
import tkinter as tk

def write():
    account_sid = "Enter account sid from twilio account"
    auth_token = "Enter auth token from twilio account"
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        to="enter your number",
        from_="enter the twilio generated number",
        url="https://drive.google.com/drive/my-drive/samplw.xml"
    )

    print(call.sid)
root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello",
                   command=write)
slogan.pack(side=tk.LEFT)

root.mainloop()
