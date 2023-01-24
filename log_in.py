class LogIn():
  def __init__(self, master):
    import tkinter as tk
    self.master = master

    self.master.title("LangFlash")
    self.a = 2
    self.frame = tk.Frame(self.master, bg= "red")
    self.frame.place(x= 0, y= 0, width= 1000, height= 600)
    self.img0 = tk.PhotoImage(master= self.frame, file= "./assets/account/here.png")
    self.img2 = tk.PhotoImage(master= self.frame, file= "./assets/account/continue_blue.png")
    self.background_img = tk.PhotoImage(file= "./assets/account/login_background.png")
    
    self.inputusername, self.inputpassword = tk.StringVar(), tk.StringVar()

    self.canvas = tk.Canvas(master= self.frame, bg = "white", bd = 0, height = 600, width = 1000, highlightthickness = 0, relief = "flat")
    self.canvas.place(x = 0, y = 0)
    self.canvas.create_text(710,100,text="LangFlash", font= ("Montserrat", 18), tags="title")

    b0 = tk.Button(master= self.frame,image = self.img0,borderwidth = 0,highlightthickness = 0,command = self.sowhat,relief = "flat")
    b1 = tk.Button(master= self.frame,image = self.img0,borderwidth = 0,highlightthickness = 0,command = self.go_signup,relief = "flat")
    b2 = tk.Button(master= self.frame, image = self.img2, bg= 'white', borderwidth = 0, highlightthickness = 0, command = self.validation, relief = "flat")

    b0.place(x = 805, y = 422, width = 37, height = 16)
    b1.place(x = 735, y = 398, width = 37, height = 16)
    b2.place(x = 656, y = 470, width = 138, height = 41)

    entry0 = tk.Entry(self.frame, bd = 2, bg = '#cfcfcf', highlightthickness = 0, font = ("Open Sans", 14), textvariable= self.inputusername)
    entry1 = tk.Entry(self.frame, bd = 2, bg = "#cfcfcf", highlightthickness = 0, font = ('Consolas', 16), show="*", textvariable= self.inputpassword)

    entry0.place(x = 554.5, y = 218, width = 341.0, height = 39)
    entry1.place(x = 554.5, y = 341, width = 341.0, height = 39)

    self.canvas.create_image(465.0, 300.0,image= self.background_img)

  def validation(self):
    import choose_lang as cl
    import pandas as pd
    import bcrypt
    self.canvas.delete("hi")
    record_data = pd.read_csv("./assets/stats/record_data.csv")
    users_names = list(record_data['user_name']) 
    user_name_input = self.inputusername.get()

    if user_name_input in users_names:
      index = users_names.index(user_name_input)
      user = (record_data.iloc[index]).to_dict()
    else:
      return self.canvas.create_text(775,270,text="Wrong Username or Password", font= ("Montserrat", 12), fill='#ff3333', tags="hi")
    
    if bcrypt.checkpw((str(self.inputpassword.get())).encode("utf-8"), (user["password"]).encode("utf-8")):
      self.frame.destroy()
      return cl.SelectLang(self.master, user_data= user)
    else:
      return self.canvas.create_text(775,270,text="Wrong Username or Password", font= ("Montserrat", 12), fill='#ff3333', tags="hi")
    
  def sowhat(self):
    if self.a % 2 == 0:
      self.canvas.delete("wtf")
      self.canvas.create_text(787,330,text="(╯°□°）╯︵ ┻━┻", font= ("Montserrat", 12), fill='#ff3333', tags="wtf")
      self.a += 1
    else:
      self.a -= 1
      self.canvas.delete("wtf")
      self.canvas.create_text(787,330,text="┬─┬ノ( ゜-゜ノ)", font= ("Montserrat", 12), fill='#ff3333', tags="wtf")

  def go_signup(self):
    import sign_up as su
    self.frame.destroy()
    return su.SignUp(self.master)

if __name__ == '__main__':
  import tkinter as tk
  import sys, os
  os.chdir(os.path.join(sys.path[0],''))

  root = tk.Tk()
  root.iconbitmap("./assets/favicon.ico")
  root.geometry("1000x600")
  root.resizable(False, False)

  app = LogIn(root)

  root.mainloop()
