import tkinter as tk
import threading
import subprocess
import time
import os

iconFile = r"Assets\Images\Communication\icons8-communication-60.ico"
platformIoFilePath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"platformio.exe")
currentWorkingDirectory = os.path.join(os.path.dirname(os.path.abspath(__file__)),"PlatformIoProject")
delayInSeconds = 0.01

def buildFileSystem():
    global outputText
    returnText = subprocess.run([platformIoFilePath, "run", "--target",
                                "buildfs", "--environment", "esp01_1m"],
                                shell = True,
                                cwd = currentWorkingDirectory,
                                capture_output = True,
                                text = True)
    for line in returnText.stdout.splitlines():
        outputText.config(state = "normal")
        outputText.insert(tk.END, f"{ line }\n")
        outputText.config(state = "disabled")
        outputText.yview_pickplace("end")
        time.sleep(delayInSeconds)
    buildButton.config(state = "normal")
    uploadButton.config(state = "normal")
    
    
def uploadFileSystem():
    global outputText
    returnText = subprocess.run([platformIoFilePath, "run", "--target",
                                "uploadfs", "--environment", "esp01_1m"],
                                shell = True,
                                cwd = currentWorkingDirectory,
                                capture_output = True,
                                text = True)
    for line in returnText.stdout.splitlines():        
        outputText.config(state = "normal")
        outputText.insert(tk.END, f"{ line }\n")
        outputText.config(state = "disabled")
        outputText.yview_pickplace("end")
        time.sleep(delayInSeconds)
    for line in returnText.stderr.splitlines():        
        outputText.config(state = "normal")
        outputText.insert(tk.END, f"{ line }\n")
        outputText.config(state = "disabled")
        outputText.yview_pickplace("end")
        time.sleep(delayInSeconds)
    buildButton.config(state = "normal")
    uploadButton.config(state = "normal")

def buildFileSystemCommand():
    outputText.config(state = "normal")
    outputText.delete("1.0", tk.END)
    outputText.config(state = "disabled")
    buildButton.config(state = "disabled")
    uploadButton.config(state = "disabled")
    threading.Thread(target = buildFileSystem).start()

def uploadFileSystemCommand():
    outputText.config(state = "normal")
    outputText.delete("1.0", tk.END)
    outputText.config(state = "disabled")
    buildButton.config(state = "disabled")
    uploadButton.config(state = "disabled")
    threading.Thread(target = uploadFileSystem).start()

def initializeWidgets():
    frame1 = tk.LabelFrame(root, padx = 10, pady = 10)
    frame1.grid(row = 0, column = 0, padx = 5, pady = 2)
    frame2 = tk.LabelFrame(root, padx = 10, pady = 10)
    frame2.grid(row = 1, column = 0, padx = 5, pady = 2)

    boardLabel = tk.Label(frame1, text = "Board:")
    boardLabel.grid(row = 0, column = 0, sticky = tk.E, padx = 5, pady = 5)
    boardValueLabel = tk.Label(frame1, text = "ESP01_1M")
    boardValueLabel.grid(row = 0, column = 1, sticky = tk.E, padx = 5, pady = 5)
    
    global buildButton
    buildButton = tk.Button(frame1, text = "Build", padx = 5,
                            command = buildFileSystemCommand)
    buildButton.grid(row = 1, column = 0, padx = 5, pady = 5)
    
    global uploadButton
    uploadButton = tk.Button(frame1, text = "Upload", padx = 5,
                            command = uploadFileSystemCommand)
    uploadButton.grid(row = 1, column = 1, padx = 5, pady = 5)
    
    global outputText
    outputText = tk.Text(frame2, state="disabled")
    outputText.grid(row = 0, column = 0)


root = tk.Tk()
root.title("File System Builder and Uploader")
root.iconbitmap(iconFile)

initializeWidgets()

root.mainloop()

