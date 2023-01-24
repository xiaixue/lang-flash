class chooseGeneral:
  def __init__(self, master, user_data, language):
    import tkinter as tk

    self.master = master
    self.user_data = user_data
    self.language = language

    self.master.title("LangFlash - Level")
    self.frame = tk.Frame(self.master, bg= "white")
    self.frame.place(x= 0, y= 0, width=1000, height=600)

    # Bringing the images
    self.back_but = tk.PhotoImage(master= self.frame, file='./assets/back_button.png')
    self.optn_box = tk.PhotoImage(master= self.frame, file='./assets/in_game/option_box.png')
    self.img2 = tk.PhotoImage(master= self.frame, file= "./assets/account/continue_blue.png")
    b2 = tk.Button(
      master= self.frame,
      image = self.img2,
      bg= 'white',
      borderwidth = 0,
      highlightthickness = 0,
      command = self.continuer,
      relief = "flat")
    b2.place(
      x = 500-138/2, y = 470,
      width = 138, height = 41)

    # Check Buttons **********TOP IMPORTANT*************
    self.level_1 = tk.IntVar()
    self.level_2 = tk.IntVar()
    self.level_3 = tk.IntVar()
    self.level_4 = tk.IntVar()
    self.level_5 = tk.IntVar()
    self.level_6 = tk.IntVar()

    button_a1 = tk.Checkbutton(
      self.frame, 
      bd= 0, bg= 'white', 
      text= 'A1', compound= 'center', font= ('DengXian',11,), 
      onvalue= 1, offvalue= 0, image= self.optn_box,
      variable= self.level_1)
    button_a2 = tk.Checkbutton(
      self.frame, 
      bd= 0, bg= 'white', 
      text= 'A2', compound= 'center', font= ('DengXian',11,), 
      onvalue= 1, offvalue= 0, image= self.optn_box,
      variable= self.level_2)
    button_b1 = tk.Checkbutton(
      self.frame, 
      bd= 0, bg= 'white', 
      text= 'B1', compound= 'center', font= ('DengXian',11,), 
      onvalue= 1, offvalue= 0, image= self.optn_box,
      variable= self.level_3)
    button_b2 = tk.Checkbutton(
      self.frame, 
      bd= 0, bg= 'white', 
      text= 'B2', compound= 'center', font= ('DengXian',11,), 
      onvalue= 1, offvalue= 0, image= self.optn_box,
      variable= self.level_4)
    button_c1 = tk.Checkbutton(
      self.frame, 
      bd= 0, bg= 'white', 
      text= 'C1', compound= 'center', font= ('DengXian',11,), 
      onvalue= 1, offvalue= 0, image= self.optn_box,
      variable= self.level_5)
    button_c2 = tk.Checkbutton(
      self.frame, 
      bd= 0, bg= 'white', 
      text= 'C2', compound= 'center', font= ('DengXian',11,), 
      onvalue= 1, offvalue= 0, image= self.optn_box,
      variable= self.level_6)
    
    button_back = tk.Button(self.frame, image = self.back_but, bd= 0, bg= 'white', command= self.go_back)

    # Canvas
    exercise_text = tk.Canvas(self.frame, bd= 0, bg= 'white', highlightthickness= 0, relief= 'flat', height= 0.4*96, width= 5.51*96,)
    exercise_text.create_text(5.51*96/2, 0.4*96/2, font=('Montserrat',18), text= "Which level(s) do you want to practice?")

    # Placement
    exercise_text.place(x= 235, y= 30 )

    button_a1.place(
        x= 1.15*96, y= 1.85*96,
        width= 2*96, height= 0.54*96)
    button_b1.place(
        x= (1.15+1.68+1.29)*96, y= 1.85*96,
        width= 2*96, height= 0.54*96)
    button_c1.place(
        x= (1.15+1.68+1.68+1.29+1.29)*96, y= 1.85*96,
        width= 2*96, height= 0.54*96)
    button_a2.place(
        x= 1.15*96, y= (1.85+0.3+0.54)*96,
        width= 2*96, height= 0.54*96)
    button_b2.place(
        x= (1.15+1.68+1.29)*96, y= (1.85+0.3+0.54)*96,
        width= 2*96, height= 0.54*96)
    button_c2.place(
        x= (1.15+1.68+1.68+1.29+1.29)*96, y= (1.85+0.3+0.54)*96,
        width= 2*96, height= 0.54*96)
    button_back.place (
        x= 0.27*96, y= 0.27*96,
        width= 0.45*96, height= 0.35*96)

  def word_set(self):
    import master_vocabulary as mv
    store_1 = {} 
    store_2 = {} 
    store_3 = {}
    store_4 = {} 
    store_5 = {} 
    store_6 = {}

    which = {"Burmese": 3, "Thai": 4, "Indonesian": 5, "Lao": 6, "Vietnamese": 7, "Khmer": 8, "Tagalog": 9, "Korean": 10}
    
    lang_id = which[self.language]
    upto = 3
    
    if self.level_1.get() == 1:
      store_1 = dict()
      for key, values in mv.master_vocabulary.items():
        if values[0] == 'a1':
          store_1[key] = values[:upto] + [values[lang_id]]
        else: pass
    if self.level_2.get() == 1:
      store_2 = dict()
      for key, values in mv.master_vocabulary.items():
        if values[0] == 'a2':
          store_2[key] = values[:upto] + [values[lang_id]]
        else: pass
    if self.level_3.get() == 1:
      store_3= dict()
      for key, values in mv.master_vocabulary.items():
        if values[0] == 'b1':
          store_3[key] = values[:upto] + [values[lang_id]]
        else: pass
    if self.level_4.get() == 1:
      store_4 = dict()
      for key, values in mv.master_vocabulary.items():
        if values[0] == 'b2':
          store_4[key] = values[:upto] + [values[lang_id]]
        else: pass
    if self.level_5.get() == 1:
      store_5 = dict()
      for key, values in mv.master_vocabulary.items():
        if values[0] == 'c1':
          store_5[key] = values[:upto] + [values[lang_id]]
        else: pass
    if self.level_6.get() == 1:
      store_6 = dict()
      for key, values in mv.master_vocabulary.items():
        if values[0] == 'c2':
          store_6[key] = values[:upto] + [values[lang_id]]
        else: pass
    
    words = { **store_1, **store_2, **store_3, **store_4, **store_5, **store_6}
    return words
    
  def continuer(self):
    words = self.word_set()
    from tkinter import messagebox
    if len(words) == 0:
      messagebox.showwarning("Warning", "You need to pick at least one option")
    else:
      import param
      self.frame.destroy()
      return param.Parameters(self.master, words, user_data= self.user_data, language= self.language)
  def go_back(self):
    import choose_lang as cl
    self.frame.destroy()
    return cl.SelectLang(self.master, user_data= self.user_data)