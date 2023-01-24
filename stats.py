class Statistics:
  def __init__(self, masters, user_data):
    import datetime
    import tkinter as tk
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import numpy as np

    self.master = masters
    self.user_data = user_data
    self.goal = self.user_data['goal']
    self.user = self.user_data['user_name']

    self.master.title("LangFlash - Profile")

    self.frame = tk.Frame(self.master, bg= "red")
    self.frame.place(x= 0, y= 0, width=1000, height=600)
    
    self.background = tk.Canvas(self.frame, bd= 0, bg= 'white', highlightthickness= 0, relief= 'flat', height= 600, width= 1000,)
    self.background.place(x= 0, y= 0 )

    self.languages = {
      "zhg": ["zh.png", "zh_off.png"],
      "ind": ["id.png", "id_off.png"], 
      "jap": ["jp.png", "jp_off.png"], 
      "vit": ["vt.png", "vt_off.png"], 
      "tai": ["th.png", "th_off.png"], 
      "kor": ["sk.png", "sk_off.png"], 
      "bur": ["my.png", "my_off.png"], 
      "lao": ["la.png", "la_off.png"], 
      "khm": ["cd.png", "cd_off.png"], 
      "tag": ["tg.png", "tg_off.png"],}

    self.languages_iter = self.languages.keys()
    self.picture_on = []
    self.picture_off = []

    counter = 0
    for j, (i, lang) in enumerate(user_data.items()):
      if i in self.languages_iter:
        if counter == 0: counter += 1
        if lang == True or str(lang) == "True":
          self.picture_on.append(tk.PhotoImage(file= f"./assets/stats/{self.languages[i][0]}"))
          self.picture_off.append(None)
          self.background.create_image(90 + 55 * (counter), 200, image= self.picture_on[-1])
        else:
          self.picture_on.append(None)
          self.picture_off.append(tk.PhotoImage(file= f"./assets/stats/{self.languages[i][1]}"))
          self.background.create_image(90 + 55 * (counter), 185, image= self.picture_off[-1])
        counter += 1
  
    self.background.create_text(3.49*50, 1.33*90, font=('Montserrat',18,), text= self.user, justify= 'left')
    self.background.create_text(800, 1.33*30, font=('Montserrat',18), text= datetime.date.today().strftime("%Y/%m/%d"))
    self.back_but = tk.PhotoImage(file='./assets/back_button.png')

    self.button_back   = tk.Button(self.frame, image = self.back_but, bd= 0, bg= 'white', command= lambda: self.go_back())
    
    self.save_pic = tk.PhotoImage(file= "./assets/stats/save.png")
    self.save_but = tk.Button(self.frame, image= self.save_pic, bd= 0, bg= "white", command= lambda: self.save())

    self.goal_set = tk.StringVar()
    self.goal_set.set(self.goal)

    self.background.create_text(800, 1.33*96, font=('Montserrat',18), text= "Daily Goal")
    self.goal_mod = tk.Spinbox(self.frame, bg= "#BDD7EE", justify= tk.CENTER, font= ("Montserrat", 18), from_=1, to= 10**4, textvariable= self.goal_set)
    self.goal_mod.place(x= 740, y= 1.33*120, relheight= 0.05, relwidth= 0.12)
    self.goal_mod.focus_set()
    self.goal_mod.bind("<KeyRelease>", self.only_number)
    
    self.button_back.place(
      x= 0.27*96, y= 0.27*96,
      width= 0.45*96, height= 0.35*96)
    self.save_but.place(
      x= 1*96, y= 0.27*96,
      width= 0.45*96, height= 0.45*96)

    # Ratio
    self.background.create_text(800, 280, font=('Montserrat',18), text= "Score")
    self.fig_pix, self.ax_pie = plt.subplots()
    self.ax_pie.pie([user_data["correct_ans"], user_data["wrong_ans"]], labels= ["Correct", "Wrong"], colors= ["#A7C7E7","#646464"], autopct='%1.1f%%')
    self.fig_pix.tight_layout()
    self.plot_accuracy = FigureCanvasTkAgg(self.fig_pix, master= self.frame)
    self.plot_accuracy.draw()
    self.plot_accuracy.get_tk_widget().place(x= 37.7952755906*17.2, y= 8* 37.7952755906, height=96*2.53, width=96*3.08)
    
    # Activity
    last_days = np.flip(np.array([((datetime.date.today()-datetime.timedelta(days= 0 + x)).strftime("%A")[0:2]) for x in range(7)]))
    last_days_check = [(datetime.date.today()-datetime.timedelta(days= 0 + x)).strftime("%Y/%m/%d") for x in range(7)]

    activity = [user_data["seventh_day"], user_data["sixth_day"], user_data["fifth_day"], user_data["fourth_day"], user_data["third_day"], user_data["second_day"], user_data["first_day"]]

    for i, j in enumerate(last_days_check):
      if j == user_data["last_day_active"]:
        days_passed = i
        del activity[0:i]
        activity += [0] * i
        break
    else:
      activity = [0,0,0,0,0,0,0]

    actvty, actvty_ax = plt.subplots()
    actvty_ax.plot(last_days, activity, color= "#CF9FFF", marker= 'o', lw= 1, markersize= 6)
    actvty_ax.plot(last_days, [user_data["goal"]] * 7, color= "#77dd77", marker= '', linestyle = "-", lw= 1, markersize= 6)

    actvty.tight_layout()

    if max(activity) > user_data["goal"]:
      actvty_ax.set_ylim(None, max(activity)+2.5)
    else:
      actvty_ax.set_ylim(None, user_data["goal"]+2.5)
    actvty_ax.set_xlim(-0.2,6.2)

    self.plot_frqncy = FigureCanvasTkAgg(actvty, master= self.frame)
    self.plot_frqncy.draw()
    self.plot_frqncy.get_tk_widget().place(x= 37.7952755906*2, y= 6.2 * 37.7952755906, height=96*3.53, relwidth=0.55)
    
  def go_back(self):
    import choose_lang as cl
    import matplotlib.pyplot as plt
    plt.close("all")
    self.frame.destroy()
    return cl.SelectLang(self.master, user_data= self.user_data)
  
  def save(self):
    self.user_data["goal"] = int(self.goal_set.get())
  
  def only_number(self, e):
    inside = str(self.goal_set.get())
    if inside.isdigit() == True:
      if 1 <= float(inside) <= 10**4:
        return 0
      elif 1 > float(inside): self.goal_set.set(10)
      else: self.goal_set.set(10**4)
    else: 
      self.goal_set.set(1)