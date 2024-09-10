HH, MM, SS = map(int, input().split(":"))
CH, CM, CS = map(int, input().split(":"))
HH -= 2
CH -= 7
BH, BM, BS= abs(HH - CH), abs(MM - CM), abs(SS - CS)
if(BH < 10):
    BH= f"0{BH}"
if(BM < 10):
    BM= f"0{BM}"
if(BS < 10):
    BS= f"0{BS}"
if(CH > HH or ( CH == HH and CM > MM) or (CH == HH and CM == MM and CS > MM)  ):
    print("See you on the next Pear Event!")
else:
    print(f"{BH}:{BM}:{BS}")