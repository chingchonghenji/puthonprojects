
import webbrowser
import os
import time

views=int(input("Enter number of views : "))
link=input("Enter a valid link : ")

os.system("C:\Program Files\Google\Chrome\Application\chrome.exe")
	
for _ in range(views):
	url= link
 
	webbrowser.open_new_tab(url)  


print(f"{link} has been visited {views} times!")

	
	

