import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

def fahrenheit_to_celsius(inp):
	return (inp-32) * 5/9;

def convert_button_clicked():
	try:
		fahrenheit_input = float(temperature.get());
		fahrenheit_to_cel_res = fahrenheit_to_celsius(fahrenheit_input);		
		result = f'{fahrenheit_input} Fahrenheit = {fahrenheit_to_cel_res:.2f} Celsius';

		result_label.config(text=result);

	except ValueError as error:
		showerror(title='Error', message=error);


if __name__ == "__main__":
	root = tk.Tk();
	root.title('Celsius to Fahrenheit Converter');
	root.resizable(0, 0);
	root.geometry('300x200');

	frame = ttk.Frame(root);
	options = {'padx': 5, 'pady': 5};

	temperature_label = ttk.Label(frame, text="Fahrenheit");
	temperature_label.grid(column=0, row=0, sticky='W', **options);

	temperature = tk.StringVar();	
	temperature_inputBox = ttk.Entry(frame, textvariable=temperature);
	temperature_inputBox.grid(column=1, row=0, **options);
	temperature_inputBox.focus();


	bttn = ttk.Button(frame, text="Convert");
	bttn.grid(column=2, row=0, sticky='W', **options);


	result_label = ttk.Label(frame);
	result_label.grid(row=1, columnspan=3, **options);

	bttn.configure(command=convert_button_clicked);

	frame.grid(padx=10, pady=10);

	root.mainloop();