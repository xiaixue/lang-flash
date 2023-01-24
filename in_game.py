class ToolTip(object):
  def __init__(self, widget):
    self.widget = widget
    self.tipwindow = None
    self.id = None
    self.x = self.y = 0

  def showtip(self, text):
    import tkinter as tk
    self.text = text
    if self.tipwindow or not self.text:
      return
    x, y, cx, cy = self.widget.bbox("insert")
    x = x + self.widget.winfo_rootx() + 57
    y = y + cy + self.widget.winfo_rooty() +27
    self.tipwindow = tw = tk.Toplevel(self.widget)
    tw.wm_overrideredirect(1)
    tw.wm_geometry("+%d+%d" % (x, y))
    label = tk.Label(tw, text=self.text, justify=tk.LEFT, background="#ffffe0", relief=tk.SOLID, borderwidth=1, font=("arial", "8", "normal"))
    label.pack(ipadx=1)

  def hidetip(self):
    tw = self.tipwindow
    self.tipwindow = None
    if tw: tw.destroy()

def CreateToolTip(widget, text):
  toolTip = ToolTip(widget)
  def enter(event):
    toolTip.showtip(text)
  def leave(event):
    toolTip.hidetip()
  widget.bind('<Enter>', enter)
  widget.bind('<Leave>', leave)

