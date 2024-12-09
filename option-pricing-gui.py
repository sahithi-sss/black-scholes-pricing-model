import tkinter as tk
from tkinter import ttk
import webbrowser
import os
import subprocess
import sys

class OptionPricingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Option Pricing Models")
        self.root.geometry("800x600")
        self.root.configure(bg='black')
        
        # Center the window on screen
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width/2) - (800/2)
        y = (screen_height/2) - (600/2)
        self.root.geometry(f'800x600+{int(x)}+{int(y)}')
        
        # Main frame
        main_frame = tk.Frame(root, bg='black')
        main_frame.pack(expand=True)
        
        # Introduction Text
        intro_text = """Option pricing is a fundamental concept in financial mathematics that determines the fair value of financial derivatives. 
        These mathematical models help traders and investors calculate theoretical values of options based on various factors like underlying asset price, 
        strike price, time to expiration, volatility, and interest rates. Different models account for various market conditions and assumptions: 
        Black-Scholes assumes log-normal distribution and constant volatility, Heston model incorporates stochastic volatility, 
        while Monte Carlo methods use simulation for complex scenarios. Jump diffusion models account for sudden price movements, 
        and tree models (binomial/trinomial) provide discrete-time approximations. Understanding these models is crucial for risk management 
        and trading strategies in options markets."""
        
        intro_label = tk.Label(
            main_frame,
            text=intro_text,
            bg='black',
            fg='white',
            wraplength=700,
            justify="center",
            font=('Arial', 11)
        )
        intro_label.pack(pady=20)
        
        # Models list and their corresponding files
        self.models = {
            "Black Scholes Option Pricing Model": "black-scholes-option-pricing-model.ipynb",
            "Binomial Options Pricing Model": "binomial-options-pricing-model.ipynb",
            "Heston Stochastic Volatility Model": "heston-stochastic-volatility-model.ipynb",
            "Merton Jump Diffusion Model": "merton-jump-diffusion-model.ipynb",
            "Trinomial Tree Model": "trinomial-tree-model.ipynb",
            "Monte Carlo Simulation": "monte-carlo-simulation.ipynb"
        }
        
        # Create links
        for model_name, file_name in self.models.items():
            link = tk.Label(
                main_frame,
                text=model_name,
                bg='black',
                fg='white',
                cursor='hand2',
                font=('Arial', 12, 'underline')
            )
            link.pack(pady=10)
            
            # Bind events for hover effect and click
            link.bind('<Enter>', lambda e, l=link: l.configure(fg='blue'))
            link.bind('<Leave>', lambda e, l=link: l.configure(fg='white'))
            link.bind('<Button-1>', lambda e, f=file_name: self.open_file(f))
    
    def open_file(self, filename):
        """Open the notebook file using the default application"""
        try:
            if sys.platform == 'win32':
                os.startfile(filename)
            elif sys.platform == 'darwin':  # macOS
                subprocess.run(['open', filename])
            else:  # linux variants
                subprocess.run(['xdg-open', filename])
        except Exception as e:
            print(f"Error opening file: {e}")

def main():
    root = tk.Tk()
    app = OptionPricingGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()