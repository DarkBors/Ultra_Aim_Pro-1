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


        
        
        # Logo (make sure to use the correct path for your logo)
        logo_path = r'G:\My Drive\Final Project Boris_E\Final Project\utils\rsz_11logo.png'
        self.logo_image = ImageTk.PhotoImage(Image.open(logo_path))
        self.logo_label = Label(self, image=self.logo_image)  # Changed to standard tk Label
        self.logo_label.grid(row=0, column=2)  # Adjust row/column as needed

        # Button to upload the data file
        upload_img = Image.open(r'G:\My Drive\Final Project Boris_E\Final Project\graphics\customtkinter-tutorial-master\Widgets\Button\upload.png')
        self.upload_button = ctk.CTkButton(self, text='Upload Data', command=self.upload_data,
                                           image=ctk.CTkImage(dark_image=upload_img, light_image=upload_img),
                                           corner_radius=10)
        self.upload_button.grid(row=1, column=2, pady=10, padx=10)

        # Label to show the file info
        self.file_info_label = ctk.CTkLabel(self, text='No file selected')
        self.file_info_label.grid(row=2, column=2, pady=10, padx=10)

        # Button to start the training
        train_img = Image.open(r'G:\My Drive\Final Project Boris_E\Final Project\graphics\customtkinter-tutorial-master\Widgets\Button\configuration.png')
        self.train_button = ctk.CTkButton(self, text='Train Model', state='disabled', command=self.train_model,
                                          image=ctk.CTkImage(dark_image=train_img, light_image=train_img),
                                          corner_radius=10)
        self.train_button.grid(row=3, column=2, pady=10, padx=10)

        # Visualization Panel (you will need to modify the VisualizationPanel to use customtkinter as well)
        self.visualization_panel = VisualizationPanel(self)
        self.visualization_panel.grid(row=4, column=2, pady=15, padx=15)

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
        if self.data:
            X_train, X_test, y_train, y_test, _ = self.data  # Unpack the preprocessed data
            self.model = NeuralNetworkModel(input_shape=(X_train.shape[1],))
            history = self.model.train(X_train, y_train)
            predictions = self.model.predict(X_test)

            # Plot the training/validation loss and predictions
            self.visualization_panel.plot_loss(history)
            self.visualization_panel.plot_predictions(y_test, predictions)

            # Evaluate the model
            r2, mse = self.model.evaluate(X_test, y_test)
            
            # Convert scores to percentage
            r2_score_percent = r2 * 100
            
            messagebox.showinfo('Model Evaluation', f'R^2 Score: {r2_score_percent:.4f}%\nMSE: {mse:.4f}')
        else:
            messagebox.showwarning('Warning', 'Please upload data before training.')

if __name__ == '__main__':
    root = MainWindow()
    root.mainloop()
