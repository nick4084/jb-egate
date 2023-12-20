@echo off
setlocal enabledelayedexpansion

color 0A
set "targetDirectory=C:/Users/nick4/Projects/jb-egate/config/" 
echo "###############################################"
echo "#     JB E-GATE AUTO FILLER                   #"
echo "###############################################"
echo "Select Users going to jb (eg. 1 or 1,2):"
:menu

set /a num=1


for %%f in ("%targetDirectory%\*.*") do (
    echo  !num!- %%~nf
    set /a num+=1
)

set /p people=Enter the people going [user listed below are configured in system]: 

if "%people%"=="" goto menu

:departure

set /p departureDate=Enter the departure date d-m-yyyy [eg. 30-9-2023 or 2-10-2023]: 
if "%departureDate%"=="" goto departure

:return_date

set /p returnDate=Enter the return date d-m-yyyy [enter] if returning on the same day: 
if "%returnDate%"=="" set returnDate=%departureDate%

for %%a in (!people!) do (
    set /a i=1
    
    for %%f in ("%targetDirectory%\*.*") do (
        if !i!==%%a (
            echo submitting %%~nf going jb from %departureDate% to %returnDate%
            py main.py %%~nf %departureDate% %returnDate%
        )
        set /a i+=1
    )
)
echo done
)