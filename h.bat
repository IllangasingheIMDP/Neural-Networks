@echo off
for /f "tokens=2 delims= " %%i in ('adb shell ip addr show swlan0 ^| findstr "inet "') do set IP=%%i
echo %IP% | for /f "delims=/" %%j in ("!IP!") do set IP=%%j
echo %IP%
pause