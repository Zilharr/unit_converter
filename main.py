from tkinter import *
from tkinter import ttk

class Converter(Frame):
    def __init__(self, root, from_unit, to_unit, conversion_formula):
        super().__init__(root)
        self.pack()

        self.lbl_from_unit = Label(self, text=f"{from_unit}:")
        self.lbl_from_unit.grid(row=0, column=0)

        self.entry_from_unit = Entry(self)
        self.entry_from_unit.grid(row=0, column=1)
        self.entry_from_unit.bind("<KP_Enter>", self.convert)

        self.btn_convert = Button(self, text='Convert', command=self.convert)
        self.btn_convert.grid(row=0, column=2)

        self.lbl_to_unit = Label(self, text=f"{to_unit}:")
        self.lbl_to_unit.grid(row=1, column=0)

        self.result = Label(self)
        self.result.grid(row=1, column=1)

        self.conversion_formula = conversion_formula

    def convert(self, event=None):
        try:
            value = float(self.entry_from_unit.get())
            converted_value = self.conversion_formula(value)
            self.result.config(text=f"{converted_value:.4f}")
        except ValueError:
            self.result.config(text='Enter a valid number')

class Category():
    def __init__(self, root, frame):
        self.window = PanedWindow(root, orient=VERTICAL, borderwidth=2, relief='sunken')
        self.window.pack(expand=True, fill=BOTH)
        self.name_frame = LabelFrame(self.window, text=frame)
        self.window.add(self.name_frame)

def main():
    root = Tk()
    root.title('Unit Converter')

    distance_category = Category(root, 'Distance')
    distance_converter = Converter(distance_category.name_frame, 'Feet', 'Meters', lambda x: x * 0.3048)
    distance_converter.pack()

    inches_to_feet = Converter(distance_category.name_frame, 'Inches', 'Feet', lambda x: x / 12)
    inches_to_feet.pack()

    kilometer_to_miles = Converter(distance_category.name_frame, 'Kilometer', 'Miles', lambda x: x * 0.6213711922)
    kilometer_to_miles.pack()

    temperature_category = Category(root, 'Temperature')
    fahrenheit_to_celsius = Converter(temperature_category.name_frame, 'Fahrenheit', 'Celsius', lambda x: (x - 32) / 1.8)
    fahrenheit_to_celsius.pack()

    celsius_to_fahrenheit = Converter(temperature_category.name_frame, 'Celsius', 'Fahrenheit', lambda x: (x * 1.8) + 32)
    celsius_to_fahrenheit.pack()

    root.mainloop()

if __name__ == "__main__":
    main()