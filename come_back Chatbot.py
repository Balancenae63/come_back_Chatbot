from tkinter import font
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from getpass import getuser
import tkinter as tk
import tkinter.messagebox
import time    
import threading    
import random

root = tk.Tk()
root.geometry("330x115")
flag_blinking = False   
flag_exiting  = False   
prinTID   = str()
prinTPass = str()
getuserFB = getuser()
numLists = int()

listsRadio = tk.IntVar()
listsRadio.set(1)
liisDatatext = tk.StringVar()

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(options= opt)
driver.get("https://www.facebook.com/")


def blink():    
    global flag_blinking    
    global flag_exiting     
    global numLists
    theRandom = float()
    while ( True ):
        time.sleep(0.1)
        choiceList = listsRadio.get()
        if (flag_blinking == True):
            numLists = numLists + 1
            if choiceList == 3 :
                theRandom = random.choice([2.0,1.0,1.5,2.5,3.0])

            elif choiceList == 4 :
                theRandom = random.choice([0.4,0.6,1.0,])
            
            print(numLists)
            print(theRandom)    
            print("ส่ง")            
            time.sleep(theRandom)
            try:
                

                try:
                    clickeChats = "//div[@data-pagelet='BizP13NInboxUinifiedThreadListView']/div/div/div[4]"
                    clickChat = driver.find_element_by_xpath(clickeChats)
                    clickChat.click()
                    time.sleep(theRandom)
                    submitsChats = "textarea"
                    submitChat = driver.find_element_by_tag_name(submitsChats)
                    time.sleep(0.5)
                    submitChat.send_keys(liisDatatext.get(),"\n")
                except:
                    time.sleep(theRandom)
                    submitsChats = "textarea"
                    submitChat = driver.find_elements_by_tag_name(submitsChats)[2]
                    time.sleep(0.5)
                    submitChat.send_keys(liisDatatext.get(),"\n")
                    tkinter.messagebox.showinfo("แจ้งเตือนข้อผิดพลาด","การส่งข้อความล้มเหลวกรุณาแก้ไข")


            except:
                try:
                    print("ย้ายไปยังโฟลเดอร์แล้ว")
                    opperseihts = "//div[@data-tooltip-content='ย้ายไปที่โฟลเดอร์เรียบร้อย']"
                    oppersiht = driver.find_elements_by_xpath(opperseihts)[3]
                    oppersiht.click()
                    time.sleep(theRandom)
                except:
                    opperseihts = "//div[@data-tooltip-content='Move to done']"
                    oppersiht = driver.find_elements_by_xpath(opperseihts)[3]
                    oppersiht.click()
                    time.sleep(theRandom)
                    
        if (flag_exiting == True):  
            return   
        time.sleep(0.5)    

def  subImage():
    #update 
    pass

def switchon():      
    global flag_blinking    
    flag_blinking = True    
    print('flag_blinking on')
    thread = threading.Thread(target=blink)    
    thread.start()

def switchoff():      
    global flag_blinking    
    flag_blinking = False        
    print('flag_blinking off')    
          
def kill():   
    global flag_exiting     
    flag_exiting = True  
    root.destroy()

def startChrome():
    
    try:
        subId = driver.find_element_by_id("email")
        subId.send_keys(prinTID)

        subPass = driver.find_element_by_id("pass")
        subPass.send_keys(prinTPass)

        loginFb = driver.find_element_by_xpath("//button[@type='submit']")
        loginFb.click()

    except:
        time.sleep(3)
        driver.get("https://business.facebook.com/latest/inbox/")
        print("ไม่ได้ล็อกอิน")

def dataList():
    global prinTID
    global prinTPass
    global theRandom
    choice = listsRadio.get()
    if choice == 1:
        tkinter.messagebox.showinfo("แจ้งเตือน", "nameface")
        prinTID = "a"
        prinTPass = "b"
    elif choice == 2:
        tkinter.messagebox.showinfo("แจ้งเตือน", "nameface")
        prinTID = "a"
        prinTPass = "b"
    elif choice == 3:
        tkinter.messagebox.showinfo("แจ้งเตือน", "เริ่มบอทแบบช้า")

    elif choice == 4:
        tkinter.messagebox.showinfo("แจ้งเตือน", "เริ่มบอทแบบเร็ว")
    else:
        print("dataList Error submit massage")

def testBtn():
    print(liisDatatext.get())
#------------------------------------------------------------------------------------#
onbutton = tk.Button(root, text = "ON'Submit ", command = switchon)      
onbutton.place(x=135 , y=45 )      

offbutton =  tk.Button(root, text = "OFF'Submit", command = switchoff)      
offbutton.place(x=225 , y=45 )      

submitImage = tk.Button(root, text="Sub'Img", command= testBtn)
submitImage.place(x=200 , y=75 )

btnStart = tk.Button(root, text="Runing", command= startChrome)
btnStart.place(x=135 , y=75 )

killbutton = tk.Button(root, text = " EXIT ", command = kill)      
killbutton.place(x=275 , y=75 )
#------------------------------------------------------------------------------------#
confremlist = tk.Radiobutton(root, text="function1",
 variable=listsRadio, value=1,  command=dataList, fg="RED", font=28)
confremlist.place(x=10, y=5)

confremlist = tk.Radiobutton(root, text="function2",
 variable=listsRadio, value=2, command=dataList, fg="RED", font=28)
confremlist.place(x=10, y=25)

confremlist = tk.Radiobutton(root, text="แบบช้า",
 variable=listsRadio, value=3, command=dataList, fg="RED", font=28)
confremlist.place(x=10, y=45)

confremlist = tk.Radiobutton(root, text="แบบเร็ว",
 variable=listsRadio, value=4, command=dataList, fg="RED", font=28)
confremlist.place(x=10, y=65)

textBox = tk.Entry(width=20, textvariable=liisDatatext, font=28)
textBox.place(x=135, y=15)
#------------------------------------------------------------------------------------#
root.mainloop()