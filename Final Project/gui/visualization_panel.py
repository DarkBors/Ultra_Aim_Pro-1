# visualization_panel.py
# This file defines the panel for data visualization.

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class VisualizationPanel(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.config(borderwidth=2, relief='sunken')

        # Create a figure for the loss plot
        self.loss_figure = Figure(figsize=(6, 4), dpi=100)
        self.loss_canvas = FigureCanvasTkAgg(self.loss_figure, master=self)
        self.loss_ax = self.loss_figure.add_subplot(111)
        
        # Create a figure for the prediction plot
        self.prediction_figure = Figure(figsize=(6, 4), dpi=100)
        self.prediction_canvas = FigureCanvasTkAgg(self.prediction_figure, master=self)
        self.prediction_ax = self.prediction_figure.add_subplot(111)

    def plot_loss(self, history):
        self.loss_ax.clear()
        self.loss_ax.plot(history.history['loss'], label='Train')
        self.loss_ax.plot(history.history['val_loss'], label='Validation')
        self.loss_ax.set_title('Model Loss')
        self.loss_ax.set_ylabel('Loss')
        self.loss_ax.set_xlabel('Epoch')
        self.loss_ax.legend(loc='upper right')
        self.loss_canvas.draw()
        self.loss_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def plot_predictions(self, y_test, predicted_reliability):
        self.prediction_ax.clear()
        self.prediction_ax.scatter(y_test, predicted_reliability)
        self.prediction_ax.set_xlabel('True Values [Reliability]')
        self.prediction_ax.set_ylabel('Predictions [Reliability]')
        self.prediction_ax.axis('equal')
        self.prediction_ax.axis('square')
        self.prediction_ax.plot([-100, 100], [-100, 100])  # Diagonal line for reference
        self.prediction_canvas.draw()
        self.prediction_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def clear_plots(self):
        # This will remove the canvases from the layout
        self.loss_canvas.get_tk_widget().pack_forget()
        self.prediction_canvas.get_tk_widget().pack_forget()
