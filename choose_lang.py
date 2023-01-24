class SelectLang():
  def __init__(self, master, user_data):
    import tkinter as tk

    self.master = master
    self.user_data = user_data
    self.master.title("LangFlash - Select Language")

    self.frame = tk.Frame(self.master, bg= "white")
    self.frame.place(x= 0, y= 0, width= 1000, height= 600)

    self.canvas = tk.Canvas(self.frame, bg = "white", bd = 0, height = 600, width = 1000, highlightthickness= 0, relief= 'flat')
    self.canvas.place(x = 0, y = 0, height = 600, width = 1000)
    self.background_img = tk.PhotoImage(master= self.frame, file = "./assets/choose_lang/choose_language_bg.png")
    self.canvas.create_image(550, 300, image= self.background_img)
    
    self.button_viet_img = tk.PhotoImage(master= self.frame, file="./assets/choose_lang/vietnamese_button.png")
    self.button_tglg_img = tk.PhotoImage(master= self.frame, file="./assets/choose_lang/tagalog_button.png")
    self.button_thai_img = tk.PhotoImage(master= self.frame, file="./assets/choose_lang/thai_button.png")
    self.button_chin_img = tk.PhotoImage(master= self.frame, file="./assets/choose_lang/chinese_button.png")
    self.button_japn_img = tk.PhotoImage(master= self.frame, file="./assets/choose_lang/japanese_button.png")
    self.button_kore_img = tk.PhotoImage(master= self.frame, file="./assets/choose_lang/korean_button.png")
    self.button_laos_img = tk.PhotoImage(master= self.frame, file="./assets/choose_lang/lao_button.png")
    self.button_khmr_img = tk.PhotoImage(master= self.frame, file="./assets/choose_lang/khmer_button.png")
    self.button_burm_img = tk.PhotoImage(master= self.frame, file="./assets/choose_lang/burmese_button.png")
    self.button_indn_img = tk.PhotoImage(master= self.frame, file="./assets/choose_lang/indonesian_button.png")
    self.exit_button     = tk.PhotoImage(master= self.frame, file="./assets/choose_lang/exit_button.png")
    self.stat_button     = tk.PhotoImage(master= self.frame, file="./assets/choose_lang/stats_button.png")

    # Creating the buttons and configuration
    self.button_exit = tk.Button(self.frame, image = self.exit_button, bd= 0, bg= 'white', command= lambda: self.go_back())
    self.button_stat = tk.Button(self.frame, image = self.stat_button, bd= 0, bg= 'white', command= lambda: self.go_stats())

    self.button_tglg = tk.Button(self.frame, borderwidth = 0, image= self.button_tglg_img, bd= 0, bg= 'white', highlightthickness = 0, relief = "flat",
      command= lambda: self.go_continue("Tagalog"))
    self.button_viet = tk.Button(self.frame, borderwidth = 0, image = self.button_viet_img, bd= 0, bg= 'white', highlightthickness = 0, relief = "flat",
      command= lambda: self.go_continue("Vietnamese"))
    self.button_thai = tk.Button(self.frame, borderwidth= 0, image= self.button_thai_img, bd= 0, bg= 'white', highlightthickness = 0, relief = "flat",
      command= lambda: self.go_continue("Thai"))
    self.button_chin = tk.Button(self.frame, borderwidth= 0, image= self.button_chin_img, bd= 0, bg= 'white', highlightthickness = 0, relief = "flat",
      command= lambda: self.go_continue("Chinese"))
    self.button_japn = tk.Button(self.frame, borderwidth= 0, image= self.button_japn_img, bd= 0, bg= 'white', highlightthickness = 0, relief = "flat",
      command= lambda: self.go_continue("Japanese"))
    self.button_kore = tk.Button(self.frame, borderwidth= 0, image= self.button_kore_img, bd= 0, bg= 'white', highlightthickness = 0, relief = "flat",
      command= lambda: self.go_continue("Korean"))
    self.button_laos = tk.Button(self.frame, borderwidth= 0, image= self.button_laos_img, bd= 0, bg= 'white', highlightthickness = 0, relief = "flat",
      command= lambda: self.go_continue("Lao"))
    self.button_khmr = tk.Button(self.frame, borderwidth= 0, image= self.button_khmr_img, bd= 0, bg= 'white', highlightthickness = 0, relief = "flat",
      command= lambda: self.go_continue("Khmer"))
    self.button_burm = tk.Button(self.frame, borderwidth= 0, image= self.button_burm_img, bd= 0, bg= 'white', highlightthickness = 0, relief = "flat", 
      command= lambda: self.go_continue("Burmese"))
    self.button_indn = tk.Button(self.frame, borderwidth= 0, image= self.button_indn_img, bd= 0, bg= 'white', highlightthickness = 0, relief = "flat", 
      command= lambda: self.go_continue("Indonesian"))

    self.button_tglg.place(x = 57.6, y = 469.44, width = 253, height = 51.84)
    self.button_viet.place(x = 57.6, y = 396.48, width = 253, height = 51.84)
    self.button_thai.place(x = 57.6, y = 323.52, width = 253, height = 51.84)
    self.button_chin.place(x = 57.6, y = 323.52-72.96-72.96, width = 253, height = 51.84)
    self.button_japn.place(x = 57.6, y = 323.52-72.96, width = 253, height = 51.84)
    self.button_kore.place(x = 355.2, y = 323.52-72.96-72.96, width = 253, height = 51.84)
    self.button_laos.place(x = 355.2, y = 323.52, width = 253, height = 51.84)
    self.button_khmr.place(x = 355.2, y = 323.52-72.96, width = 253, height = 51.84)
    self.button_burm.place(x = 355.2, y = 396.48, width = 253, height = 51.84)
    self.button_indn.place(x = 355.2, y = 469.44, width = 253, height = 51.84)
    self.button_exit.place(x= 0.27*96, y= 0.27*96, width= 0.37*96, height= 0.37*96)
    self.button_stat.place(x= 100, y= 0.27*96, width= 0.37*96, height= 0.37*96)
  
  def go_stats(self):
    import stats
    self.frame.destroy()
    return stats.Statistics(self.master, self.user_data)
  
  def go_back(self):
    import log_in as li
    self.frame.destroy()
    return li.LogIn(self.master)

  def go_continue(self, language):
    self.frame.destroy()
    if language == "Chinese": 
      import choose_zh as zh
      return zh.chooseVocabularyChinese(self.master, self.user_data, language)
    elif language == "Japanese": 
      import choose_jp as cj
      return cj.chooseVocabularyJapanese(self.master, self.user_data, language)
    else:
      import choose_general as cg
      return cg.chooseGeneral(self.master, self.user_data, language)