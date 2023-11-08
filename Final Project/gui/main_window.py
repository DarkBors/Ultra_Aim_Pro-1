# main_window.py
# This file creates the main window for the GUI.

import customtkinter as ctk
from tkinter import Label
from tkinter import filedialog, messagebox
from .visualization_panel import VisualizationPanel
from model.neural_network import NeuralNetworkModel
from data.preprocessing import preprocess_data
from PIL import Image, ImageTk

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Ultra_Aim_Pro')
        self.minsize(300, 200)
        ctk.set_appearance_mode("dark")  # Set the appearance mode

        # Configure the row and column weights to make the window responsive
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=1)  # Visualization panel row
        self.grid_columnconfigure(2, weight=1)


        # Define the parameters for the sliders
        self.slider_params = [
            {'row': 5, 'label_text': 'Dense Layer 1 Units:', 'from_': 16, 'to': 128, 'default_value': 64, 'number_of_steps': 113},
            {'row': 7, 'label_text': 'Dense Layer 2 Units:', 'from_': 16, 'to': 128, 'default_value': 32, 'number_of_steps': 113},
            {'row': 9, 'label_text': 'Learning Rate:', 'from_': 0.0001, 'to': 0.01, 'default_value': 0.001, 'number_of_steps': 1001},
            {'row': 11, 'label_text': 'Validation Split:', 'from_': 0.01, 'to': 0.2, 'default_value': 0.07, 'number_of_steps': 20},
            {'row': 13, 'label_text': 'Epochs:', 'from_': 100, 'to': 2000, 'default_value': 1000, 'number_of_steps': 20},
            {'row': 15, 'label_text': 'Batch Size:', 'from_': 16, 'to': 128, 'default_value': 77, 'number_of_steps': 113}
        ]

        # Create the sliders with entry boxes
        self.sliders = {}
        for params in self.slider_params:
            label, entry, slider = self.create_slider_with_entry(**params)
            self.sliders[params['label_text']] = {'label': label, 'entry': entry, 'slider': slider}

        
        
        # Logo (make sure to use the correct path for your logo)
        logo_path = r'G:\My Drive\Final Project Boris_E\Final Project\Ultra_Aim_Pro\Final Project\graphics\rsz_11logo.png'
        self.logo_image = ImageTk.PhotoImage(Image.open(logo_path))
        self.logo_label = Label(self, image=self.logo_image)  # Changed to standard tk Label
        self.logo_label.grid(row=0, column=0, columnspan=3, pady=10, padx=10)  # Adjust row/column as needed

        # Button to upload the data file
        upload_img = Image.open(r'G:\My Drive\Final Project Boris_E\Final Project\Ultra_Aim_Pro\Final Project\graphics\upload.png')
        self.upload_button = ctk.CTkButton(self, text='Upload Data', command=self.upload_data,
                                           image=ctk.CTkImage(dark_image=upload_img, light_image=upload_img),
                                           corner_radius=10)
        self.upload_button.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

        # Label to show the file info
        self.file_info_label = ctk.CTkLabel(self, text='No file selected')
        self.file_info_label.grid(row=2, column=0, columnspan=3, pady=10, padx=10)

        # Button to start the training
        train_img = Image.open(r'G:\My Drive\Final Project Boris_E\Final Project\Ultra_Aim_Pro\Final Project\graphics\configuration.png')
        self.train_button = ctk.CTkButton(self, text='Train Model', state='disabled', command=self.train_model,
                                          image=ctk.CTkImage(dark_image=train_img, light_image=train_img),
                                          corner_radius=10)
        self.train_button.grid(row=3, column=0, columnspan=3, pady=10, padx=10)

        # Visualization Panel (you will need to modify the VisualizationPanel to use customtkinter as well)
        self.visualization_panel = VisualizationPanel(self)
        self.visualization_panel.grid(row=4, column=0, columnspan=3, pady=15, padx=15)

        
    def create_slider_with_entry(self, row, label_text, from_, to, default_value, number_of_steps):
        # Label for the slider
        slider_label = ctk.CTkLabel(self, text=label_text)
        slider_label.grid(row=row, column=0, pady=10, padx=10, sticky='e')

        # Entry for the slider value
        slider_value_entry = ctk.CTkEntry(self, width=120)
        slider_value_entry.grid(row=row, column=1, pady=15, padx=15, sticky='w')
        slider_value_entry.insert(0, str(default_value))  # Set the default value

        # Slider
        slider = ctk.CTkSlider(self, from_=from_, to=to, number_of_steps=number_of_steps)
        slider.set(default_value)  # Set the default value
        slider.grid(row=row + 1, column=0, columnspan=3, pady=10, padx=10)

        # Bind the slider movement to update the entry
        def slider_moved(event):
            slider_value_entry.delete(0, ctk.END)
            slider_value_entry.insert(0, str(slider.get()))

        slider.bind('<B1-Motion>', slider_moved)
        slider.bind('<ButtonRelease-1>', slider_moved)

        # Bind the entry to update the slider
        def entry_changed(event):
            try:
                value = float(slider_value_entry.get())
                if from_ <= value <= to:
                    slider.set(value)
            except ValueError:
                pass  # If the entry is not a valid number, do nothing

        slider_value_entry.bind('<Return>', entry_changed)

        return slider_label, slider_value_entry, slider
        
        
        # Add labels for the sliders
        ctk.CTkLabel(self, text='Dense Layer 1 Units:').grid(row=5, column=1, pady=10, padx=10, sticky='e')
        ctk.CTkLabel(self, text='Dense Layer 2 Units:').grid(row=6, column=1, pady=10, padx=10, sticky='e')
        ctk.CTkLabel(self, text='Learning Rate:').grid(row=7, column=1, pady=10, padx=10, sticky='e')
        ctk.CTkLabel(self, text='Validation Split:').grid(row=8, column=1, pady=10, padx=10, sticky='e')
        ctk.CTkLabel(self, text='Epochs:').grid(row=9, column=1, pady=10, padx=10, sticky='e')
        ctk.CTkLabel(self, text='Batch Size:').grid(row=10, column=1, pady=10, padx=10, sticky='e')

        
        
        # Placeholder for data and model
        self.data = None
        self.model = None


    def upload_data(self):
        file_path = filedialog.askopenfilename(
            title='Select Dataset',
            filetypes=[('Excel Files', '*.xlsx'), ('All Files', '*.*')]
        )
        print(f"File path chosen: {file_path}")  # Debug print
        if file_path:
            try:
                # Update the file info label with the selected file
                self.file_info_label.configure(text=f'Selected: {file_path}')
                # Preprocess the data
                self.data = preprocess_data(file_path)
                print("Data preprocessed successfully.")  # Debug print
                # Enable the train button
                # self.train_button['state'] = 'normal'
                self.train_button.configure(state='normal')
                
            except Exception as e:
                messagebox.showerror('Error', f'An error occurred while loading the data: {e}')
                print(f"An error occurred: {e}")  # Debug print

                
    def train_model(self):
        # Retrieve slider values from the entry boxes
        dense1_units = int(self.sliders['Dense Layer 1 Units:']['entry'].get())
        dense2_units = int(self.sliders['Dense Layer 2 Units:']['entry'].get())
        learning_rate = float(self.sliders['Learning Rate:']['entry'].get())
        validation_split = float(self.sliders['Validation Split:']['entry'].get())
        epochs = int(self.sliders['Epochs:']['entry'].get())
        batch_size = int(self.sliders['Batch Size:']['entry'].get())
            
        if self.data:
            X_train, X_test, y_train, y_test, _ = self.data  # Unpack the preprocessed data
            # Assuming dense1_units, dense2_units, and learning_rate are meant to be keyword arguments:
            self.model = NeuralNetworkModel(input_shape=(X_train.shape[1],), dense1_units=dense1_units, dense2_units=dense2_units, learning_rate=learning_rate)
            history = self.model.train(X_train, y_train, validation_split, epochs, batch_size)
                
            predictions = self.model.predict(X_test)

            # Plot the training/validation loss and predictions
            self.visualization_panel.plot_loss(history)
            self.visualization_panel.plot_predictions(y_test, predictions)

            # Evaluate the model
            r2, mse = self.model.evaluate(X_test, y_test)
            
            # Convert scores to percentage and display them
            r2_score_percent = r2 * 100
            messagebox.showinfo('Model Evaluation', f'R^2 Score: {r2_score_percent:.4f}%\nMSE: {mse:.4f}')
        else:
            messagebox.showwarning('Warning', 'Please upload data before training.')

if __name__ == '__main__':
    root = MainWindow()
    root.mainloop()
