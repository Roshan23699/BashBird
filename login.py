import curses, time, sys
from curses.textpad import rectangle, Textbox
from BottomBar import BottomBar
from SMTP.main import SEND_MAIL
from threading import Thread
from main_menu import Main_Menu



class LOGIN_UI:


    #<!------------------------------------------Variables------------------------------------------------->
    __stdscr = None
    __x_start = 0
    __x_end = 0
    __y_start = 0
    __nol = 1
    __noc = 40
    __height = 1
    __width = 1
    __y_end = 0

    # To implement authentication loading
    # __is_authenticating = False

    # options for bottom bar which shows all the instructions to follow
    __options = [
        {'key': 'e', 'msg': 'Edit email'},
        {'key': 'p', 'msg': 'Enter password'},
        {'key': 'l', 'msg': 'Login'},
        {'key': 'q', 'msg': 'Exit program'},
        {'key': 'i', 'msg': 'Show Login Instructions'}
    ]

    #<!----------------------------------------------------Functions-------------------------------------->
    '''Constructor of class'''
    def __init__(self, stdscr):
        self.__stdscr = stdscr
        self.__set_values()
        self.__main()


    '''To set the default layout of login screen'''
    # Arguements:
    # email: Default email to show
    # password: Pasword to show
    # isEdit: If none don't show save message else show save message based on True or False value
    def __setup_layout(self, email, password, isEdit = None):
        self.__stdscr.clear()

        # Setting up title and padding rectangle
        rectangle(self.__stdscr, self.__y_start - 3, self.__x_start - 4, self.__y_end , self.__x_end + 6)
        title = " Login to your account ".upper()
        self.__stdscr.attron(curses.A_BOLD)
        self.__stdscr.addstr(self.__y_start - 3, self.__width // 2 - len(title) // 2 + 1, title)
        self.__stdscr.attroff(curses.A_BOLD)

        # Setting up view of email textbox
        self.__stdscr.attron(curses.A_BOLD)
        rectangle(self.__stdscr, self.__y_start, self.__x_start, self.__y_start + self.__nol + 1, self.__x_end + 2)
        email_msg = " Email: "
        if isEdit == False:
            email_msg += "(Ctrl + G to save) "
        self.__stdscr.addstr(self.__y_start, self.__x_start + 1, email_msg)

        # Setting up view of password textbox
        # TODO: Later add asterisk to editbox
        pass_start = self.__y_start + self.__nol + 3
        rectangle(self.__stdscr, pass_start, self.__x_start, pass_start + self.__nol + 1, self.__x_end + 2)
        password_msg = " Password: "
        if isEdit == True:
            password_msg += "(Ctrl + G to save) "
        self.__stdscr.addstr(pass_start, self.__x_start + 1, password_msg)
        self.__stdscr.attroff(curses.A_BOLD)

        # Add the email and password on screen
        self.__stdscr.addstr(self.__y_start + 1, self.__x_start + 2, email)
        self.__stdscr.addstr(self.__y_start + 5, self.__x_start + 2, password)

        # setup bottom bar
        BottomBar(self.__stdscr, self.__options)

        self.__stdscr.refresh()


    '''Edit box for login and password'''
    def __edit_box(self, email, password, posy, posx, isPass = False):
        curses.curs_set(1)
        # TODO: Use isPass to show asterisk for password
        nol = 1
        noc = 40
        editwin = curses.newwin(nol, noc, posy, posx)
        self.__setup_layout(email, password, isPass)
        if isPass:
            editwin.insstr(password)
        else:
            editwin.insstr(email)
        self.__stdscr.refresh()
        box_email = Textbox(editwin)
        box_email.stripspaces = True
        box_email.edit()
        curses.curs_set(0)
        return box_email.gather()


    '''Main function which setups the whole login page'''
    def __main(self):
        curses.curs_set(0)
        self.__setup_layout("", "")
        key = 1
        email = ""
        password = ""
        while key != ord('q'):
            
            key = self.__stdscr.getch()

            # If the key is e then make the email box active
            if key == ord('e'):
                email = self.__edit_box(email, password, self.__y_start + 1, self.__x_start + 2)
            
            # If the key is p then make the password box active
            elif key == ord('p'):
                password = self.__edit_box(email, password, self.__y_start + 5, self.__x_start + 2, isPass=True)
            
            elif key == ord('l'):
                # self.__is_authenticating = True
                self.__show_staus_message("Authenticating", isLoading=True)
                try:
                    SEND_MAIL(email, password)
                    self.__show_staus_message("Authentication Successful", time_to_show=1)
                    main_menu = Main_Menu(self.__stdscr)
                    main_menu.show()
                    # self.__is_authenticating = False
                    
                except Exception as e:
                    # self.__is_authenticating = False
                    self.__show_staus_message(str(e), time_to_show=4)

            # This is to refresh the layout when user resizes the terminal
            self.__set_values()
            self.__setup_layout(email, password)    

            self.__stdscr.refresh()
        sys.exit()


    #<!------------------------------------------------Utils------------------------------------------------->
    '''To show status message while authenticating'''
    # Arguements:
    # msg: Message to show
    # time_to_show: Time for which message needs to be shown
    # isLoading: If the text is related to loading
     # TODO: Implement loading also
    def __show_staus_message(self, msg, time_to_show = -1, isLoading=False):
        # Blink the text if it is in loading state
        if isLoading:
            self.__stdscr.attron(curses.A_BLINK)

        self.__stdscr.attron(curses.A_STANDOUT)
        self.__stdscr.attron(curses.A_BOLD)
        self.__stdscr.addstr(self.__height - 5, self.__width // 2 - len(msg) // 2, " " + str(msg) +  " ")
        self.__stdscr.refresh()
        if time_to_show != -1:
            time.sleep(time_to_show)

        self.__stdscr.attroff(curses.A_STANDOUT)
        self.__stdscr.attroff(curses.A_BOLD)

        if isLoading:
            self.__stdscr.attroff(curses.A_BLINK)
        



    '''To setup the default values'''
    def __set_values(self):

        # Set the value of height and width
        self.__height, self.__width = self.__stdscr.getmaxyx()

        # Starting x-coordinate
        self.__x_start = self.__width // 2 - self.__noc // 2 

        # Ending x-coordinate
        self.__x_end = self.__width // 2 + self.__noc // 2

        # Starting y-coordinate
        self.__y_start = self.__height // 2 - 3

        # Ending y-coordinate
        self.__y_end = self.__y_start + 9


def main(stdscr):
    LOGIN_UI(stdscr)

if __name__ == "__main__":
    curses.wrapper(main)