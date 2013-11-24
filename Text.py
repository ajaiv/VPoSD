import math# For performing the mathematical operations
import pylab

#Plotting the Band Diagrams of P-type and N-type


#Function to get the range and used in plotting
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

#Variables
Type_SC = 0
Type_Dopant = 0
Dopant_Level = 0
Dopant_Name = ''
Con_Na = 0
Con_Nd = 0
Con_A = 0
Con_B = 0
Con_Nd_Limit = 0
Con_Na_Limit = 0
Con_Intr = pow(10,10)
Con_N = 0
Con_P = 0
Intr_Ei = 0.5527
Fermi_Level = 0
#Fermi_N_Q = 0  Quasi Fermi level for non-equilibrium
#Fermi_P_Q = 0
#Plotting of Fermi level
x_axis = []
Ec_axis = []
Ev_axis = []
Ei_axis = []
Ef_axis = []
Ed_axis = []
Default_axis = []# for making Ev visible


# To get the SC type (N or P)
while 1 :
    Type_SC = int(input('Enter the type of Semiconductor\nPress \n\
1 : => for N-type \n\
2 : => for P-type \n\
3 : => for Intrinsic \n \n'))
    if Type_SC == 1 :
        print''
        #print '\n\nThe type of Semiconductor is : N -type \n'
        break
    elif Type_SC == 2 :
        print''
        #print '\n\nThe type of Semiconductor is : P -type \n'
        break
    elif Type_SC == 3 :
        print''
        #print '\n\nThe type of Semiconductor is : Intrinsic '
        break
    else :
        print '\nInvalid choice \nEnter the correct type \n'


# To get the Dopant and the Dopant_level
while 1 :
    if Type_SC == 1 :
        print('\nEnter the kind of dopant\nPress ')
        Type_Dopant = int(input('1 : => for Antimony (Sb) \n\
2 : => for Phosphorus (P) \n\
3 : => for Arsenic (As)\n'))
        # Donor_level in eV
        if Type_Dopant == 1 :
            Dopant_Name = 'Antimony'
            Dopant_Level = 0.039
            #print '\nThe kind of dopant is Antimony (Sb) '
        if Type_Dopant == 2 :
            Dopant_Name = 'Phosphorus'
            Dopant_Level = 0.045
            #print '\nThe kind of dopant is Phosphorus (P) '
        if Type_Dopant == 3 :
            Dopant_Name = 'Arsenic'
            Dopant_Level = 0.054
            #print '\nThe kind of dopant is Arsenic (As) '
        if Dopant_Level!= 0 :
            print''
            #print 'The value of Donor level is ', Dopant_Level, 'eV below Ec \n'
        else :
            continue
 
    elif Type_SC == 2 :
        print('\nEnter the kind of dopant\nPress ')
        Type_Dopant = int(input('1 : => for Boron (B) \n\
2 : => for Aluminium (Al) \n\
3 : => for Gallium (Ga)\n\
4 : => for Indium (In)\n'))
        # Dopant_level in eV
        if Type_Dopant == 1 :
            Dopant_Name = 'Boron'
            Dopant_Level = 0.045
            #print '\nThe kind of dopant is Boron (B) '
        if Type_Dopant == 2 :
            Dopant_Name = 'Aluminium'
            Dopant_Level = 0.067
            #print '\nThe kind of dopant is Aluminium (Al) '
        if Type_Dopant == 3 :
            Dopant_Name = 'Gallium'
            Dopant_Level = 0.072
            #print '\nThe kind of dopant is Gallium (Ga) '
        if Type_Dopant == 4 :
            Dopant_Name = 'Indium'
            Dopant_Level = 0.16
            #print '\nThe kind of dopant is Indium (In) '
        if Dopant_Level!= 0 :
            print ''
            #print 'The value of Acceptor level is' , Dopant_Level, 'eV above Ev \n'
        else :
            continue   
    break;

