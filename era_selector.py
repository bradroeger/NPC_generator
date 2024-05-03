import os
import tkinter as tk
from tkinter import ttk
import subprocess
from tkinter.scrolledtext import ScrolledText
import imp

def get_era_files(path):
    era_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".py"):
                era_files.append(os.path.join(root, file))
    return era_files

def load_era_file(file_path):
    module_name = os.path.splitext(os.path.basename(file_path))[0]
    module = imp.load_source(module_name, file_path)
    return module

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Era Selector")
        self.pack(fill=tk.BOTH, expand=True)
        self.create_widgets()

    def create_widgets(self):
        # Left side: Era selection box
        self.era_label = tk.Label(self, text="Select an era:")
        self.era_label.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

        self.era_listbox = tk.Listbox(self, selectbackground="#90EE90", selectmode=tk.SINGLE)
        self.era_listbox.grid(row=1, column=0, sticky=tk.W + tk.E, padx=10, pady=10)
        self.era_listbox.bind("<Double-1>", self.on_era_double_click)  # Bind double-click event

        era_files = get_era_files("eras")

        for file_path in era_files:
            era_module = load_era_file(file_path)
            self.era_listbox.insert(tk.END, era_module.era_name)

        # Right side: Output display box
        self.output_text = ScrolledText(self, wrap=tk.WORD, width=80, height=20)
        self.output_text.grid(row=0, column=1, rowspan=2, sticky=tk.W + tk.E + tk.N + tk.S, padx=10, pady=10)

        # Button frame
        self.button_frame = tk.Frame(self)
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        # Quit button
        self.quit_button = ttk.Button(self.button_frame, text="Quit", command=self.master.destroy)
        self.quit_button.grid(row=0, column=0, padx=5)

        # Select button
        self.select_button = ttk.Button(self.button_frame, text="Select", command=self.get_selection)
        self.select_button.grid(row=0, column=1, padx=5)

        # Clear button
        self.clear_button = ttk.Button(self.button_frame, text="Clear", command=self.clear_output)
        self.clear_button.grid(row=0, column=2, padx=5)

    def on_era_double_click(self, event):
        # Double-click event handler for selecting an era
        selected_index = self.era_listbox.nearest(event.y)
        if selected_index >= 0:
            self.era_listbox.selection_clear(0, tk.END)
            self.era_listbox.selection_set(selected_index)
            self.get_selection()

    def get_selection(self):
        try:
            selected_item = self.era_listbox.get(self.era_listbox.curselection())
            os.environ["SELECTED_ERA"] = selected_item

            # Redirect standard output to the text widget
            import sys
            sys.stdout = TextRedirector(self.output_text, "stdout")

            # Run the Main.py script
            result = subprocess.run(["python3", "Main.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            # Display the result in the text widget
            self.output_text.insert(tk.END, result.stdout)
            self.output_text.insert(tk.END, result.stderr)

        except Exception as e:
            self.output_text.insert(tk.END, f"An error occurred: {str(e)}\n")

    def clear_output(self):
        # Clear the content of the output text widget
        self.output_text.delete(1.0, tk.END)

class TextRedirector:
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.insert(tk.END, str, (self.tag,))

    def flush(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
