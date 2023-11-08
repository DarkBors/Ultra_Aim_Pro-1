# main_window.py
# This file creates the main window for the GUI..

from customtkinter import *
from tkinter import filedialog, messagebox
from .visualization_panel import VisualizationPanel  # Adjust the import according to your package structure
from model.neural_network import NeuralNetworkModel
from data.preprocessing import preprocess_data
from PIL import Image, ImageTk

class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.title('Ultra_Aim_Pro')
        self.minsize(300, 200)
        
        # Set dark mode for the entire application
        set_appearance_mode("dark")
        
        # Create the Tabview widget for tabbed interface
        self.tabview = CTkTabview(master=self)
        self.tabview.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        # Create the 'Main' tab
        self.main_tab = self.tabview.add("Main")
        
        # Create the 'Analyze' tab
        self.visualization_tab = self.tabview.add("Analyze")
        
        # Move the sliders and other widgets to the 'Main' tab
        self.create_main_tab_widgets()
        
        # Placeholder for data and model
        self.data = None
        self.model = None


    def create_main_tab_widgets(self):
        # Logo (make sure to use the correct path for your logo)
        logo_path = r'G:\My Drive\Final Project Boris_E\Final Project\Ultra_Aim_Pro\Final Project\graphics\rsz_11logo.png'
        logo_image = Image.open(logo_path)
        self.logo_image = ImageTk.PhotoImage(logo_image)  # Convert to PhotoImage
        self.logo_label = CTkLabel(self.main_tab, image=self.logo_image)
        self.logo_label.grid(row=0, column=0, columnspan=3, pady=10, padx=10)

        # Button to upload the data file
        upload_img = Image.open(r'G:\My Drive\Final Project Boris_E\Final Project\Ultra_Aim_Pro\Final Project\graphics\upload.png')
        self.upload_button = CTkButton(self.main_tab, text='Upload Data', command=self.upload_data,
                                           image=CTkImage(dark_image=upload_img, light_image=upload_img),
                                           corner_radius=10)
        self.upload_button.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

        # Label to show the file info
        self.file_info_label = CTkLabel(self.main_tab, text='No file selected', text_color="white")
        self.file_info_label.grid(row=2, column=0, columnspan=3, pady=10, padx=10)


        # Button to start the training
        train_img = Image.open(r'G:\My Drive\Final Project Boris_E\Final Project\Ultra_Aim_Pro\Final Project\graphics\configuration.png')
        self.train_button = CTkButton(self.main_tab, text='Train Model', state='disabled', command=self.train_model,
                                          image=CTkImage(dark_image=train_img, light_image=train_img),
                                          fg_color="#333333", hover_color="#444444", text_color="white", corner_radius=10)
        self.train_button.grid(row=3, column=0, columnspan=3, pady=10, padx=10)


        # Create the sliders with entry boxes in the 'Main' tab
        self.create_sliders_in_main_tab()

    def create_sliders_in_main_tab(self):
        # Define the parameters for the sliders
        slider_params = [
            {'row': 5, 'label_text': 'Dense Layer 1 Units:', 'from_': 16, 'to': 128, 'default_value': 64, 'number_of_steps': 113},
            {'row': 7, 'label_text': 'Dense Layer 2 Units:', 'from_': 16, 'to': 128, 'default_value': 32, 'number_of_steps': 113},
            {'row': 9, 'label_text': 'Learning Rate:', 'from_': 0.0001, 'to': 0.01, 'default_value': 0.001, 'number_of_steps': 1001},
            {'row': 11, 'label_text': 'Validation Split:', 'from_': 0.01, 'to': 0.2, 'default_value': 0.07, 'number_of_steps': 20},
            {'row': 13, 'label_text': 'Epochs:', 'from_': 100, 'to': 2000, 'default_value': 1000, 'number_of_steps': 20},
            {'row': 15, 'label_text': 'Batch Size:', 'from_': 16, 'to': 128, 'default_value': 77, 'number_of_steps': 113}
        ]

        # Create the sliders with entry boxes
        self.sliders = {}
        for params in slider_params:
            label = CTkLabel(self.main_tab, text=params['label_text'], text_color="white", fg_color="#333333")
            label.grid(row=params['row'], column=0, pady=10, padx=10, sticky='e')

            entry = CTkEntry(self.main_tab, width=120, fg_color="#333333", text_color="white")
            entry.grid(row=params['row'], column=1, pady=15, padx=15, sticky='w')
            entry.insert(0, str(params['default_value']))  # Set the default value

            slider = CTkSlider(self.main_tab, from_=params['from_'], to=params['to'], number_of_steps=params['number_of_steps'],
                                   fg_color="#333333", button_color="#555555", button_hover_color="#666666")
            
            slider.set(params['default_value'])  # Set the default value
            slider.grid(row=params['row'] + 1, column=0, columnspan=3, pady=10, padx=10)

            label, entry, slider = self.create_slider_with_entry(params)
            self.sliders[params['label_text']] = {'label': label, 'entry': entry, 'slider': slider}

    def create_slider_with_entry(self, params):
        # Label for the slider
        slider_label = CTkLabel(self.main_tab, text=params['label_text'])
        slider_label.grid(row=params['row'], column=0, pady=10, padx=10, sticky='e')

        # Entry for the slider value
        slider_value_entry = CTkEntry(self.main_tab, width=120)
        slider_value_entry.grid(row=params['row'], column=1, pady=15, padx=15, sticky='w')
        slider_value_entry.insert(0, str(params['default_value']))  # Set the default value

        # Slider
        slider = CTkSlider(self.main_tab, from_=params['from_'], to=params['to'], number_of_steps=params['number_of_steps'])
        slider.set(params['default_value'])  # Set the default value
        slider.grid(row=params['row'] + 1, column=0, columnspan=3, pady=10, padx=10)

        # Bind the slider movement to update the entry
        def slider_moved(event):
            slider_value_entry.delete(0, 'end')
            slider_value_entry.insert(0, str(slider.get()))

        slider.bind('<B1-Motion>', slider_moved)
        slider.bind('<ButtonRelease-1>', slider_moved)

        # Bind the entry to update the slider
        def entry_changed(event):
            try:
                value = float(slider_value_entry.get())
                if params['from_'] <= value <= params['to']:
                    slider.set(value)
            except ValueError:
                pass  # If the entry is not a valid number, do nothing

        slider_value_entry.bind('<Return>', entry_changed)

        return slider_label, slider_value_entry, slider

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
        epochs = int(float(self.sliders['Epochs:']['entry'].get()))
        batch_size = int(self.sliders['Batch Size:']['entry'].get())

        if self.data:
            X_train, X_test, y_train, y_test, _ = self.data  # Unpack the preprocessed data
            # Assuming dense1_units, dense2_units, and learning_rate are meant to be keyword arguments:
            self.model = NeuralNetworkModel(input_shape=(X_train.shape[1],), dense1_units=dense1_units, dense2_units=dense2_units, learning_rate=learning_rate)
            history = self.model.train(X_train, y_train, validation_split, epochs, batch_size)

            predictions = self.model.predict(X_test)

            # Plot the training/validation loss and predictions
            self.visualization_panel = VisualizationPanel(self.visualization_tab)
            self.visualization_panel.grid(row=0, column=0, sticky="nsew")  # Place the visualization panel in the 'Analyze' tab
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
