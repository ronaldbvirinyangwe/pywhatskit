import pywhatkit
try:
    pywhatkit.sendwhatmsg("+263715431391","hello Python", 12,53)
    print("Successfully Sent!")
except:
    print("An Unexpected Error!")