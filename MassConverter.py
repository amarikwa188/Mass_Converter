from tkinter import Tk, END
from tkinter.ttk import Entry, Label, Combobox, Button


class MassConverter:
    """
    Represents an instance of the mass converter application.
    """
    def __init__(self) -> None:
        """
        Initializes the application, sets up ui elements.
        """
        self.root = Tk()
        self.root.geometry("300x200+500+200")
        self.root.resizable(0, 0)
        self.root.title("Mass Converter")
        self.FONT = "Helvetica"

        self.value_label: Label = Label(self.root, text="Value:",
                                        font=(self.FONT, 11))
        self.value_label.place(relx=0.25, rely=0.1, anchor="center")

        self.value_entry: Entry = Entry(self.root)
        self.value_entry.place(relx=0.65, rely=0.1, anchor="center")
        self.value_entry.insert(0, "1")

        self.input_unit_label: Label = Label(self.root, text="Input Unit:",
                                             font=(self.FONT, 11))
        self.input_unit_label.place(relx=0.25, rely=0.3, anchor="center")

        conversion_options: list[str] = ["Tonne", "Kilogram", "Pound", "Ounce"]
        self.input_unit_combobox: Combobox = Combobox(self.root, state="readonly",
                                                      values=conversion_options)
        self.input_unit_combobox.place(relx=0.65, rely=0.3, anchor="center")
        self.input_unit_combobox.current(0)

        self.output_unit_label: Label = Label(self.root, text="Output Unit:", 
                                              font=(self.FONT, 11))
        self.output_unit_label.place(relx=0.25, rely=0.5, anchor="center")

        self.output_unit_combobox: Combobox = Combobox(self.root, state="readonly",
                                                       values=conversion_options)
        self.output_unit_combobox.place(relx=0.65, rely=0.5, anchor="center")
        self.output_unit_combobox.current(1)

        self.convert_button: Button = Button(self.root, text="Convert",
                                             command=self.convert)
        self.convert_button.place(relx=0.5, rely=0.7, anchor="center")

        self.result_text: Label = Label(self.root, text="Result: ---",
                                        font=(self.FONT, 12))
        self.result_text.place(relx=0.5, rely=0.9, anchor="center")
        
        self.conversion_data: dict[tuple, float] = {("Tonne", "Kilogram"): 1000,
                                               ("Kilogram", "Tonne"): 0.001,
                                               ("Tonne", "Pound"): 2204.62,
                                               ("Pound", "Tonne"): 0.000453592,
                                               ("Kilogram", "Pound"): 2.20462,
                                               ("Pound", "Kilogram"): 0.453592 ,
                                               ("Tonne", "Ounce"): 35274,
                                               ("Ounce", "Tonne"): 0.0000283495,
                                               ("Kilogram", "Ounce"): 35.274,
                                               ("Ounce", "Kilogram"): 0.0283495,
                                               ("Pound", "Ounce"): 16, 
                                               ("Ounce", "Pound"): 0.0625
                                               }

        self.root.mainloop()
    

    def convert(self) -> None:
        """
        Converts the set value from one given unit to the other.
        """
        first_unit: str = self.input_unit_combobox.get()
        second_unit: str = self.output_unit_combobox.get()

        try:
            input_value: float = float(self.value_entry.get())
        except ValueError:
            self.result_text.config(text="Invalid Value Input", 
                                    foreground="red")
            self.value_entry.delete(0, END)
            self.value_entry.insert(0, "1")
            input_value = 1.0
        else:
            if first_unit == second_unit:
                rate: float = 1
            else:
                conversion_pair: tuple[str] = (first_unit, second_unit)
                rate: float = self.conversion_data[conversion_pair]
            
            result: float = input_value * rate
            self.result_text.config(text=f"Result = {round(result, 4)} {second_unit}s",
                                    foreground="black")
        

if __name__ == "__main__":
    MassConverter()        