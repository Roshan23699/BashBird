# BashBird

## General Info:

BashBird is terminal based email client that lets you send and view emails from terminal. The app is written in python3 and uses socket programming under the hood to connect IMAP (to receive emails) and SMTP (to send emails) servers.

## Features:

-   Complete **terminal** based experience
-   Support for gmail, outlook and coep email account
-   Authenticate securely using SSL and STARTTLS
-   Send emails to multiple recipients.
-   Add multiple attachments (pdf, zip, images supported)
-   Multiple mailboxes
-   View emails by selecting mailbox
-   Delete emails
-   Download email attachments

## Getting Started:

#### Prerequisites:

1. Python3
2. Linux

#### Installing:

1. Install all the required dependencies:
    ```sh
    pip3 install -r requirements.txt
    ```

#### Usage:

1. Start using the app:
    ```sh
    python3 bashbird.py
    ```

#### Instructions:

1. Use the app in maximize window mode for optimal experience
2. [Check the IMAP](https://support.google.com/mail/answer/7126229?hl=en) is enabled for your gmail account
3. Follow login instructions page to login using your gmail account

> The app was tested on python version 3.8 and linux environment

## Screenshots

<div style={display: 'flex'}>
    <img src="Screenshots/1.png" alt="Intro Page" title="Intro Page"/>
    <img src="Screenshots/2.png" alt="Login Page" title="Login Page" />
    <img src="Screenshots/3.png" alt="Main menu Page" title="Main menu Page"/>
    <img src="Screenshots/4.png" alt="Write mail Page" title="Write mail Page"  />
    <img src="Screenshots/5.png" alt="Mailboxes Page" title="Mailboxes Page"   />
    <img src="Screenshots/6.png" alt="Email Page" title="Email Page"  />
    <img src="Screenshots/7.png" alt="Mail Details Page" title="Mail Details Page"  />
</div>
