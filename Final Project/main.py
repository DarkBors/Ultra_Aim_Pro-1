# main.py
# This is the entry point of the application.
###################################################################################
##                             ULTRA-AIM-PRO                                     ##
##                                                                               ##
## Ultra96-based PYNQ AI-Managed Performance and Reliability Optimization system ##
##                                                                               ##
##                  Created by: Dark Bors v1.0.3-beta                           ##
##                                                                               ##
##                                                                 Final Project ##
###################################################################################

from gui.main_window import MainWindow

def main():
    app = MainWindow()
    app.mainloop()

if __name__ == '__main__':
    main()

