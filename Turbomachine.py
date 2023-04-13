import math
Va= float(input('please entre the value of Va: '))
alpha1= math.radians(float(input('please entre the value of alpha1: ')))
alpha2= math.radians(float(input('please entre the value of alpha2: ')))
beta2= math.radians(float(input('please entre the value of beta2: ')))
Rration= float(input('please entre the value of rr/rt: '))
rm= float(input('please entre the value of rm: '))
Tt1= float(input('please entre the value of Tt1 in Kelvin: '))
Pt1= float(input('please entre the value of Pt1 in Pascal: '))
Cp= float(input('please entre the value of Cp: '))
gamma= float(input('please entre the value of gamma: '))
r= float(input('please entre the value of r: '))


U= Va*(math.tan(alpha2)+math.tan(beta2))
w=U*Va*(math.tan(alpha2)-math.tan(alpha1))
print("The value of U is: ", U ," m/s")
print("The value of W is: ", w ," J/Kg")

rt=2*rm/(1+Rration)
rr= Rration*rt
S=math.pi*((rt**2)-(rr**2))
print("The value of the area S is: ", S ," k")
# print("The value of s is: ", w ," m2")
T1= Tt1-((Va**2)/(2*Cp))
print("The value of the static temperature T1 is: ", T1 ," k")
P1=Pt1/((Tt1/T1)**(gamma/gamma-1))
print("The value of the static pressure P1 is: ", P1 ," Pa")
Rau1= P1/(r *T1)
print("The value of the density Rau is: ", Rau1 ," Kg/m^3")
flowRate= Rau1*Va*S
print("The value of the flow rate mdot is: ", flowRate ," Kg/s")
P=w*flowRate
print("The value of power P is: ", P ," J/s")


