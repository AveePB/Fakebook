@echo off

REM Navigate to the directory containing the virtual environment and Python script
cd /d %~dp0

REM Activate the virtual environment
call env\Scripts\activate

REM Run the Python script
python .\app.py

REM Pause to keep the window open
pause
