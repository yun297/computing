# Name: Zhu Yunsong(32)
# Class: 3A3
# File Name: IOFiles_Yunsong.py

def readA1():
    try:
        A1 = open('2022_sec3/python/17-1-22/A1.txt', 'r')
        print(A1.readline())
        print(A1.readline())
        print(A1.readline())
        A1.close()
    except IOError:
        print('There was an error opening the file!')
        return

def readA2():
    try:
        A2 = open('2022_sec3/python/17-1-22/A2.txt', 'r')
        S1 = A2.readline()
        S2 = A2.readline()
        S3 = A2.readline()
        S4 = A2.readline()
        A2.close()
    except IOError:
        print('There was an error opening the file!')
        return
    
def countLine():
    try:
        A1 = open('2022_sec3/python/17-1-22/A1.txt', 'r')
        A2 = open('2022_sec3/python/17-1-22/A2.txt', 'r')
        
        lineCountA1 = 0
        lineCountA2 = 0
        
        for linesA1 in A1.readlines():
            lineCountA1 += 1
            
        print('Number of lines in A1.txt:', lineCountA1)
        
        for linesA1 in A2.readlines():
            lineCountA2 += 1
            
        print('Number of lines in A2.txt:', lineCountA2)
        
        A1.close()
        A2.close()
    except IOError:
        print('There was an error opening the file!')
        return
    
def fileCreateB1():
    try:
        A1 = open('2022_sec3/python/17-1-22/A1.txt', 'r')
        A2 = open('2022_sec3/python/17-1-22/A2.txt', 'r')
        B1 = open('2022_sec3/python/17-1-22/B1.txt', 'w+')
        B1.write('3A1')
        B1.write('\nNumber of students: 32\n')
        
        B1.write('1 ANG YI ZHE\n2 CEDRIC CHUA YU XUAN\n3 CEDRIC TAI HONG E\n4 DU YUNTAO\n5 ETHAN CHEN YI\n6 FENG QINGDONG\n7 GAN WEI WEN\n8 GAN WILSON\n9 JULIAN OON KANGXIANG\n10 KAYDEN SEAH CHUNG HIAN\n11 KIM JUN YANG\n12 KOH ZANCONG\n13 LIN TAI LAI\n14 LIU BORAN\n15 LIU HAO RAN\n16 LOW JIT YIN ELGIN\n17 MA PEI KAI MARK\n18 NG ZHI JIAN\n19 NGOI CHENG YI\n20 NIU HONGRUI\n21 POH ZI QIAN ANDERSON\n22 SHI RUIQI\n23 SONG SHENGGUANG\n24 SUN PEIYAN\n25 TAN SHYAN ZHI\n26 TAN YU MING\n27 TEO ZHAN SHENG\n28 WANG ZITIAN\n29 YANG PENGRAN\n30 ZACHARY WONG\n31 ZHAO CHENGUANG\n32 ZHOU SHUOCHENG')
        
        A1.close()
        A2.close()
        B1.close()
    except IOError:
        print('There was an error opening/creating the file!')
        return
    
# readA1()

# readA2()

# countLine()

# fileCreateB1()
