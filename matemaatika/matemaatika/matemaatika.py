import random
print("proverka znanij!")
voprosq=int(input("skolko voprosov?"))
tase=int(input("vqberi tase (Tase 1, Tase 2, Tase 3): "))
if tase==1:
    num_range=(1, 10)
elif tase==2:
    num_range=(10, 100)
elif tase==3:
    num_range=(100, 1000)
else:
    print("nu togda vqberu za tebja - tase 2 budet")
    num_range = (10, 100)
dejstvija=['+', '-', '*', '/', '**']
prav_otvetq=0
for i in range(voprosq):
    dejstvie=random.choice(dejstvija)
    num1=random.randint(num_range[0], num_range[1])
    num2=random.randint(num_range[0], num_range[1])
    if dejstvie=='+':
        otvet=num1+num2
    elif dejstvie=='-':
        otvet=num1-num2
    elif dejstvie=='*':
        otvet=num1*num2
    elif dejstvie=='/':
        num2=random.randint(1, num_range[1])
        otvet=num1/num2
    elif dejstvie=='**':
        otvet=num1 ** num2
    print(f"skolko budet {num1} {dejstvie} {num2}?")
    tvoj_otvet=float(input("otvet: "))
    if tvoj_otvet==otvet:
        print("pravilno!")
        prav_otvetq+=1
    else:
        print("haha nepravilno!")
score=(prav_otvetq/voprosq)*100
print("\nkonec!")
print("tvoj score:", score)
if score<60:
    print("Hinne 2")
elif score<75:
    print("Hinne 3")
elif score<90:
    print("Hinne 4")
else:
    print("Hinne 5")
