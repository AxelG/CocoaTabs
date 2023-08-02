@echo off

REM
echo Installing dependencies...
pip install tk

REM
echo Installing dependencies...
pip install pyautogui

REM
echo Installing CocoaTabs v0.1.1...
python install.py

REM
echo Installing CocoaTabs v0.1.1...
del macos_installer.sh