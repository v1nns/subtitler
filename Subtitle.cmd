@echo off
cls
set PATH=%PATH%;C:\Users\USERNAME\AppData\Local\Programs\Python\Python36-32
:my_loop
IF %1 == "" GOTO completed
  rem executing script
  python C:\subtitler.py %1
  SHIFT
  GOTO my_loop
:completed
  PAUSE
