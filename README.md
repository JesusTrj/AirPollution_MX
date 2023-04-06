# AirPollution_MX
Repository for air pollution study in Mexico gathering data from Open APIs. 

## Dev Environment
---
* MacOS, VSCode
* Windows, WSL, VSCode
* Python
    * Version: 3.10.4
    * Virtual environment creation with [Virtualenv - PyPI Project](https://pypi.org/project/virtualenv/)
    * .env for secrets storage

## VSCode Setup
---
### Pre-Checks
1. Be sure to already have installed VSCode on PC, if not download it from [Visual Studio Code Official Site](https://code.visualstudio.com/download).
2. Download & Install Python version 3.10.4 from [Python official releases](https://www.python.org/downloads/release/python-31004/), be sure to select the correct executable; preferred Windows Installer for 64 bit systems / macOS 64 bit Universal Installer.
3. Have installed a DBMS (Database Management System), we recommend using DBeaver Community, which can be installed from [Official Site](https://dbeaver.io/download/) or from Microsoft Store on Windows Systems.
4. Follow the next [instructions](https://support.atlassian.com/bitbucket-cloud/docs/
install-and-set-up-git/) to install git on PC.
5. Set [WSL + VSCode](https://code.visualstudio.com/docs/remote/wsl) in case of using Windows.
6. Being connected to a secure network, try not to be connected to public WiFi.
---
### Environment Setup
#### Clone Repository
1. With VSCode open press CTRL+Shift+P on Windows; CMD+Shift+P con MacOS.
2. Type "Clone" and select the first option, then click on "Clone from Github"
3. Select the option that states "JesusTrj/AirPollution_MX"
4. Choose a place to save the files and accept
#### Set Virtual Environment
1. Open a new terminal on VSCode
2. Run the following commands:
    ```
    pip install virtualenv
    virtualenv Air_Pollution_env
    ```
3. Activate virtual environment by running the next command on terminal
    ```
    ** Only available on MacOS & Windows-WSL **
    source Air_Pollution_env/bin/activate
    ```
4. Change the interpreter using CTRL+Shift+P / CMD+Shift+P and typing "Python: Select Interpreter" click on: *"Python 3.10.4 ('Air_Pollution_env':venv)"*
---
## Other options
### Requirements (Python)
* To load requirements:
    ```
    pip install -r requirements.txt
    ```
* To save requirements after installing new dependencies
    ```
    pip freeze > requirements.txt
    ```
### Deactivate & Delete Virtual Environment
1. Make sure virtual environment is activated.
2. Deactivate using the following command on terminal:
    ```
    deactivate
    ```
3. Delete environment from root lever folder:
    ```
    rm -r Air_Pollution_env
    ```

