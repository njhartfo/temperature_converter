import tkinter as tk

def fahrenheit_to_celsius():
    """
    Convert the value for Fahrenheit to Celsius and insert the result into lbl_result.
    """
    fahreinheit = ent_temperature.get()
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELCIUS}"

# Window creation    
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False,height=False)

# fahrenheit entry frame with entry widget and label
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# .grid() to set layout for temperature entry and label in frm_entry
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1,sticky="w")

# button to conrol conversion function and display result
btn_convert = tk.Button(
        master=window,
        text="\N{RIGHTWARDS BLACK ARROW}",
        command=fahrenheit_to_celsius
    )
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# .grid() to set layout for all elements
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# run app
window.mainloop()
