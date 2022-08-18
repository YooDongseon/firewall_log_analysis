for i in range(1, 21):
    with open(f"parse{i}.log",'w') as wf:
        with open(f"disk/firewall_{i}.log",'r') as rf:
            txt = rf.read()
            txt=txt.replace("Mon","\nMon")
            txt=txt.replace("Tue","\nTue")
            txt=txt.replace("Wed","\nWed")
            txt=txt.replace("Thu","\nThu")
            txt=txt.replace("Fri","\nFri")
            txt=txt.replace("Sat","\nSat")
            txt=txt.replace("Sun","\nSun")
            wf.write(txt)