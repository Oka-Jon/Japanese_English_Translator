from tkinter import *
from googletrans import Translator

def translate_text():
    todo = to_translate.get("1.0", END)
    if lang_pick.get() == 1:
        new_text = translator.translate(todo, dest="ja")
    elif lang_pick.get() ==2:
        new_text = translator.translate(todo, dest="en")
    translated_text.delete("1.0", END)
    translated_text.insert(END, new_text.text)

translator = Translator()

window = Tk()
window.title("Jap->Eng / Eng->Jap Translator")
window.minsize(width=700, height=400)
window.config(padx=100, pady=50)

to_translate = Text(height=5, width=50)
to_translate.focus()
to_translate.insert(END, "Enter your text to translate here.")
to_translate.place(x=0, y=0)

lang_pick = IntVar()
lang1 = Radiobutton(text="English -> Japanese", value=1, variable=lang_pick)
lang2 = Radiobutton(text="日本語 -> 英語", value=2, variable=lang_pick)
lang1.place(x=400, y=0)
lang2.place(x=400, y=25)

translate_button = Button(text="Translate", command=translate_text)
translate_button.place(x=400, y=200)

translated_text = Text(height=5, width =50)
translated_text.place(x=0, y= 200)










window.mainloop()