class inGame:
  def __init__(self, master, words, user_data, language, diff= False, dui= 0, budui= 0, trad= False, flip_= 0):
    import tkinter as tk
    import random
    import numpy as np

    self.master = master
    self.dly_count = user_data['goal']
    self.words = words
    self.lang = language
    self.user_data = user_data
    self.trad = trad
    self.diff = diff
    self.dui = dui
    self.budui = budui    
    self.flip = flip_
    self.master.title("LangFlash")

    to_add = {3: [1, -1, 0, 1], 2: [-1,  1, 1, 0]}
    if flip_ == 0: answers_order = [3,2]
    elif flip_ == 1: answers_order = [2,3]
    elif flip_ == 2:
      answers_order = []
      while(len(answers_order) < 2):
        p = random.randint(2,3)
        if not p in answers_order:
          answers_order.append(p)
    
    if self.lang == "Chinese":
      if self.trad == True: 
        self.show = answers_order[0] + to_add[answers_order[0]][3]
        self.disp = answers_order[1] + to_add[answers_order[0]][2]
      else: 
        self.show = answers_order[0] + to_add[answers_order[0]][0]
        self.disp = answers_order[1] + to_add[answers_order[0]][1]
    if self.lang == "Japanese":
      self.show = answers_order[0]
      self.disp = answers_order[1]
    elif self.lang != "Chinese":
      self.show = answers_order[1]
      self.disp = answers_order[0]
    
    lang_check = {"Chinese": "zhg", "Japanese": "jap", "Indonesian": "ind", "Vietnamese": "vit", "Thai": "tai", "Korean": "kor", "Burmese": "bur", "Lao": "lao", "Khmer": "khm", "Tagalog": "tag",}

    self.user_data[lang_check[self.lang]] = True
    
    self.frame = tk.Frame(self.master, bg= "red")
    self.frame.place(x= 0, y= 0, width=1000, height=600)

    self.back = tk.Canvas(self.frame, bd= 0, bg= 'white', highlightthickness= 0, relief= 'flat', height= 600, width= 1000)
    self.back.place(x= 0, y= 0,)
    
    if self.diff == True: option = 8
    else: option = 4

    self.exer_box = tk.PhotoImage(master= self.frame, file=f'./assets/in_game/exercise_box.png')
    self.exit_but = tk.PhotoImage(master= self.frame, file=f'./assets/in_game/exit_button.png')
    self.optn_box = tk.PhotoImage(master= self.frame, file=f'./assets/in_game/option_box.png')

    if self.lang == 'Chinese':
      self.disc = True
      self.piny_ico = tk.PhotoImage(master= self.frame, file=f'./assets/in_game/show_pinyin.png')
      self.button_show_piny = tk.Button(self.frame,image=self.piny_ico, bd= 0, bg= '#fff', command= lambda: self.pinyin())
      self.button_show_piny.place(x = 851.52, y = 43.2,width = 80, height = 40)
         
    self.answers = list()

    keys = list(self.words.keys())
    self.answers = []
    while (len(self.answers) < option):
      words_key = random.choice(keys)
      if not words_key in self.answers:
        self.answers.append(words_key)
        keys.remove(words_key)

    self.right_answer = random.randint(0,len(self.answers)-1)
    self.font_show = "Arial" #DengXian
    self.button_option_1 = tk.Button(self.frame, image = self.optn_box, bd= 0, bg= 'white', text= self.words[self.answers[0]][self.disp], compound= 'center', font= (self.font_show,12), command= lambda: self.continuer(1))
    self.button_option_2 = tk.Button(self.frame, image = self.optn_box, bd= 0, bg= 'white', text= self.words[self.answers[1]][self.disp], compound= 'center', font= (self.font_show,12), command= lambda: self.continuer(2))
    self.button_option_3 = tk.Button(self.frame, image = self.optn_box, bd= 0, bg= 'white', text= self.words[self.answers[2]][self.disp], compound= 'center', font= (self.font_show,12), command= lambda: self.continuer(3))
    self.button_option_4 = tk.Button(self.frame, image = self.optn_box, bd= 0, bg= 'white', text= self.words[self.answers[3]][self.disp], compound= 'center', font= (self.font_show,12), command= lambda: self.continuer(4))
    
    if self.diff == True:
      self.button_option_5 = tk.Button( self.frame,image = self.optn_box, bd= 0, bg= 'white', text= self.words[self.answers[4]][self.disp], compound= 'center', font= (self.font_show,12), command= lambda: self.continuer(5))
      self.button_option_6 = tk.Button(self.frame, image = self.optn_box, bd= 0, bg= 'white', text= self.words[self.answers[5]][self.disp], compound= 'center', font= (self.font_show,12), command= lambda: self.continuer(6))
      self.button_option_7 = tk.Button(self.frame, image = self.optn_box, bd= 0, bg= 'white', text= self.words[self.answers[6]][self.disp], compound= 'center', font= (self.font_show,12), command= lambda: self.continuer(7))
      self.button_option_8 = tk.Button(self.frame, image = self.optn_box, bd= 0, bg= 'white', text= self.words[self.answers[7]][self.disp], compound= 'center', font= (self.font_show,12), command= lambda: self.continuer(8))
      
      self.button_option_5.place( x= 85.44, y= 298.56+63.36, width= 172, height= 52)
      self.button_option_6.place( x= 85.44+217.92, y= 298.56+63.36, width= 172, height= 52)
      self.button_option_7.place( x= 85.44+217.92+217.92, y= 298.56+63.36, width= 172, height= 52)
      self.button_option_8.place( x= 85.44+217.92+217.92+217.92, y= 298.56+63.36, width= 172, height= 52)		
      
    self.button_exit   = tk.Button(self.frame, image = self.exit_but, bd= 0, bg= 'white', command= self.go_back)

    self.exercise_bkgd = tk.Canvas(self.frame, bd= 0, bg= 'white', highlightthickness= 0, relief= 'flat', height= 150, width= 560,)
    self.exercise_text = tk.Canvas(self.frame, bd= 0, bg= 'white', highlightthickness= 0, relief= 'flat', height= 0.4*96, width= 5.51*96,)
    self.or_bkgd = tk.Canvas(self.frame, bd= 0, bg= 'white', highlightthickness= 0, relief= 'flat', height= 0.4*96, width= 5.51*96,)

    self.exercise_bkgd.create_image(280,75, image= self.exer_box)
    """""""""""""""""""""""""""""""""""""""""""""""""" #######################
    
    self.exercise_bkgd.create_text(280, 75, text= self.words[self.answers[self.right_answer]][self.show], font= (self.font_show, 20), width= 490)
    
    self.exercise_text.create_text(5.51*96/2, 0.4*96/2, font=('Montserrat',18), text= "Choose the correct option")
    self.or_bkgd.create_text(5.51*96/2, 0.4*96/2, font=('Montserrat',18), text="or")
    qp = self.user_data["first_day"] + self.dui
    self.back.create_text(500, 570, text= f"{qp}/{self.dly_count}", font= (self.font_show, 11))
    
    self.exercise_bkgd.place(x= 220, y= 97)
    self.exercise_text.place(x= 235, y= 30)
    self.or_bkgd.place(x=234 , y= 460)
    
    self.button_option_1.place(x= 85.44, y= 298.56, width= 172, height= 52,)
    self.button_option_2.place(x= 85.44+217.92, y= 298.56, width= 172, height= 52)
    self.button_option_3.place(x= 85.44+217.92+217.92, y= 298.56, width= 172, height= 52)
    self.button_option_4.place(x= 85.44+217.92+217.92+217.92, y= 298.56, width= 172, height= 52)
        
    self.button_exit.place(x= 0.27*96, y= 0.27*96, width= 0.37*96, height= 0.37*96)


    self.guess = tk.StringVar()
    
    self.text_answer = tk.Entry(self.frame, bd = 0, bg = "#BDD7EE", highlightthickness = 0, justify = tk.CENTER, font = (self.font_show, 20),
    show="", textvariable= self.guess)
    self.text_answer.focus_set()
    self.text_answer.bind("<Return>", self.continuer)

    self.text_answer.place(x = 181.44, y = 506.88, width = 636.48, height = 38.4)
    
    if self.lang == "Japanese":
      self.asd = self.exercise_bkgd.create_text(280,132, text= self.words[self.answers[self.right_answer]][1], font= (self.font_show, 11), tag= 'pin')
    
    buttons_list = [self.button_option_1, self.button_option_2, self.button_option_2, self.button_option_3, self.button_option_4]
    if self.diff == True:
      buttons_list += [self.button_option_5, self.button_option_6, self.button_option_7, self.button_option_8]

    for i in buttons_list:
      mmm = i.cget("text")
      if len(mmm) > 25:
        CreateToolTip(i, mmm)

  def pinyin(self):
    if self.disc == True:
      self.asd = self.exercise_bkgd.create_text(280,132, text= self.words[self.answers[self.right_answer]][3], font= (self.font_show, 11), tag= 'pin')
      self.disc = False
    else:
      self.exercise_bkgd.delete(self.asd)
      self.disc = True
    return 0

  def continuer(self, ans):
    if type(ans) == type(int()):
      if self.right_answer == ans-1:
        self.frame.destroy()
        self.dui += 1
        return inGame(self.master, self.words, user_data= self.user_data, language= self.lang, diff= self.diff, trad= self.trad, dui= self.dui, budui= self.budui, flip_= self.flip)
      else:
        self.budui += 1
    else:
      if self.guess.get() == self.words[self.answers[self.right_answer]][1] or self.guess.get() == self.words[self.answers[self.right_answer]][2]:
        self.frame.destroy()
        self.dui += 1
        return inGame(self.master, self.words, user_data= self.user_data, language= self.lang, diff= self.diff, trad= self.trad, dui= self.dui, budui= self.budui, flip_= self.flip)
      else:
        self.budui += 1
    return 0

  def go_back(self):
    import choose_lang as cl
    import pandas as pd
    import datetime
    import numpy as np

    record_data = pd.read_csv("./assets/stats/record_data.csv", index_col= 0)
    current = (record_data.iloc[(record_data["user_name"].tolist()).index(self.user_data["user_name"])]).to_dict()
    self.frame.destroy()
    
    last_days_check = [(datetime.date.today()-datetime.timedelta(days= 0 + x)).strftime("%Y/%m/%d") for x in range(7)]
    activity = [self.user_data["seventh_day"],  self.user_data["sixth_day"],  self.user_data["fifth_day"],  self.user_data["fourth_day"],  self.user_data["third_day"],  self.user_data["second_day"],  self.user_data["first_day"]]
    names = ["seventh_day", "sixth_day", "fifth_day", "fourth_day", "third_day", "second_day", "first_day",]

    for i, j in enumerate(last_days_check):
      if j == self.user_data["last_day_active"]:
        del activity[0:i]
        activity += [0] * i
        break
    else:
      activity = [0,0,0,0,0,0,0]
    
    for l, k in enumerate(names):
      self.user_data[k] = activity[l]

    self.user_data["correct_ans"] += self.dui
    self.user_data["wrong_ans"] += self.budui
    self.user_data["last_day_active"] = datetime.date.today().strftime("%Y/%m/%d")
    self.user_data["first_day"] += self.dui
    record_data.loc[(record_data["user_name"].tolist()).index(self.user_data["user_name"]), list(current.keys())] =  self.user_data
  
    record_data.to_csv("./assets/stats/record_data.csv")
    return cl.SelectLang(self.master, user_data= self.user_data)