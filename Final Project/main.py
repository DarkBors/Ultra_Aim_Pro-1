# main.py
# This is the entry point of the application.


from gui.main_window import MainWindow
from app_logging import logger

# Now, use the logging in your main function
def main():
    logger.info("""ℹ️ Application Start :
                ###################################################################################
                ##                             ULTRA-AIM-PRO                                     ##
                ##                                                                               ##
                ## Ultra96-based PYNQ AI-Managed Performance and Reliability Optimization system ##
                ##                                                                               ##
                ##                  Created by: Dark Bors v2.0.0-Official                        ##
                ##                                                                               ##
                ##                                                                 Final Project ##
                ###################################################################################
                """)  # Log that the application has started
    try:
        app = MainWindow()
        app.mainloop()
        logger.info('ℹ️ Application Exit')  # Log that the application has exited
    except Exception as e:
        logger.exception('🐛 An exception occurred: ')  # This will log the exception with traceback

if __name__ == '__main__':
    main()
    