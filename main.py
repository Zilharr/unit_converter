from tkinter import *
from tkinter import ttk

class Converter(Frame):
    def __init__(self, root, from_unit, to_unit, conversion_formula, alt_conversion_formula):
        super().__init__(root)
        self.from_unit = from_unit
        self.to_unit = to_unit
        self.pack()

        self.lbl_from_unit = Label(self, text=from_unit + ': ')
        self.lbl_from_unit.grid(row=0, column=0, padx=10)

        self.entry_from_unit = Entry(self)
        self.entry_from_unit.grid(row=0, column=2, padx=10)
        self.entry_from_unit.bind("<KP_Enter>", self.convert)

        self.btn_convert = Button(self, text='Convert', command=self.convert)
        self.btn_convert.grid(row=0, column=3)

        self.btn_switch = Button(self, text='Switch', command=self.switch)
        self.btn_switch.grid(row=0, column=4, padx=5)
        self.btn_switch_state = False

        self.lbl_to_unit = Label(self, text=to_unit + ': ')
        self.lbl_to_unit.grid(row=1, column=0)

        self.result = Label(self)
        self.result.grid(row=1, column=1)

        self.conversion_formula = conversion_formula
        self.alt_conversion_formula = alt_conversion_formula

    def convert(self, event=None):
        try:
            value = float(self.entry_from_unit.get())
            if self.btn_switch_state:
                converted_value = self.conversion_formula(value)
                self.result.config(text=f"{converted_value:.8f}")
            else:
                converted_value = self.alt_conversion_formula(value)
                self.result.config(text=f"{converted_value:.8f}")
        except ValueError:
            self.result.config(text='Enter a valid number')

    def switch(self, event=None):
        self.lbl_from_unit, self.lbl_to_unit = self.lbl_to_unit, self.lbl_from_unit
        self.lbl_from_unit.grid(row=0, column=0)
        self.lbl_to_unit.grid(row=1, column=0)
        self.btn_switch_state = not self.btn_switch_state

class Category():
    def __init__(self, root, frame):
        self.window = PanedWindow(root, orient=HORIZONTAL, borderwidth=2, relief='sunken')
        self.window.pack(side=LEFT, expand=True, fill=BOTH, padx=2, pady=2)
        self.name_frame = LabelFrame(self.window, text=frame)
        self.window.add(self.name_frame)

def main():
    root = Tk()
    root.title('Unit Converter')

    distance_category = Category(root, 'Distance')
    inches_to_centimeters = Converter(distance_category.name_frame, 'Inches', 'Centimeters', lambda x: x / 2.54, lambda x: x * 2.54)
    inches_to_centimeters.pack(padx=10, pady=10)

    inches_to_feet = Converter(distance_category.name_frame, 'Inches', 'Feet', lambda x: x * 12, lambda x: x / 12)
    inches_to_feet.pack(padx=10, pady=10)

    feet_to_meters = Converter(distance_category.name_frame, 'Feet', 'Meters', lambda x: x / 0.3048, lambda x: x * 0.3048)
    feet_to_meters.pack(padx=10, pady=10)

    kilometer_to_feet = Converter(distance_category.name_frame, 'Kilometer', 'Feet', lambda x: x / 3280.84, lambda x: x * 3280.84)
    kilometer_to_feet.pack(padx=10, pady=10)

    feet_to_miles = Converter(distance_category.name_frame, 'Feet', 'Miles', lambda x: x * 5280, lambda x: x / 5280)
    feet_to_miles.pack(padx=10, pady=10)

    kilometer_to_miles = Converter(distance_category.name_frame, 'Kilometer', 'Miles', lambda x: x * 1.60934, lambda x: x * 0.6213711922)
    kilometer_to_miles.pack(padx=10, pady=10)

    kilometer_to_AU = Converter(distance_category.name_frame, 'Kilometer', 'Astronomical Unit', lambda x: x * 149597870.7, lambda x: x / 149597870.7)
    kilometer_to_AU.pack(padx=10, pady=10)

    miles_to_AU = Converter(distance_category.name_frame, 'Miles', 'Astronomical Unit', lambda x: x * 92955807.27, lambda x: x / 92955807.27)
    miles_to_AU.pack(padx=10, pady=10)

    temperature_category = Category(root, 'Temperature')
    fahrenheit_to_celsius = Converter(temperature_category.name_frame, 'Fahrenheit', 'Celsius', lambda x: (x * 1.8) + 32, lambda x: (x - 32) / 1.8)
    fahrenheit_to_celsius.pack(padx=10, pady=10)

    kelvin_to_fahrenheit = Converter(temperature_category.name_frame, 'Kelvin', 'Fahrenheit', lambda x: (((x - 32) / 1.8) + 273.15), lambda x: (x * (9/5)) - 459.67)
    kelvin_to_fahrenheit.pack(padx=10, pady=10)

    kelvin_to_celsius= Converter(temperature_category.name_frame, 'Kelvin', 'Celsius', lambda x: x + 273.15, lambda x: x - 273.15)
    kelvin_to_celsius.pack(padx=10, pady=10)

    liquid_category = Category(root, 'Liquids')
    ounces_to_gallons = Converter(liquid_category.name_frame, 'Ounces', 'Gallons', lambda x: x * 128, lambda x: x / 128)
    ounces_to_gallons.pack(padx=10, pady=10)

    pint_to_gallons = Converter(liquid_category.name_frame, 'Pint', 'Gallons', lambda x: x * 8, lambda x: x / 8)
    pint_to_gallons.pack(padx=10, pady=10)

    quarts_to_gallons = Converter(liquid_category.name_frame, 'Quarts', 'Gallons', lambda x: x * 4, lambda x: x / 4)
    quarts_to_gallons.pack(padx=10, pady=10)

    teaspoon_to_tablespoon = Converter(liquid_category.name_frame, 'Teaspoon', 'Tablespoon', lambda x: x * 3, lambda x: x / 3)
    teaspoon_to_tablespoon.pack(padx=10, pady=10)

    gallons_to_liters = Converter(liquid_category.name_frame, 'Gallons', 'Liters', lambda x: x / 3.7854, lambda x: x * 3.7854)
    gallons_to_liters.pack(padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()