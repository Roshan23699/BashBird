import curses
import time
from menu import Menu
from write_mail import Write_Mail_UI
from show_folders import Show_Folders

'''Temporary function to check if passing function to dictionary is working'''
def temp(stdscr):
    # Get height and width of screen
    h, w = stdscr.getmaxyx()

    # Print that particular item at center of screen
    stdscr.clear()
    msg = "You entered into temporary  mode!"
    x_pos = w // 2 - len(msg) // 2
    y_pos = h // 2
    stdscr.addstr(y_pos, x_pos, msg)
    stdscr.refresh()

    # If backspace is pressed go back to menu
    # TODO: Later will need to switch this to some other key
    key = stdscr.getch()

    # While key is not backspace take input from user
    # TODO: Later delete this might cause problem
    while key != curses.KEY_BACKSPACE:
        key = stdscr.getch()

# TODO: Solve responsiveness issues
def show_main_intro(stdscr):
    title1 = "**************************************************"
    title2 = "***  TERMEMAIL - TERMINAL BASED EMAIL CLIENT!  ***"
    title3 = "**************************************************"
    h, w = stdscr.getmaxyx()
    stdscr.attron(curses.A_BOLD)
    x_pos = w // 2 - (len(title1) // 2)
    y_pos = h // 2 - 1
    stdscr.addstr(y_pos, x_pos, title1)
    stdscr.refresh()
    time.sleep(0.15)
    x_pos = w // 2 - (len(title2) // 2)
    y_pos = h // 2
    stdscr.addstr(y_pos, x_pos, title2)
    stdscr.refresh()
    time.sleep(0.15)
    x_pos = w // 2 - (len(title3) // 2)
    y_pos = h // 2 + 1
    stdscr.addstr(y_pos, x_pos, title3)
    stdscr.refresh()
    time.sleep(0.15)
    stdscr.refresh()
    time.sleep(1)
    while y_pos < h - 3:
        stdscr.clear()
        y_pos += 2
        stdscr.addstr(y_pos - 1, x_pos,title1)
        stdscr.addstr(y_pos, x_pos, title2)
        stdscr.addstr(y_pos + 1, x_pos, title3)
        stdscr.refresh()
        if y_pos < h - 6:
            stdscr.attron(curses.A_DIM)
        time.sleep(0.035)
    stdscr.clear()
    stdscr.refresh()
    stdscr.attroff(curses.A_DIM)
    stdscr.attroff(curses.A_BOLD)

'''Main menu class which shows main menu'''
class Main_Menu:
    __menu_strings = [ "Logout", "Exit"]
    __menu = []
    __stdscr = None
    '''Constructor of main menu'''
    # Arguements
    # stdscr    Standard screen
    def __init__(self, stdscr):
        self.__stdscr = stdscr
        menu = [{'title': "Write mail", 'Function': Write_Mail_UI}]
        menu.append({'title': "View mails", 'Function': Show_Folders})
        for item in self.__menu_strings:
            # Alert: Function will expect first arguement as stdscr for sure
            menu.append({'title': item, 'Function': temp})
        self.__menu = menu
    
    '''To show the menu'''
    def show(self):
        Menu(self.__stdscr, self.__menu, "Main menu", isMain=True)


def main(stdscr):
    curses.curs_set(0)
    show_main_intro(stdscr)
    # show the main menu
    main_menu = Main_Menu(stdscr)
    main_menu.show()



if __name__ == "__main__":
    curses.wrapper(main)