import webbrowser
#install flowing two package
#sudo apt-get install python-pip
#sudo pip install selenium

#function to open url

def openurl():
    webbrowser.get('firefox').open_new_tab('https://myaccount.google.com/lesssecureapps')
    return
#retype url which we want to open

openurl()

