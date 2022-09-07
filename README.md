### **File System Builder and Uploader**
An alternative tool for building and updating a device file system running the Esp8266LiteTemplate without using Visual Studio Code PlatformIO via Serial or Over-the-air connection

[ESP 8266 Lite Template][Github Link]

---
<br />

**Sample File in the File System**
1. PlatformIoProject>data>config.json looks like this:
    * Used for setting up access point credentials to be used by ESP8266WiFiMulti library

        ```
        {
            "deviceType" : "ESP01",
            "accessPoint" : [
                                {
                                    "ssid": "WiFi1",
                                    "password": "12345"
                                },
                                {
                                    "ssid": "WiFi2",
                                    "password": "12345"
                                },
                                {
                                    "ssid": "WiFi3",
                                    "password": "12345"
                                }
                            ]
        }
        ```

---
<br />

**Platform IO Commands Called from VS Code PlatformIO IDE**
1. The commands are run inside the PlatformIO Project folder
1. Build File System
    ```
    C:\Users\user\.platformio\penv\Scripts\platformio.exe run --target buildfs --environment esp01_1m
    ```
1. Upload File System
    ```
    C:\Users\user\.platformio\penv\Scripts\platformio.exe run --target uploadfs --environment esp01_1m
    ```
    
---
<br />

**Perceived Challenges**
* Uses .platformio folder which has a size of 569 MB
    * Created a local copy of the C:\Users\user\\.platformio\penv\Scripts\platformio.exe file to the project folder and it worked.
    * No need to copy the entirety of the .platformio folder.
* References a PlatformIO Project template
    * Created a new PlaftformIO Project that generated a platformio.ini file.
    * A copy of the BasePlaformIoProject>platformio.ini file contents is added to the PlaftformIoProject>platformio.ini file.
    * Tested the build file system and upload file system commands and it worked.

---
<br />

**Localized Call of Platform IO Commands**
1. The commands are run inside of the PlatformIO Project folder
1. Build File System
    ```
    D:\DEV\FileSystemBuilderUploader\platformio.exe run --target buildfs --environment esp01_1m
    ```
1. Upload File System
    ```
    D:\DEV\FileSystemBuilderUploader\platformio.exe run --target uploadfs --environment esp01_1m
    ```

---
<br />

**FSBuilderUploaderExe Features**
1. Must be able to open the PlatformIoProject/platformio.ini file.
1. Must be able to display the PlatformIoProject/platformio.ini file.
1. Must be able to edit the PlatformIoProject/platformio.ini file.
1. Must be able to save the PlatformIoProject/platformio.ini file.
1. Must be able to open the PlatformIoProject/data/config.json file.
1. Must be able to display the PlatformIoProject/data/config.json file.
1. Must be able to edit the PlatformIoProject/data/config.json file.
1. Must be able to save the PlatformIoProject/data/config.json file.
1. Must be able to run the build file system command inside the PlatformIoProject folder.
1. Must be able to run the upload file system command inside the PlatformIoProject folder.

---
<br />

**Virtual Environment Setup**
1. Create a virtual environment:
    ```powershell
    py -m venv venv <# Syntax is py -m venv <Path\FolderNameOfVirtualEnvironment> #>
    ```
1. Run the batch file:
    ```powershell
    venv\Scripts\activate.bat
    ```
1. Open the Command Palette
1. Select the Python: Select Interpreter command
1. Select the python.exe under your workspace venv folder
1. Close the powershell terminal
1. Open a new powershell terminal to run your powershell commands in the virtual environment
1. (Optional) Upgrade pip:
    ```powershell
    py -m pip install --upgrade pip
    ```



---
<br />

<!-- Reusable and Invisible URL Definitions  -->
[Github Link]: https://github.com/lorenzmiranda05/Esp8266LiteTemplate