# Name: myLib
# Version: 0.2.0
# Last Update: 2021.12.27 01:07UTC
# Creator: Mikpos(Mikolaj Ostrowski)
# Mail: mikolaj.p.ostrowski@gmail.com
# GitHub:
# License: Freeware
#
# This is library with useful functions:
#     NF-Not finished
#     Features:
#       COLORS:
#             colors are stored in consts.py
#             colors of console
#       NORMAL:
#       info(): return name and version
#             param1: if there is 'ver', will return only number of version
#       numberInfo(): return info about given number
#             param1: number
#             param2:
#                   '+' will return +,0,-,
#                   'b' will return true, if number is a number
#       startLogging():
#           param1: 0 or 1, 0 if you like to append data, 1 if you like to save in clear file or create this file
#           param2: name and directory of file
#       stopLogging(): closing file to save logs
#       loggingConfiguration(): configure logging settings(time format)
#       log():
#           param1: data to print in console and in log file
#
#       export():
#           param1: data to save
#           param2: 0 or 1, 0 if you like to append data, 1 if you like to save in clear file or create this file
#           param3: name and directory of file
#
#
#
#       PYGAME:
#       NF pginit(): Inicialize pygame packets
#       NF windowCreate(): create window
#             param1: name
#             param2: width
#             param3: height
#             param4: caption
#       exitPg(): check if keys to exit pygame window is clicked and exit programm

# import pygame as pg
import sys
import math as mt
import consts as cs
import time as tm
import logging


ver = "0.3.0"


# def init():
#     global dataPrintPgTable=[]

def info(verParam):
    if verParam == "ver":
        print(f'{ver}')
    else:
        print(f'myLib {ver}')

def startLogging(resetFile=0, fileName="log.txt"):
    global fileLog
    if resetFile == 1:
        fileLog = open(fileName, "w")
        fileLog.close()
    fileLog = open(fileName, "a")

def stopLogging():
    fileLog.close()

def loggingConfiguration():
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

def log(infoArg):
    #if fileLog.closed == True: NOT WORKING!!!
        #startLogging()
    logging.info(f'{cs.bcolors.OKGREEN}{infoArg}{cs.bcolors.ENDC}')
    fileLog.write(f'{tm.ctime()[11:19]}: {infoArg}\n')

def exportData(data, resetFile=0, fileName="exportedData.txt"):
    if resetFile == 1:
        fileExport = open(fileName, "w")
    else:
        fileExport = open(fileName, "a")
    fileExport.write(str(data))
    fileExport.close()

def numberInfo(number, param1):
    if param1 == 'b':
        try:
            number += 1
        except:
            return False
        return True

    elif param1 == '+' and numberInfo(number, 'b') == True:
        if number > 0:
            return '+'
        elif number == 0:
            return '0'
        elif number < 0:
            return '-'
    else:
        return '01 Error: Not a number'

# def pginit():
#     pg.init()
#     pg.font.init()
#
# def windowCreate(nameWinPg, width, height, caption):
#     global nameWinPg = pg.display.set_mode((width, height))
#     pg.display.set_caption(caption)
#
# def exitPg():
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             sys.exit(0)
#         elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
#             sys.exit(0)
#
# def dataPrintPgSetup(pos, font, color, spacing):
#     global posPrintPg=pos
#     global fontPrintPg=font
#     global colorPrintPg=color
#     global spacPrintPg=spacing
#
# def dataPrintPgAdd(text):
#     dataPrintPgTable.append(text)
#
# def dataPrintPg():
#     i=0
#     while i<len(dataPrintPgTable):
#         nameWinPg.blit(fontPrintPg.render(dataPrintPgTable[i], False, f'cs.{colorPrintPg}'), (posPrintPg[0],posPrintPg[1]+i*spacPrintPg))
#         i+=1
#     dataPrintPgTable.clear()

def pointCalc(x, y, ang, dist):
    x_end = 0.0
    y_end = 0.0
    if ang < 0:
        ang = 360 + ang

    if ang == 0 or ang == 360:
        x_end = x
        y_end = y + dist
    elif ang < 90:
        x_end = x + mt.sin(mt.radians(ang)) * dist
        y_end = y + mt.cos(mt.radians(ang)) * dist
    elif ang == 90:
        x_end = x + dist
        y_end = y
    elif ang < 180:
        x_end = x + mt.sin(mt.radians(ang)) * dist
        y_end = y - mt.cos(mt.radians(ang)) * dist
    elif ang == 180:
        x_end = x
        y_end = y - dist
    elif ang < 270:
        x_end = x - mt.sin(mt.radians(ang)) * dist
        y_end = y - mt.cos(mt.radians(ang)) * dist
    elif ang == 270:
        x_end = x - dist
        y_end = y
    elif ang < 360:
        x_end = x - mt.sin(mt.radians(ang)) * dist
        y_end = y + mt.cos(mt.radians(ang)) * dist
    return x_end, y_end
#angle = input(f'podaj kat: ')
#print(pointCalc(0, 0, int(angle), 10))

def execTime(arg1):
    start = 0
    stop = 0
    start = tm.perf_counter_ns()
    returnedValue = exec(arg1)
    stop = tm.perf_counter_ns()

    return str(returnedValue), stop-start




