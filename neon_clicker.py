import tkinter as tk
import random

class ModerniHra:
    def __init__(self, root):
        self.root = root
        self.root.title("Neon Clicker 2026")
        self.root.geometry("600x500")
        self.root.configure(bg="#1e1e2e") # Tmavé pozadí (Catppuccin style)

        self.skore = 0
        
        # Horní panel se skóre
        self.label_skore = tk.Label(
            root, text=f"SKÓRE: {self.skore}", 
            font=("Segoe UI", 20, "bold"), 
            bg="#1e1e2e", fg="#fab387"
        )
        self.label_skore.pack(pady=20)

        # Herní plocha (Canvas) - vypadá lépe než čisté okno
        self.platno = tk.Canvas(
            root, width=500, height=300, 
            bg="#313244", highlightthickness=2, 
            highlightbackground="#cba6f7"
        )
        self.platno.pack(pady=10)

        # Vytvoření "terče" jako kruhu na plátně
        self.terc = self.platno.create_oval(
            0, 0, 50, 50, fill="#f38ba8", outline="#f5e0dc", width=2
        )
        
        # První náhodná pozice
        self.presun_terc()

        # Nabázání kliknutí na objekt na plátně
        self.platno.tag_bind(self.terc, "<Button-1>", self.pri_zasahu)

        # Spodní část pro jméno
        self.frame_input = tk.Frame(root, bg="#1e1e2e")
        self.frame_input.pack(side="bottom", pady=30)

        self.vstup = tk.Entry(
            self.frame_input, font=("Arial", 12), 
            bg="#45475a", fg="white", insertbackground="white", borderwidth=0
        )
        self.vstup.insert(0, "Tvé jméno...")
        self.vstup.pack(side="left", padx=10, ipady=5)

        self.btn_save = tk.Button(
            self.frame_input, text="ULOŽIT", command=self.ulozit,
            bg="#a6e3a1", fg="#11111b", font=("Arial", 10, "bold"),
            relief="flat", padx=20
        )
        self.btn_save.pack(side="left")

    def presun_terc(self):
        x = random.randint(10, 440)
        y = random.randint(10, 240)
        self.platno.coords(self.terc, x, y, x+50, y+50)
        
    def pri_zasahu(self, event):
        self.skore += 1
        self.label_skore.config(text=f"SKÓRE: {self.skore}")
        # Efekt změny barvy při kliku
        barvy = ["#f38ba8", "#fab387", "#f9e2af", "#a6e3a1", "#89b4fa"]
        self.platno.itemconfig(self.terc, fill=random.choice(barvy))
        self.presun_terc()

    def ulozit(self):
        jmeno = self.vstup.get()
        print(f"Hráč {jmeno} skončil se skóre {self.skore}")
        self.btn_save.config(text="HOTOVO", state="disabled", bg="#585b70")

if __name__ == "__main__":
    root = tk.Tk()
    hra = ModerniHra(root)
    root.mainloop()