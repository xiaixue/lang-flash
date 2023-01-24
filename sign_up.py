class SignUp():
  def __init__(self, master):
    import tkinter as tk
    self.master = master
    self.master.title("LangFlash - Sign Up")

    self.frame = tk.Frame(self.master, bg= "red")
    self.frame.place(x= 0, y= 0, width=1000, height=600)
    
    self.setpassword = tk.StringVar()
    self.setpin      = tk.StringVar()
    self.setusername = tk.StringVar()
    
    self.canvas = tk.Canvas(self.frame, bg = "#ffffff", bd = 0, height = 600, width = 1000, highlightthickness = 0, relief = "ridge")
    self.canvas.place(x = 0, y = 0)

    self.img0 = tk.PhotoImage(master = self.frame, file = f"./assets/account/continue_red.png")
    self.img1 = tk.PhotoImage(master = self.frame, file = f"./assets/account/img1.png")
    self.background_img = tk.PhotoImage(master = self.frame, file = f"./assets/account/BackGround.png")

    b0 = tk.Button(self.frame, image = self.img0, borderwidth = 0, highlightthickness = 0, command = self.Data, relief = "flat")
    b1 = tk.Button(self.frame, image = self.img1, bd = 0, highlightthickness = 0, command = self.go_back, relief = "flat")
    
    entry0 = tk.Entry(self.frame, bd = 2, bg = "#cfcfcf", highlightthickness = 0, font = ('Consolas', 16), show='*', textvariable= self.setpin)
    entry1 = tk.Entry(self.frame, bd = 2, bg = "#cfcfcf", highlightthickness = 0, font = ('Consolas', 16), show='*', textvariable = self.setpassword)
    entry2 = tk.Entry(self.frame, bd = 2, bg = "#cfcfcf", highlightthickness = 0, font = ('Open Sans', 14), textvariable = self.setusername)
    
    b0.place(x = 207, y = 525, width = 138, height = 41)
    b1.place(x = 42, y = 43, width = 26, height = 26)
    entry0.place(x = 101.5, y = 431, width = 151.0, height = 38)
    entry1.place(x = 101.5, y = 312, width = 341.0, height = 39)
    entry2.place(x = 101.5, y = 193, width = 341.0,  height = 39)

    self.canvas.create_image(500.0, 300.0, image= self.background_img)

  def Data(self):
    import log_in as li
    import pandas as pd
    from tkinter import messagebox

    password = str(self.setpassword.get()).encode("utf-8")
    username = str(self.setusername.get())
    pin      = str(self.setpin.get())

    record_data = pd.read_csv("./assets/stats/record_data.csv", index_col= 0)

    if username in list(record_data['user_name']):
      return messagebox.showwarning("Warning", "Username already exists")
    if len(password) > 3 and len(pin) == 4:
      import bcrypt
      import datetime

      hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
      passed = hashed_password.decode('utf-8')
      self.frame.destroy()
      new_user_data = {'user_name': username, 
      'password': passed, 
      'pin': pin, 
      'goal': 50, 
      'correct_ans': 1, 
      'wrong_ans': 0, 
      'zhg': False, 'ind': False, 'jap': False, 'vit': False, 'tai': False, 'kor': False, 'bur': False, 'lao': False, 'khm': False, 'tag': False, 'last_day_active': datetime.date.today().strftime("%Y/%m/%d"),
      'seventh_day': 0,
      'sixth_day': 0,
      'fifth_day': 0,
      'fourth_day': 0,
      'third_day': 0,
      'second_day': 0,
      'first_day': 0,
      }
      added_user = record_data.append(new_user_data, ignore_index= False)
      added_user.to_csv("./assets/stats/record_data.csv")
      return li.LogIn(self.master)
    else: return messagebox.showwarning("Warning", "Pin has to be 4 characters long or \nPassword has to be 4 characters long or more.")

  def go_back(self):
    self.frame.destroy()
    import log_in as li
    return li.LogIn(self.master)