# To get the Dopant concentration
while 1 :
    if Type_SC == 1 :
        print 'The concentration of', Dopant_Name , ' in the form : \n   A * 10 ^ B'
        Con_A = float(input('\nEnter the value of \nA = ' ))
        Con_B = float(input('\nB = ' ))
        Con_Nd = Con_A * ( pow(10,Con_B))
        Con_Nd_Limit = 1.6*(pow(10,18))
        #Degeneracy condition
        if Con_Nd > Con_Nd_Limit :
            Con_Nd = 0
            print '\nThe material is heavily doped and is exceeding the degeneracy limit.\
 Please Enter a value below 1.6*10^18\n'
            continue
        # Acceptor concentration in N type
        if int(input('\nIs the material doped with Acceptor impurities ?. \
\nIf yes press \'1\' else \'0\' : ')) == 1:
            print '\nThe concentration of Acceptor in the form A * 10 ^ B'
            Con_A = float(input('\nEnter the value of \nA = ' ))
            Con_B = float(input('\nB = ' ))
            Con_Na = Con_A * ( pow(10,Con_B))
            Con_Na_Limit = 9.1*(pow(10,17))
            if Con_Na > Con_Na_Limit :
                Con_Na = 0
                print '\nThe material is heavily doped and is exceeding the degeneracy limit.\
 Please Enter a value below 9.1*10^17\n'
                continue
    if Type_SC == 2 :
        print 'The concentration of', Dopant_Name , ' in the form : \n   A * 10 ^ B'
        Con_A = float(input('\nEnter the value of \nA = ' ))
        Con_B = float(input('\nB = ' ))
        Con_Na = Con_A * ( pow(10,Con_B))
        Con_Na_Limit = 9.1*(pow(10,17))
        #Degeneracy condition
        if Con_Na > Con_Na_Limit :
            Con_Na = 0
            print '\nThe material is heavily doped and is exceeding the degeneracy limit.\
 Please Enter a value below 9.1*10^17\n'
            continue
        # Donor concentration
        if int(input('\nIs the material doped with Donor impurities ?. \
\nIf yes press \'1\' else \'0\' : ')) == 1:
            print '\nThe concentration of Donor in the form A * 10 ^ B'
            Con_A = float(input('\nEnter the value of \nA = ' ))
            Con_B = float(input('\nB = ' ))
            Con_Nd = Con_A * ( pow(10,Con_B))
            Con_Nd_Limit = 1.6*(pow(10,18))
            if Con_Nd > Con_Nd_Limit :
                Con_Nd = 0
                print '\nThe material is heavily doped and is exceeding the degeneracy limit.\
 Please Enter a value below 1.6*10^18\n'
                continue
    break



# To get the Value of Fermi Level

#Intrinsic
if Type_SC == 3 :
    print '''\n\n\n    Type of material                :   Intrinsic
    Material                        :   Silicon
    Temperature                     :   300 K
    Intrinsic concentration         :   10^10 /cm^3
    The Band Gap                    :   1.12 eV
    Ei - Intrinsic Level            :   0.5527 eV (0.0073eV below mid gap)\n
    Ef - Fermi level                :   0.5527 eV (Same as Ei)
    Donor concentration             :   0
    Acceptor concentration          :   0
    Concentration of electrons (n)  :   10^10 /cm^3
    Concentration of holes (p)      :   10^10 /cm^3'''

#Extrinsic - N Type
if Type_SC == 1 :
    if Con_Nd > Con_Na :
        Con_N = ((Con_Nd - Con_Na)/2.0) + pow((( (Con_Intr*Con_Intr) + pow(((Con_Nd - Con_Na)/2.0),2))),0.5)
        Con_P = (Con_Intr*Con_Intr)/Con_N
    elif Con_Nd < Con_Na :
        Con_P = ((Con_Na - Con_Nd)/2.0) + pow((( (Con_Intr*Con_Intr) + pow(((Con_Na - Con_Nd)/2.0),2))),0.5)
        Con_N = (Con_Intr*Con_Intr)/Con_P
    else :
        Con_P = pow(10,10)
        Con_N = pow(10,10)
    # Under Equilibrium Condition
    if Con_Nd == Con_Na :
        Fermi_Level = Intr_Ei
    else :
        Fermi_Level = Intr_Ei + 0.026 * ( math.log( Con_N / Con_Intr ))
    print '\n\n\n    Type of material                :   Extrinsic'
    print '    Dopant                          :  ', Dopant_Name
    print '    Dopant Level                    :  ', Dopant_Level, 'eV below Ec'
    print '''
    Substrate material              :   Silicon
    Temperature                     :   300 K
    Intrinsic concentration         :   10^10 /cm^3
    The Band Gap                    :   1.12 eV
    Ei - Intrinsic Level            :   0.5527 eV (0.0073eV below mid gap)\n\n'''
    print '    Ef -Fermi level                 :  ',round(Fermi_Level,3),'eV. (', 1.12 - round(Fermi_Level,3), 'eV below CB)'
    print '    Donor Concentration             :  ',Con_Nd , '  /cm^3'
    print '    Acceptor Concentration          :  ',Con_Na , '  /cm^3'
    print '    Concentration of electrons (n)  :  ',round(Con_N,3) , '  /cm^3'
    print '    Concentration of holes (p)      :  ',round(Con_P,3) , '  /cm^3'

    # Under Quasi Equilibrium condition (When a conc. Grad. occurs due to light etc)
    #Fermi_N_Q = Intr_Ei + 0.026* ( math.log((Con_N/Con_Intr)))
    #Fermi_P_Q = Intr_Ei - 0.026* ( math.log((Con_P/Con_Intr)))

    
