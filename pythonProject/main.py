import pywhatkit
import pyautogui
import time

# Display ASCII Art Banner
print(r"""
/$$$$$$$   /$$$$$$  /$$      /$$ /$$$$$$$  /$$$$$$$$ /$$$$$$$ 
| $$__  $$ /$$__  $$| $$$    /$$$| $$__  $$| $$_____/| $$__  $$
| $$  \ $$| $$  \ $$| $$$$  /$$$$| $$  \ $$| $$      | $$  \ $$
| $$$$$$$ | $$  | $$| $$ $$/$$ $$| $$$$$$$ | $$$$$   | $$$$$$$/
| $$__  $$| $$  | $$| $$  $$$| $$| $$__  $$| $$__/   | $$__  $$
| $$  \ $$| $$  | $$| $$\  $ | $$| $$  \ $$| $$      | $$  \ $$
| $$$$$$$/|  $$$$$$/| $$ \/  | $$| $$$$$$$/| $$$$$$$$| $$  | $$
|_______/  \______/ |__/     |__/|_______/ |________/|__/  |__/

                                   By : Doraemon                                                                                                 
    Note : I won't be responsible for any damage caused by this script. Use at your own risk.
""")

# Function to send a WhatsApp message automatically
def send_whatsapp_message_automatically(phone_number, message):
    try:
        # Open WhatsApp Web and type the message
        pywhatkit.sendwhatmsg_instantly(phone_number, message, wait_time=10)  # Set a wait time for loading

        # Wait for a short period to ensure the message is typed
        #--------------#


        time.sleep(1)  # Reduced wait time to ensure the message is fully typed



        # Click the "Send" button
        pyautogui.click()  # Click the "Send" button

        print("Message sent successfully!")
    except Exception as e:
        print("An error occurred:", e)

# Input phone number and message in a hacker-style format
target_number = input("┌─[Enter Target Number (with country code, e.g., +8801XXXXXXXXX)]\n└──╼ $ ")
message_text = input("┌─[Enter Message to Send]\n└──╼ $ ")

# Loop for continuous message sending
while True:
    # Send the message automatically
    send_whatsapp_message_automatically(target_number, message_text)

    # Add a short delay before sending the next message



    time.sleep(1)  # Reduced wait time before sending the next message



    # Optional: Add a condition to break the loop if needed
