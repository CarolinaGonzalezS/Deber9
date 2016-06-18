import time 
hor=0
minu=0
seg=0
for dia in range(1,366):	
    for hor in range(0,24):   
        for minu in range(0,60):
            for seg in range(0,60):
                can='0'+str(seg)
                can1='0'+str(minu)
                can2='0'+str(hor)
                print("HORA ACTUAL")
                if minu<10 and seg<10 and hor<10:
                    print(can2,':',can1,':',can)
                
                else: 
                    if minu<10 and hor<10:
                        print(can2,':',can1,':',seg)
                    elif seg<10 and hor<10:
                        print(can2,':',minu,':',can)
                    elif minu<10 and seg<10:
                        print(hor,':',can1,':',can)
                    elif seg<10:                   
                        print(hor,':',minu,':',can)
                
                    elif minu<10:                   
                        print(hor,':',can1,':',seg)
                    elif hor<10:                   
                        print(can2,':',minu,':',seg)
                    else:
                        print(hor,':',minu,':',seg) 
                time.sleep(1)