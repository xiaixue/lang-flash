class Parameters:
  def __init__(self, master, words, user_data, language):
    import tkinter as tk

    self.master = master
    self.language = language
    self.words = words
    self.user_data = user_data

    self.master.title("LangFlash - Settings")
    self.frame = tk.Frame(self.master, bg= "white")
    self.frame.place(x= 0, y= 0, width=1000, height=600)

    self.back_but = tk.PhotoImage(master= self.frame, file='./assets/back_button.png')
    self.optn_box = tk.PhotoImage(master= self.frame, file='./assets/in_game/option_box.png')
    self.flip_button_pic = tk.PhotoImage(master= self.frame, file= "./assets/flip.png")
    self.shff_button_pic = tk.PhotoImage(master= self.frame, file= "./assets/shffl.png")
    self.norm_button_pic = tk.PhotoImage(master= self.frame, file= "./assets/normal.png")

    self.exercise_text = tk.Canvas(self.frame, bd= 0, bg= 'white', highlightthickness= 0, relief= 'flat', height= 600, width= 1000,)
    self.exercise_text.create_text(3.49*96, 1.33*96, font=('Montserrat',18), text= "Do you want to practice just a set of words?")
    self.exercise_text.create_text(800, 1.33*96, font=('Montserrat',18), text= "Select difficulty")
    
    self.set_of_words = tk.IntVar()
    self.difficulty_chosen = tk.IntVar()
    self.style = tk.IntVar()
    button_back   = tk.Button(self.frame, image = self.back_but, bd= 0, bg= 'white', command= self.go_back)
    yes_button = tk.Radiobutton(self.frame, image= self.optn_box, bd= 0, bg= 'white', text= "Yes", compound= 'center', font= ('Montserrat',18), value= 1, variable= self.set_of_words, command= lambda: self.set_qst(True))
    nop_button = tk.Radiobutton(self.frame, image= self.optn_box, bd= 0, bg= 'white', text= "No", compound= 'center', font= ('Montserrat',18), value= 0, variable= self.set_of_words, command= lambda: self.set_qst(False))
    self.easy_option = tk.Radiobutton(self.frame, image = self.optn_box, bd= 0, bg= 'white', text= "Easy", compound= 'center', font= ('Montserrat',18), value = 0, variable= self.difficulty_chosen)
    self.hard_option = tk.Radiobutton(self.frame, image = self.optn_box, bd= 0, bg= 'white', text= "Hard", compound= 'center', font= ('Montserrat',18), value = 1, variable= self.difficulty_chosen)
    self.norm_button = tk.Radiobutton(self.frame, image= self.norm_button_pic, bd= 0, bg= "white", font= ("Montserrat", 18), variable= self.style, value= 0)
    self.flip_button = tk.Radiobutton(self.frame, image= self.flip_button_pic, bd= 0, bg= "white", font= ("Montserrat", 18), variable= self.style, value= 1)
    self.shff_button = tk.Radiobutton(self.frame, image= self.shff_button_pic, bd= 0, bg= "white", font= ("Montserrat", 18), variable= self.style, value= 2)

    self.img2 = tk.PhotoImage(master= self.frame, file= f"./assets/account/continue_blue.png")
    b2 = tk.Button(master= self.frame, image = self.img2, bg= 'white', borderwidth = 0, highlightthickness = 0, command = self.go_game, relief = "flat")
    b2.place(x = 280, y = 500, width = 138, height = 41)


    if language == 'Chinese':
      self.sim_trad = tk.IntVar()
      self.exercise_text.create_text(800, (2.37+1.33)*96, font=('Montserrat',18), text= "Phonetic system")
      self.trad_ico = tk.PhotoImage(master= self.frame, file='./assets/in_game/show_traditional.png') 
      self.simp_ico = tk.PhotoImage(master= self.frame, file='./assets/in_game/show_simplified.png')
      self.button_show_trad = tk.Radiobutton(self.frame, image=self.trad_ico, bg='#fff', bd= 0 , value= 0, variable= self.sim_trad)
      self.button_show_simp = tk.Radiobutton(self.frame, image=self.simp_ico, bd= 0, bg= '#fff', value= 1, variable= self.sim_trad)
      self.button_show_trad.place(x = 760, y = (2.37+1.33)*105, width = 100, height = 40)
      self.button_show_simp.place(x = 760, y = (2.37+1.33)*120, width = 100, height = 40)
    
    self.exercise_text.place(x= 0, y= 0 )
    button_back.place(x= 0.27*96, y= 0.27*96, width= 0.45*96, height= 0.35*96)
    yes_button.place(x= 3.49*80, y= 1.33*120, width= 200, height= 52)
    nop_button.place(x= 3.49*80, y= 1.33*190, width= 200, height= 52)
    self.flip_button.place(x= 780, y= 20, width= 80, height= 38)
    self.shff_button.place(x= 860, y= 20, width= 80, height= 38)
    self.norm_button.place(x= 700, y= 20, width= 80, height= 38)
    self.easy_option.place(x= 720, y= 1.33*120, width= 200, height= 52)
    self.hard_option.place(x= 720, y= 1.33*190, width= 200, height= 52)
      
      
  def go_back(self):
    self.frame.destroy()
    if self.language == "Chinese":
      import choose_zh as cz
      return cz.chooseVocabularyChinese(self.master, user_data= self.user_data, language= self.language)
    elif self.language == "Japanese":
      import choose_jp as cj
      return cj.chooseVocabularyJapanese(self.master, user_data= self.user_data, language= self.language)
    else:
      import choose_general as cg
      return cg.chooseGeneral(self.master, user_data= self.user_data, language= self.language)

  def set_qst(self, check):
    import tkinter as tk
    
    try:
        self.exercise_text.delete("question")
        self.text_answer.destroy()
    except: pass

    if check == True:
      self.exercise_text.create_text(320, (2.37+1.33)*96, font=('Montserrat',18), text= "How many words do you want to practice?", tags="question")
      self.amount = tk.StringVar()
      self.text_answer = tk.Spinbox(self.frame, bd = 0, bg = "#BDD7EE", highlightthickness = 0, justify = tk.CENTER, font = ('Consolas', 20), textvariable = self.amount, from_= 10, to= len(self.words.keys())-1)
      self.text_answer.place(x = 250, y = 400, width = 200, height = 40)
      self.text_answer.focus_set()
      self.text_answer.bind("<KeyRelease>", self.only_number)

  def only_number(self, e):
    inside = str(self.amount.get())
    if inside.isdigit() == True:
      if 10 <= float(inside) <= len(self.words.keys())-1:
        return 0
      elif 10 > float(inside): self.amount.set(10)
      else: self.amount.set(len(self.words.keys())-1)
    else: 
      self.amount.set(10)

  def go_game(self):
    import in_game as ig

    if self.difficulty_chosen.get() == 0: self.difficulty = False
    else: self.difficulty = True

    if self.set_of_words.get() == 1:
      import random as rnd

      amount = int(self.amount.get())
      keys = list(self.words.keys())
      new_words = dict()
      random_numbers = []
      while (len(random_numbers) < amount):
        words_index = rnd.choice(keys)
        if not words_index in random_numbers:
          random_numbers.append(words_index)
          keys.remove(words_index)
      
      for i in random_numbers:
        new_words[i] = self.words[i]
      
      self.words = new_words
      
    self.trad = False
    if self.language == "Chinese": 
      if int(self.sim_trad.get()) == 1:
        self.trad = False
      else:
        self.trad = True
        
    self.frame.destroy()
    return ig.inGame(self.master, self.words, user_data= self.user_data, language= self.language, diff= self.difficulty, trad= self.trad, flip_= self.style.get())