#For importing all the required files
from PyQt4 import QtGui
from PyQt4.QtGui import QStandardItemModel
from PyQt4.QtGui import QStandardItem
from PyQt4 import QtCore
import sys
from data_collector import Ui_MainWindow#The .py file created from PyQt4 .ui file
import pylab#For plotting
import math#For calculation

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None): #To initialise the values 
        
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)#setting data_collector
        self.a.setVisible(False)# Setting all visibility of Widgets in data_collector to false. 
        self.b.setVisible(False)
        self.lbl.setVisible(False)
        self.err_lbl.setVisible(False)
        self.textEdit.setVisible(False)
        self.plotBtn.setVisible(False)
        self.Name.setVisible(True)
        
        #Defining Values
        self.Con_Intr = pow(10, 10)
        self.Intr_Ei = 0.5527
        self.Fermi_Level = 0
        self.Con_Nd = 0
        self.Con_Na = 0
        self.Type_SC = 0
        self.Dopant_index = 0
        
        #Creating list of values which is to be used many times in the program
        self.semi_conductor = ["Intrinsic SC", "N -Type SC", "P -Type SC"]
        self.ntype_dopant = ["Antimony", "Phosphorus", "Arsenic"]
        self.ntype_dopant_level = [0.039, 0.045, 0.054]
        self.ptype_dopant = ["Boron", "Aluminium", "Gallium", "Indium"]
        self.ptype_dopant_level = [0.045, 0.067, 0.072, 0.16]
        
        #Setting Flag 
        self.flag = False
       
        #Used to present the list for user to select 
        self.populate_list(self.semi_conductor, "Double click : The type of Semiconductor :-")
        self.qlist.doubleClicked.connect(self.someMethod)# calling method someMethod
    
    @QtCore.pyqtSignature("")
    

    def on_plotBtn_clicked(self):#When plot button is clicked on result calls plot function
        self.plot_values()

    def populate_list(self, data, question):#Used to present the list for user to select
        
        self.label.setText(question)#passing Text to label.
        model = QStandardItemModel(self.qlist)#creates a qlist
        for val in data:
            item = QStandardItem(val)
            model.appendRow(item)
        self.qlist.setModel(model)
    
    def someMethod(self, item):#Starting of Program: when user double clicks 
        data = item.data().toString()#copies the velue
        
        if self.Type_SC == 0:#Initial step
            self.Type_SC = self.semi_conductor.index(data) + 1#Assigning value to Type_SC 
            if self.Type_SC == 1:#Intrinsic
                
                self.print_values()#Directly goes to Print result
                self.qlist.hide()#Hide qlist
                
            elif self.Type_SC == 2:
                self.populate_list(self.ntype_dopant, "Select dopant for N-type SC")#Passing next qlist for N-Type
            elif self.Type_SC == 3:
                self.populate_list(self.ptype_dopant, "Select dopant for P-type SC")#Passing next qlist for P-Type
                
        elif self.Type_SC == 2:
            self.Dopant_index = self.ntype_dopant.index(data)#getting dopant index
            self.qlist.hide() 
            self.label.setText("Concentration of "+self.ntype_dopant[self.Dopant_index]+"     (in the form of A*10^B))")
            self.label_2.setText("\n\n(value should be below 1.6*10^18)(Degeneracy Limit)")
            self.a.setVisible(True)#To enter value in the form A*10^B
            self.b.setVisible(True)
            self.lbl.setVisible(True)
            
        elif self.Type_SC == 3:
            self.Dopant_index = self.ptype_dopant.index(data)
            self.qlist.hide()  
            self.label.setText("Concentration of "+self.ptype_dopant[self.Dopant_index]+"      (in the form of A*10^B)")
            self.label_2.setText("\n\n(value should be below 9.1*10^17)(Degeneracy Limit)") 
            self.a.setVisible(True)#To enter value in the form A*10^B
            self.b.setVisible(True)
            self.lbl.setVisible(True)        
    
    def check_AB(self):#Ensures that the value entered is correct (A,B)
        
        val1 = str(self.a.text())#converts value entered to string 
        val2 = str(self.b.text())
        if val1 == "":#If box is empty then goes back to that box
            self.a.setFocus()
        elif val2 == "":
            self.b.setFocus()
        elif not self.is_float(val1):#If some string is entered (calls function)
            self.a.setText("")#clears box
            self.a.setFocus()
        elif not self.is_float(val2):
            self.b.setText("")
            self.b.setFocus()            
        else:
            if self.Type_SC == 2:
                
                if self.flag == False:#Already False
                    Con_Nd_Limit = 1.6*(pow(10,18))                
                    self.Con_Nd = float(val1) * ( pow(10,float(val2)))
                    if self.Con_Nd > Con_Nd_Limit:
                        
                        self.err_lbl.setVisible(True)#To pass error value                        
                        t = """The material is heavily doped and is exceeding the Degeneracy limit.
                        \nPlease Enter a value below 1.6*10^18 """                        
                        palette = QtGui.QPalette()
                        palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)#Red coloured alert
                        self.err_lbl.setPalette(palette)            
                        self.err_lbl.setText(t)
                        
                        self.a.setText("")#clears A B and ask again
                        self.b.setText("")
                        self.a.setFocus()
                    else:
                        val1 = "0"#Again asking user input
                        val2 = "0"
                        msg = "Is the material containing Accepter impurities"
                        self.ask_extra_impurity(msg)
                        
                else:#checks opposite concentration                  
                    self.Con_Na = float(val1) * ( pow(10,float(val2)))
                    Con_Na_Limit = 9.1*(pow(10,17))
                    
                    if self.Con_Na > Con_Na_Limit :
                        
                        self.err_lbl.setVisible(True)
                        t = """The material is heavily doped and is exceeding the Degeneracy limit.
                        \nPlease Enter a value below 9.1*10^17 """
                        palette = QtGui.QPalette()
                        palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
                        self.err_lbl.setPalette(palette)
                        self.err_lbl.setText(t)
                        
                        self.a.setText("")
                        self.b.setText("")
                        self.a.setFocus()                    
                    else:
                        self.print_all_values()
                        
                    
            elif self.Type_SC == 3:
                
                if self.flag == False:
                    self.Con_Na = float(val1) * ( pow(10,float(val2)))
                    Con_Na_Limit = 9.1*(pow(10,17))
                    if self.Con_Na > Con_Na_Limit:
                        
                        self.err_lbl.setVisible(True)
                        t = """The material is heavily doped and is exceeding the Degeneracy limit.
                        \nPlease Enter a value below 9.1*10^17 """
                        palette = QtGui.QPalette()
                        palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
                        self.err_lbl.setPalette(palette)
                        self.err_lbl.setText(t)

                        self.a.setText("")
                        self.b.setText("")
                        self.a.setFocus()
                    else:                        
                        val1 = "0"
                        val2 = "0"
                        msg = "Is the material containing Donor impurities"
                        self.ask_extra_impurity(msg)
                        
                else:
                       
                    Con_Nd_Limit = 1.6*(pow(10,18))                
                    self.Con_Nd = float(val1) * ( pow(10,float(val2)))
                    if self.Con_Nd > Con_Nd_Limit:
                        
                        self.err_lbl.setVisible(True)                        
                        t = """The material is heavily doped and is exceeding the Degeneracy limit.
                        \nPlease Enter a value below 1.6*10^18 """                        
                        palette = QtGui.QPalette()
                        palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
                        self.err_lbl.setPalette(palette)            
                        self.err_lbl.setText(t)
                        
                        self.a.setText("")
                        self.b.setText("")
                        self.a.setFocus()                                           
                    else:
                        self.print_all_values()
    
    def print_all_values(self):#Hide and to call print
        
        self.a.setVisible(False)
        self.b.setVisible(False)
        self.err_lbl.setVisible(False)
        self.label.setVisible(False)
        self.label_2.setVisible(False)
        
        print self.semi_conductor[self.Type_SC-1]#To print value in console 
        if self.Type_SC == 2:
            print self.ntype_dopant[self.Dopant_index]
            print self.ntype_dopant_level[self.Dopant_index]
        else:
            print self.ptype_dopant[self.Dopant_index]
            print self.ptype_dopant_level[self.Dopant_index]
        print self.Con_Na, self.Con_Nd
        
        self.print_values()
    
    def ask_extra_impurity(self, msg):#Ask for other kind of Dopant
        
        self.flag = True#Sets flag to True as first value is obtained
        self.err_lbl.setVisible(False)
        self.a.setText("")
        self.b.setText("")
        self.a.setFocus()
        
        reply = QtGui.QMessageBox.question(self, 'Ask',
            msg, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)#Message box appears        
        if reply == QtGui.QMessageBox.Yes:
            if self.Type_SC == 2:
                self.label.setText("Enter the concentration (in the form of A*10^B)")
                self.label_2.setText("\n\n(value should be below 9.1*10^17)(Degeneracy Limit)")
            if self.Type_SC == 3:
                self.label.setText("Enter the concentration (in the form of A*10^B)")
                self.label_2.setText("\n\n(value should be below 1.6*10^18)(Degeneracy Limit)")
        else:
            self.label.setVisible(False)#if not doped with opposite, hide all window
            self.label_2.setVisible(False)
            self.a.setVisible(False)
            self.b.setVisible(False)
            self.lbl.setVisible(False)
            self.print_all_values()#Print all values
   
    def on_a_returnPressed(self):#checks when A is pressed
        self.check_AB()
   
    def on_b_returnPressed(self):#checks when B is pressed        
        self.check_AB()        
    
    def is_float(self, str):#Checks input to be float and returns TRUE or FALSE
        
        try:
            float(str)
            return True
        except:
            return False
    
    def my_range(self, start, end, step):#To obtain range
        while start <= end:
            yield start#Kind of return : http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained 
            start += step
    
    def plot_values(self):#Final PLOTTING        
        
        
        x_axis = []
        Ec_axis = []
        Ei_axis = []
        Ev_axis = []
        Ed_axis = []
        Ef_axis = []
        Default_axis = []
        
        for i in self.my_range(1, 5, 0.05):
            
            x_axis.append((i))
            Ec_axis.append(1.12)
            Ev_axis.append(0.0)
            Ei_axis.append(0.5527)
            Default_axis.append(-.00001)
            
            if self.Type_SC != 1:
                Ef_axis.append(self.Fermi_Level)            
            if self.Type_SC == 2 :
                Ed_axis.append((1.12 - self.ntype_dopant_level[self.Dopant_index]))
            if self.Type_SC == 3 : 
                Ed_axis.append((self.ptype_dopant_level[self.Dopant_index]))
                
        if self.Type_SC == 1 :
            pylab.title('Energy Band Diagram - Intrinsic Material')
            print 'Plot is shown\
    \nEc       : Blue\
    \nEv       : Brown trianlgle\
    \nEi       : Majanta'
        else :
            pylab.title('Energy Band Diagram - Extrinsic Material')
            print 'Plot is shown\
    \nEc          : Blue\
    \nEv          : Brown trianlgle\
    \nEi          : Majanta\
    \nDonor level : yellow\
    \nFermilevel  : dots'
            
        pylab.plot(x_axis, Ec_axis, linewidth=1.0)
        pylab.plot(x_axis, Default_axis)
        pylab.plot(x_axis, Ev_axis , 'v')
        pylab.plot(x_axis, Ei_axis , 'm')
        
        if self.Type_SC != 1: 
            pylab.plot(x_axis, Ed_axis , 'y')
            pylab.plot(x_axis, Ef_axis , 'x')      
        
        pylab.show()
    
    def print_values(self):#Print final values
        
        self.textEdit.setVisible(True)#setting the result window
        self.plotBtn.setVisible(True)#Setting Plot Button
        
        if self.Type_SC != 1:#Calculating Electron and hole concentration
            if self.Con_Nd > self.Con_Na :
                Con_N = ((self.Con_Nd - self.Con_Na)/2.0) + pow((( (self.Con_Intr*self.Con_Intr) + pow(((self.Con_Nd - self.Con_Na)/2.0),2))),0.5)
                Con_P = (self.Con_Intr*self.Con_Intr)/Con_N
            if self.Con_Nd < self.Con_Na :
                Con_P = ((self.Con_Na - self.Con_Nd)/2.0) + pow((( (self.Con_Intr*self.Con_Intr) + pow(((self.Con_Na - self.Con_Nd)/2.0),2))),0.5)
                Con_N = (self.Con_Intr*self.Con_Intr)/Con_P
            # Under Equilibrium Condition
            #Finding the values for Fermi level
            self.Fermi_Level = self.Intr_Ei + 0.026 * ( math.log( Con_N / self.Con_Intr ))
            
        if self.Type_SC == 1:#Plotting for Intrinsic Material
            str1 =  """            
            \n
Type of material                   :   Intrinsic
Material                                  :   Silicon
Temperature                          :   300 K
Intrinsic concentration       :   10^10 /cm^3
The Band Gap                         :   1.12 eV\n
Ei - Intrinsic Level                :   0.5527 eV (0.0073eV below mid gap)
Ef - Fermi level                      :   0.5527 eV (Same as Ei)\n
\nDonor concentration            :   0
Acceptor concentration       :   0\n
\nConcentration of n                :   10^10 electrons (/cm^3)
Concentration of p                :   10^10 holes (/cm^3) """
            
        if self.Type_SC == 2:#Plotting for Extrinsic Material            
            str1 =  """            
            \n
Type of material                     :   Extrinsic - N-Type
Material                                    :   Silicon
Temperature                            :   300 K
Intrinsic concentration         :   10^10 /cm^3
The Band Gap                           :   1.12 eV
Ei - Intrinsic Level                  :   0.5527 eV (0.0073eV below mid gap)\n"""
            str1 += "\nDopant                                       :    " + self.ntype_dopant[self.Dopant_index]
            str1 += "\nDopant Level                            :    "+ str(self.ntype_dopant_level[self.Dopant_index]) + " eV below Ec"
            str1 +=  "\n\nEf -Fermi level                         :    " + str(round(self.Fermi_Level,3)) + "eV. (" + str(1.12 - round(self.Fermi_Level,3)) + " eV below Ec (CB))"
            str1 += "\n\nDonor Concentration              :    " + str(self.Con_Nd) + " /cm^3"
            str1 +=  "\nAcceptor Concentration         :    " + str(self.Con_Na) + "  /cm^3"
            str1 +=   "\n\nConcentration of n                  :    " + str(round(Con_N,3)) + " electrons /cm^3"
            str1 +=   "\nConcentration of p                  :    " + str(round(Con_P,3)) + " holes/cm^3"
        
        if self.Type_SC == 3:#Plotting for Extrinsic Material            
            str1 =  """            
            \n
Type of material                     :   Extrinsic - P-Type
Material                                    :   Silicon
Temperature                            :   300 K
Intrinsic concentration         :   10^10 /cm^3
The Band Gap                           :   1.12 eV
Ei - Intrinsic Level                  :   0.5527 eV (0.0073eV below mid gap)\n"""
            str1 += "\nDopant                                       :    " + self.ptype_dopant[self.Dopant_index]
            str1 += "\nDopant Level                            :    "+ str(self.ptype_dopant_level[self.Dopant_index]) + " eV above Ev"
            str1 +=  "\n\nEf -Fermi level                         :    " + str(round(self.Fermi_Level,3)) + "eV. (" + str(round(self.Fermi_Level,3)) + " eV above Ev (VB))"
            str1 += "\n\nDonor Concentration              :    " + str(self.Con_Nd) + " /cm^3"
            str1 +=  "\nAcceptor Concentration         :    " + str(self.Con_Na) + "  /cm^3"
            str1 +=   "\n\nConcentration of n                  :    " + str(round(Con_N,3)) + " electrons /cm^3"
            str1 +=   "\nConcentration of p                  :    " + str(round(Con_P,3)) + " holes/cm^3"

        self.textEdit.setText(str1)#Passing text to text edit to get the result
       
app = QtGui.QApplication(sys.argv)
Fermilevel = MainWindow()#To create a new class
Fermilevel.show()#To display the main window
app.exec_()#To execute the application - app