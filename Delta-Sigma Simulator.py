#Simulation eines Delta-Sigma Wandlers
import matplotlib.pyplot as plt
out1=0; out2= 0; out3=0; out4=0; measure = 0; y=0
print("** Zu messende Spannung < 2 V, um Overflow zu vermeiden, Referenz unkritischer **\n")
n = int(input("Wie viele Durchläufe sollen erfolgen? "))
nn=n
measureStep=[]
volt=float(input("Spannung am Eingang: "))
ref=float(input("Referenzspannung: "))
print("\nDas Modell wird mit folgenden Daten durchlaufen: \n")
print("Zu messende Spannung: ", volt, " V", "Referenzspannung: ", ref, " V")
print("Es erfolgen ", n, " Durchläufe\n")

while n > 0:
    out1= volt-out4 #Summierknoten1 - DAC-Output
    out2= out2+out1 #Aktueller Wert des Integrators + Summierer-Output (out1)
    
    if out2 >=0:     #Diskriminator
        out3 = 1.0;
    else:
        out3 = 0;
    
    if out3 == 1.0:		#DAC Output (out4)
        out4 = ref;
    else:
        out4 = ref*(-1.0);
    #print("Index ist:  ",n)   
    measure = measure + out4 #Die Ausgangsspannung am DAC wird schrittweise addiert
    if nn-n != 0:
        y=measure/(nn-n)
    measureStep.append(y)
    print((nn-n),"Out1= ","%.4f" % out1, "| Out2= ","%.4f" % out2, "| Out3= ","%.4f" % out3, "| Out4= ","%.4f" % out4, "| Messw= ","%.4f" % measureStep[nn-n])
    n=n-1
   
measure = measure/nn #Mittelwert des DAC-Outputs wird ermittelt
measureStep.append(measure)
print("\n\nOut1= ", "%.4f" % out1, "| Out2= ", "%.4f" % out2, "| Out3= ","%.4f" % out3, "| Out4= ","%.4f" % out4, "| Messergebnis= ","%.4f" % measure)
      
print("\nSimulation abgeschlossen")

# Erstellen der X-Achse
x_values = range(len(measureStep))  # X-Achse von 0 bis zur Länge der Liste

# Erstellen des Plots
plt.plot(x_values, measureStep, marker='o')

# Achsentitel und Plot Titel
plt.title('Plot der Approximation')
plt.xlabel('Messung Nr.')
plt.ylabel('Messwert')

# Zeige den Plot
plt.grid()
plt.show()