#Extrinsic - P Type
if Type_SC == 2 :
    if Con_Na > Con_Nd :
        Con_P = ((Con_Na - Con_Nd)/2.0) + pow((( (Con_Intr*Con_Intr) + pow(((Con_Na - Con_Nd)/2.0),2))),0.5)
        Con_N = (Con_Intr*Con_Intr)/Con_P
    elif Con_Na < Con_Nd :
        Con_N = ((Con_Nd - Con_Na)/2.0) + pow((( (Con_Intr*Con_Intr) + pow(((Con_Nd - Con_Na)/2.0),2))),0.5)
        Con_P = (Con_Intr*Con_Intr)/Con_N
    else :
        Con_P = pow(10,10)
        Con_N = pow(10,10)
    # Under Equilibrium Condition
    if Con_Nd == Con_Na :
        Fermi_Level = Intr_Ei
    else :
        Fermi_Level = Intr_Ei + 0.026 * ( math.log( Con_N / Con_Intr ))
    print '\n\n\n    Type of material                :   Extrinsic'
    print '    Dopant                          :  ', Dopant_Name
    print '    Dopant Level                    :  ', Dopant_Level, 'eV above EV'
    print '''
    Substrate material              :   Silicon
    Temperature                     :   300 K
    Intrinsic concentration         :   10^10 /cm^3
    The Band Gap                    :   1.12 eV
    Ei - Intrinsic Level            :   0.5527 eV (0.0073eV below mid gap)\n\n'''
    print '    Ef -Fermi level                 :  ',round(Fermi_Level,3), 'eV above VB'
    print '    Acceptor Concentration          :  ',Con_Na , '  /cm^3'
    print '    Donor Concentration             :  ',Con_Nd , '  /cm^3'
    print '    Concentration of holes (p)      :  ',round(Con_P,3) , '  /cm^3'
    print '    Concentration of electrons (n)  :  ',round(Con_N,3) , '  /cm^3'

    
    # Under Quasi Equilibrium condition (When a conc. Grad. occurs due to light etc)
    #Fermi_N_Q = Intr_Ei + 0.026* ( math.log((Con_N/Con_Intr)))
    #Fermi_P_Q = Intr_Ei - 0.026* ( math.log((Con_P/Con_Intr)))

#Plotting of Fermi level
for i in my_range(1, 5, 0.05):
    x_axis.append((i))
    Ec_axis.append(1.12)
    Ev_axis.append(0.0)
    Ei_axis.append(0.5527)
    Ef_axis.append(Fermi_Level)
    Default_axis.append(-.00001)
    if Type_SC == 1 : 
        Ed_axis.append((1.12-Dopant_Level))
    if Type_SC == 2 :
        Ed_axis.append(Dopant_Level)
if Type_SC == 3 :
    pylab.title('Intrinsic Material')
else :
    pylab.title('Extrinsic Material')
pylab.plot(x_axis, Ec_axis, linewidth=1.0)
pylab.plot(x_axis, Default_axis)
pylab.plot(x_axis, Ev_axis , 'v')
pylab.plot(x_axis, Ei_axis , 'm')
if Type_SC == 3 :
    print '\n\n\nPlot is shown\n    Ec       : Blue\n    Ev       : Brown trianlgle\n    Ei       : Majanta'
else :
    pylab.plot(x_axis, Ed_axis , 'y')
    pylab.plot(x_axis, Ef_axis , 'x')
    print '\n\n\nPlot is shown\n    Ec          : Blue\n    Ev          : Brown trianlgle\n    Ei          : Majanta\n    Donor level : yellow\n    Fermi\
level : dots'
pylab.show()


