class chooseVocabularyJapanese:
  def __init__(self, master, user_data, language):
    import tkinter as tk
    self.master = master
    self.user_data = user_data
    self.language = language
    self.master.title("LangFlash - Level")

    self.frame = tk.Frame(self.master, bg= "white")
    self.frame.place(x= 0, y= 0, width=1000, height=600)

    # Bringing the images
    self.back_but = tk.PhotoImage(master= self.frame, file=f'./assets/back_button.png')
    self.optn_box = tk.PhotoImage(master= self.frame, file=f'./assets/in_game/option_box.png')
    self.img2 = tk.PhotoImage(master= self.frame, file= f"./assets/account/continue_blue.png")
    b2 = tk.Button(
      master= self.frame,
      image = self.img2,
      bg= 'white',
      borderwidth = 0,
      highlightthickness = 0,
      command = self.go_param,
      relief = "flat")
    b2.place(
      x = 500-138/2, y = 470,
      width = 138, height = 41)
    
    # Check Buttons **********TOP IMPORTANT*************
    self.n1 = tk.IntVar()
    self.n2 = tk.IntVar()
    self.n3 = tk.IntVar()
    self.n4 = tk.IntVar()
    self.n5 = tk.IntVar()

    button_N5 = tk.Checkbutton(
      self.frame, 
      bd= 0, bg= 'white', 
      text= 'N5', compound= 'center', font= ('DengXian',11,), 
      onvalue= 1, offvalue= 0, image= self.optn_box,
      variable= self.n5)
    button_N2 = tk.Checkbutton(
      self.frame, 
      bd= 0, bg= 'white', 
      text= 'N4', compound= 'center', font= ('DengXian',11,), 
      onvalue= 1, offvalue= 0, image= self.optn_box,
      variable= self.n2)
    button_N3 = tk.Checkbutton(
      self.frame, 
      bd= 0, bg= 'white', 
      text= 'N3', compound= 'center', font= ('DengXian',11,), 
      onvalue= 1, offvalue= 0, image= self.optn_box,
      variable= self.n3)
    button_N4 = tk.Checkbutton(
      self.frame, 
      bd= 0, bg= 'white', 
      text= 'N2', compound= 'center', font= ('DengXian',11,), 
      onvalue= 1, offvalue= 0, image= self.optn_box,
      variable= self.n4)
    button_N1 = tk.Checkbutton(
      self.frame, 
      bd= 0, bg= 'white', 
      text= 'N1', compound= 'center', font= ('DengXian',11,), 
      onvalue= 1, offvalue= 0, image= self.optn_box,
      variable= self.n1)
    button_back     = tk.Button(self.frame, image = self.back_but, bd= 0, bg= 'white', command= self.go_back)

    # Canvas
    exercise_text = tk.Canvas(self.frame, bd= 0, bg= 'white', highlightthickness= 0, relief= 'flat', height= 0.4*96, width= 5.51*96,)
    exercise_text.create_text(5.51*96/2, 0.4*96/2, font=('Montserrat',18), text= "Which level(s) do you want to practice?")

    # Placement
    exercise_text.place(x= 235, y= 30 )

    button_N5.place(
      x= (2.72+1.68+1.29)*96, y= (1.85+0.3+0.54)*96,
      width= 2*96, height= 0.54*96)
    button_N4.place(
      x= (1.15+1.68+1.29)*96, y= 1.85*96,
      width= 2*96, height= 0.54*96)
    button_N3.place(
      x= (1.15+1.68+1.68+1.29+1.29)*96, y= 1.85*96,
      width= 2*96, height= 0.54*96)
    button_N2.place(
      x= 2.72*96, y= (1.85+0.3+0.54)*96,
      width= 2*96, height= 0.54*96)
    button_N1.place(
      x= 1.15*96, y= 1.85*96,
      width= 2*96, height= 0.54*96)
    button_back.place (
      x= 0.27*96, y= 0.27*96,
      width= 0.45*96, height= 0.35*96)

  def word_set(self):
    import master_vocabulary as mv
    n1 = dict()
    n2 = dict()
    n3 = dict()
    n4 = dict()
    n5 = dict()
    
    if self.n1.get() == 1:
      n1 = dict()
      for key, values in mv.japanese_wordlist.items():
        if values[0] == 'N1':
          n1[key] = values
        else: pass
    if self.n2.get() == 1:
      n2 = dict()
      for key, values in mv.japanese_wordlist.items():
        if values[0] == 'N4':
          n2[key] = values
        else: pass
    if self.n3.get() == 1:
      n3= dict()
      for key, values in mv.japanese_wordlist.items():
        if values[0] == 'N3':
          n3[key] = values
        else: pass
    if self.n4.get() == 1:
      n4 = dict()
      for key, values in mv.japanese_wordlist.items():
        if values[0] == 'N2':
          n4[key] = values
        else: pass
    if self.n5.get() == 1:
      n5 = dict()
      for key, values in mv.japanese_wordlist.items():
        if values[0] == 'N5':
          n5[key] = values
        else: pass
    words = { **n1, **n2, **n3, **n4, **n5,}
    return words
    
  def go_param(self):
    words = self.word_set()
    from tkinter import messagebox
    if len(words) == 0:
      messagebox.showwarning("Warning", "You need to pick at least one option")
      pass
    else:
      import param
      self.frame.destroy()
      return param.Parameters(self.master, words, user_data= self.user_data, language= self.language)

  def go_back(self):
    import choose_lang as cl
    self.frame.destroy()
    return cl.SelectLang(self.master, self.user_data)