@echo off
echo Hardware Information:
echo.

echo CPU Serial Number:
wmic cpu get ProcessorId
echo.

echo GPU Serial Number:
wmic path win32_videocontroller get PNPDeviceID
echo.

echo RAM Serial Number:
wmic memorychip get SerialNumber
echo.

echo Disk Serial Number:
wmic diskdrive get SerialNumber
echo.

echo Motherboard Information
echo Motherboard Serial Number:
wmic baseboard get SerialNumber
echo.

echo HWID (UUID):
wmic csproduct get UUID
echo.

pause
