class chooseVocabularyChinese:
  def __init__(self, master, user_data, language= "Chinese"):
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
    self.bhsk1 = tk.IntVar()
    self.bhsk2 = tk.IntVar()
    self.bhsk3 = tk.IntVar()
    self.bhsk4 = tk.IntVar()
    self.bhsk5 = tk.IntVar()
    self.bhsk6 = tk.IntVar()
    self.bhsk7 = tk.IntVar()
    self.bhsk8 = tk.IntVar()
    self.bhsk9 = tk.IntVar()

    button_hsk_1 = tk.Checkbutton(
      self.frame, 
      bd= 0, bg= 'white', 
      text= 'HSK 1', compound= 'center', font= ('DengXian',11,), 
      onvalue= 1, offvalue= 0, image= self.optn_box,
      variable= self.bhsk1)
    button_hsk_2 = tk.Checkbutton(
      self.frame, 
      bd= 0, bg= 'white', 
      text= 'HSK 2', compound= 'center', font= ('DengXian',11,), 
      onvalue= 1, offvalue= 0, image= self.optn_box,
      variable= self.bhsk2)
    button_hsk_3 = tk.Checkbutton(
      self.frame, 
      bd= 0, bg= 'white', 
      text= 'HSK 3', compound= 'center', font= ('DengXian',11,), 
      onvalue= 1, offvalue= 0, image= self.optn_box,
      variable= self.bhsk3)
    button_hsk_4 = tk.Checkbutton(
      self.frame, 
      bd= 0, bg= 'white', 
      text= 'HSK 4', compound= 'center', font= ('DengXian',11,), 
      onvalue= 1, offvalue= 0, image= self.optn_box,
      variable= self.bhsk4)
    button_hsk_5 = tk.Checkbutton(
      self.frame, 
      bd= 0, bg= 'white', 
      text= 'HSK 5', compound= 'center', font= ('DengXian',11,), 
      onvalue= 1, offvalue= 0, image= self.optn_box,
      variable= self.bhsk5)
    button_hsk_6 = tk.Checkbutton(
      self.frame, 
      bd= 0, bg= 'white', 
      text= 'HSK 6', compound= 'center', font= ('DengXian',11,), 
      onvalue= 1, offvalue= 0, image= self.optn_box,
      variable= self.bhsk6)
    button_hsk_7 = tk.Checkbutton(
      self.frame, 
      bd= 0, bg= 'white', 
      text= 'HSK 7', compound= 'center', font= ('DengXian',11,), 
      onvalue= 1, offvalue= 0, image= self.optn_box,
      variable= self.bhsk7)
    button_hsk_8 = tk.Checkbutton(
      self.frame, 
      bd= 0, bg= 'white', 
      text= 'HSK 8', compound= 'center', font= ('DengXian',11,), 
      onvalue= 1, offvalue= 0, image= self.optn_box,
      variable= self.bhsk8)
    button_hsk_9 = tk.Checkbutton(
      self.frame, 
      bd= 0, bg= 'white', 
      text= 'HSK 9', compound= 'center', font= ('DengXian',11,), 
      onvalue= 1, offvalue= 0, image= self.optn_box,
      variable= self.bhsk9)
    button_back = tk.Button(self.frame, image = self.back_but, bd= 0, bg= 'white', command= self.go_back)

    # Canvas
    exercise_text = tk.Canvas(self.frame, bd= 0, bg= 'white', highlightthickness= 0, relief= 'flat', height= 0.4*96, width= 5.51*96,)
    exercise_text.create_text(5.51*96/2, 0.4*96/2, font=('Montserrat',18), text= "Which level(s) do you want to practice?")

    # Placement
    exercise_text.place(x= 235, y= 30 )

    button_hsk_1.place(
        x= 1.15*96, y= 1.85*96,
        width= 2*96, height= 0.54*96)
    button_hsk_2.place(
        x= (1.15+1.68+1.29)*96, y= 1.85*96,
        width= 2*96, height= 0.54*96)
    button_hsk_3.place(
        x= (1.15+1.68+1.68+1.29+1.29)*96, y= 1.85*96,
        width= 2*96, height= 0.54*96)
    button_hsk_4.place(
        x= 1.15*96, y= (1.85+0.3+0.54)*96,
        width= 2*96, height= 0.54*96)
    button_hsk_5.place(
        x= (1.15+1.68+1.29)*96, y= (1.85+0.3+0.54)*96,
        width= 2*96, height= 0.54*96)
    button_hsk_6.place(
        x= (1.15+1.68+1.68+1.29+1.29)*96, y= (1.85+0.3+0.54)*96,
        width= 2*96, height= 0.54*96)
    button_hsk_7.place(
        x= 1.15*96, y= (1.85+0.3+0.54+0.3+0.54)*96,
        width= 2*96, height= 0.54*96)
    button_hsk_8.place(
        x= (1.15+1.68+1.29)*96, y=(1.85+0.3+0.54+0.3+0.54)*96,
        width= 2*96, height= 0.54*96)
    button_hsk_9.place(
        x= (1.15+1.68+1.68+1.29+1.29)*96, y= (1.85+0.3+0.54+0.3+0.54)*96,
        width= 2*96, height= 0.54*96)
    button_back.place (
        x= 0.27*96, y= 0.27*96,
        width= 0.45*96, height= 0.35*96)

  def word_set(self):
    import master_vocabulary as mv
    hsk1 = {} 
    hsk2 = {} 
    hsk3 = {}
    hsk4 = {} 
    hsk5 = {} 
    hsk6 = {} 
    hsk7 = {} 
    hsk8 = {} 
    hsk9 = {}
    
    if self.bhsk1.get() == 1:
      hsk1 = dict()
      for key, values in mv.chinese_wordlist.items():
        if values[0] == '1':
          hsk1[key] = values
        else: pass
    if self.bhsk2.get() == 1:
      hsk2 = dict()
      for key, values in mv.chinese_wordlist.items():
        if values[0] == '2':
          hsk2[key] = values
        else: pass
    if self.bhsk3.get() == 1:
      hsk3= dict()
      for key, values in mv.chinese_wordlist.items():
        if values[0] == '3':
          hsk3[key] = values
        else: pass
    if self.bhsk4.get() == 1:
      hsk4 = dict()
      for key, values in mv.chinese_wordlist.items():
        if values[0] == '4':
          hsk4[key] = values
        else: pass
    if self.bhsk5.get() == 1:
      hsk5 = dict()
      for key, values in mv.chinese_wordlist.items():
        if values[0] == '5':
          hsk5[key] = values
        else: pass
    if self.bhsk6.get() == 1:
      hsk6 = dict()
      for key, values in mv.chinese_wordlist.items():
        if values[0] == '6':
          hsk6[key] = values
        else: pass
    if self.bhsk7.get() == 1:
      hsk7 = dict()
      for key, values in mv.chinese_wordlist.items():
        if values[0] == '7':
          hsk7[key] = values
        else: pass
    if self.bhsk8.get() == 1:
      hsk8 = dict()
      for key, values in mv.chinese_wordlist.items():
        if values[0] == '8':
          hsk8[key] = values
        else: pass
    if self.bhsk9.get() == 1:
      hsk9 = dict()
      for key, values in mv.chinese_wordlist.items():
        if values[0] == '9':
          hsk9[key] = values
        else: pass
    words = { **hsk1, **hsk2, **hsk3, **hsk4, **hsk5, **hsk6, **hsk7, **hsk8, **hsk9}
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
    return cl.SelectLang(self.master, self.user_data)