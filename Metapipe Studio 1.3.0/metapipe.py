import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory, askopenfilename
import os
import shutil


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")

        self.sutun_1_veriler = ["f", "m"]
        self.sutun_2_veriler = ["tal", "med", "srt"]
        self.sutun_3_veriler = ["nrw", "unw"]

        self.sutun_1_cb = ttk.Combobox(self, values=self.sutun_1_veriler)

        self.sutun_2_cb = ttk.Combobox(self, values=self.sutun_2_veriler)

        self.sutun_3_cb = ttk.Combobox(self, values=self.sutun_3_veriler)

        self.sutun_4_secim = ttk.Entry(self)

        self.sutun_1_lbl = ttk.Label(self, text="Gender:")
        self.sutun_2_lbl = ttk.Label(self, text="Size:")
        self.sutun_3_lbl = ttk.Label(self, text="Type:")
        self.sutun_4_lbl = ttk.Label(self, text="MAYA VERSION(e.g. 2023 or 2022):")

        self.sonuc_btn = ttk.Button(self, text="Next", command=self.sonuc_goster)

        self.sutun_1_lbl.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        self.sutun_1_cb.grid(row=0, column=1, padx=10, pady=10)

        self.sutun_2_lbl.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        self.sutun_2_cb.grid(row=1, column=1, padx=10, pady=10)

        self.sutun_3_lbl.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.sutun_3_cb.grid(row=2, column=1, padx=10, pady=10)

        self.sutun_4_lbl.grid(row=3, column=0, padx=10, pady=10, sticky=tk.W)
        self.sutun_4_secim.grid(row=3, column=1, padx=10, pady=10)

        self.sonuc_btn.grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

    def sonuc_goster(self):
        sutun_1_secim = self.sutun_1_cb.get()
        sutun_2_secim = self.sutun_2_cb.get()
        sutun_3_secim = self.sutun_3_cb.get()
        sutun_4_secim = self.sutun_4_secim.get().replace("\\", "/")
        ROOT_DIR = askdirectory(title="Select ROOT DIR for dna_calib Path")
        dnaPath = askopenfilename(title="Select Metahuman Dna Path")
        body_type = "{}_{}_{}".format(sutun_1_secim, sutun_2_secim, sutun_3_secim)
        source_folder = os.path.dirname(os.path.abspath(__file__))
        MAYA_VERSION = sutun_4_secim
        self.codeblock(dnaPath, ROOT_DIR, body_type, MAYA_VERSION)
        self.move_files(source_folder, "c:/Arts and Spells/Scripts")

    def codeblock(self, dnaPath, ROOT_DIR, body_type, MAYA_VERSION):
        output_file_path = os.path.join("c:/Arts and Spells/Scripts", "dat.py")
        source_py = os.path.join(os.path.dirname(os.path.abspath(__file__)), "MetaPipeStudioSource.py")
        with open(source_py) as file:
            lines = file.readlines()
            lines = [line.replace('c:/dna_calibration', ROOT_DIR) for line in lines]
            lines = [line.replace("2023", MAYA_VERSION) for line in lines]
            lines = [line.replace("C:/Users/Uzay/Documents/Megascans Library/Downloaded/DHI/h344NMUV_asset/1k/asset_source/MetaHumans/CustomDNA/SourceAssets/CustomDNA.dna", dnaPath) for line in lines]
            lines = [line.replace("m_med_nrw", body_type) for line in lines]

        code_block = ''.join(lines)

        with open(output_file_path, "w") as output_file:
            output_file.write(code_block)

    def move_files(self, source_folder, destination_folder):
        files = os.listdir(source_folder)
        os.makedirs(destination_folder, exist_ok=True)

        for file_name in files:
            source = os.path.join(source_folder, file_name)
            destination = os.path.join(destination_folder, file_name)
            shutil.copy(source, destination)
            print(f"{file_name} moved.")
        return


if __name__ == '__main__':
    mw = MainWindow()
    mw.mainloop()
