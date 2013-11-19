from PyQt4 import QtGui
from PyQt4.QtGui import QStandardItemModel
from PyQt4.QtGui import QStandardItem
from PyQt4 import QtCore
import sys
from data_collector import Ui_MainWindow
import pylab
import math

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.a.setVisible(False)
        self.b.setVisible(False)
        self.lbl.setVisible(False)
        self.err_lbl.setVisible(False)
        self.textEdit.setVisible(False)
        self.plotBtn.setVisible(False)
        self.Con_Intr = pow(10, 10)
        self.Intr_Ei = 0.5527 
        self.Fermi_Level = 0
        
        self.semi_conductor = ["Intrinsic", "N-Type", "P-Type"]
        self.ntype_dopant = ["Antimony", "Phosphorus", "Arsenic"]
        self.ntype_dopant_level = [0.039, 0.045, 0.054]
        self.ptype_dopant = ["Boron", "Aluminium", "Gallium", "Indium"]
        self.ptype_dopant_level = [0.045, 0.067, 0.072, 0.16]
        
        self.flag = False
        self.Con_Nd = 0
        self.Con_Na = 0
        self.Type_SC = 0
        self.Dopant_index = 0
         
        self.populate_list(self.semi_conductor, "select semi-conductor type")
        self.qlist.doubleClicked.connect(self.someMethod)
    
    @QtCore.pyqtSignature("")    
    def on_plotBtn_clicked(self):
        
        self.plot_values()
            
    def check_le(self):
        
        val1 = str(self.a.text())
        val2 = str(self.b.text())
        if val1 == "":
            self.a.setFocus()
        elif val2 == "":
            self.b.setFocus()
        elif not self.is_float(val1):
            self.a.setText("")
            self.a.setFocus()
        elif not self.is_float(val2):
            self.b.setText("")
            self.b.setFocus()            
        else:
            if self.Type_SC == 2:
                
                if self.flag == False:
                    Con_Nd_Limit = 1.6*(pow(10,18))                
                    self.Con_Nd = float(val1) * ( pow(10,float(val2)))
                    if self.Con_Nd > Con_Nd_Limit:
                        
                        self.err_lbl.setVisible(True)                        
                        t = """ The material is heavily doped and is exceeding the degeneracy limit.
                                Please Enter a value below 1.6*10^18 """                        
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
                        msg = "Is the material containing accepter impurities"
                        self.ask_extra_impurity(msg)
                        
                else:                  
                    self.Con_Na = float(val1) * ( pow(10,float(val2)))
                    Con_Na_Limit = 9.1*(pow(10,17))
                    
                    if self.Con_Na > Con_Na_Limit :
                        
                        self.err_lbl.setVisible(True)
                        t = """ The material is heavily doped and is exceeding the degeneracy limit.
                                Please Enter a value below 9.1*10^17 """
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
                        t = """ The material is heavily doped and is exceeding the degeneracy limit.
                                Please Enter a value below 9.1*10^17 """
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
                        msg = "Is the material containing donor impurities"
                        self.ask_extra_impurity(msg)
                        
                else:
                       
                    Con_Nd_Limit = 1.6*(pow(10,18))                
                    self.Con_Nd = float(val1) * ( pow(10,float(val2)))
                    if self.Con_Nd > Con_Nd_Limit:
                        
                        self.err_lbl.setVisible(True)                        
                        t = """ The material is heavily doped and is exceeding the degeneracy limit.
                                Please Enter a value below 1.6*10^18 """                        
                        palette = QtGui.QPalette()
                        palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
                        self.err_lbl.setPalette(palette)            
                        self.err_lbl.setText(t)
                        
                        self.a.setText("")
                        self.b.setText("")
                        self.a.setFocus()                                           
                    else:
                        self.print_all_values()
                        
    def print_all_values(self):
        
        self.a.setVisible(False)
        self.b.setVisible(False)
        self.err_lbl.setVisible(False)
        self.label.setVisible(False)
        
        print self.semi_conductor[self.Type_SC-1]
        if self.Type_SC == 2:
            print self.ntype_dopant[self.Dopant_index]
            print self.ntype_dopant_level[self.Dopant_index]
        else:
            print self.ptype_dopant[self.Dopant_index]
            print self.ptype_dopant_level[self.Dopant_index]
        print self.Con_Na, self.Con_Nd
        
        self.print_values()
        
    def ask_extra_impurity(self, msg):
        
        self.flag = True
        self.err_lbl.setVisible(False)
        self.a.setText("")
        self.b.setText("")
        self.a.setFocus()
        
        reply = QtGui.QMessageBox.question(self, 'Ask',
            msg, QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)        
        if reply == QtGui.QMessageBox.Yes:
            self.label.setText("Enter the concentration (in the form of A*10^B)")
        else:
            self.label.setVisible(False)
            self.a.setVisible(False)
            self.b.setVisible(False)
            self.lbl.setVisible(False)
            self.print_all_values()
        
    def on_a_returnPressed(self):
        self.check_le()
    
    def on_b_returnPressed(self):        
        self.check_le()        
            
    def is_float(self, str):
        
        try:
            float(str)
            return True
        except:
            return False
    
    def someMethod(self, item):
        
        data = item.data().toString()
        
        if self.Type_SC == 0:
            self.Type_SC = self.semi_conductor.index(data) + 1
            if self.Type_SC == 1:
                
                self.print_values()
                self.qlist.hide()
                
            elif self.Type_SC == 2:
                self.populate_list(self.ntype_dopant, "select dopant for N-type SC")
            elif self.Type_SC == 3:
                self.populate_list(self.ptype_dopant, "select dopant for P-type SC")
                
        elif self.Type_SC == 2:
            self.Dopant_index = self.ntype_dopant.index(data)
            self.qlist.hide() 
            self.label.setText("Enter the concentration of "+self.ntype_dopant[self.Dopant_index]+" \n(in the form of A*10^B)")
            self.a.setVisible(True)
            self.b.setVisible(True)
            self.lbl.setVisible(True)
            
        elif self.Type_SC == 3:
            self.Dopant_index = self.ptype_dopant.index(data)
            self.qlist.hide()  
            self.label.setText("Enter the concentration of "+self.ptype_dopant[self.Dopant_index]+" \n (in the form of A*10^B)")           
            self.a.setVisible(True)
            self.b.setVisible(True)
            self.lbl.setVisible(True)
        
        
    def populate_list(self, data, question):
        
        self.label.setText(question)
        model = QStandardItemModel(self.qlist)
        for val in data:
            item = QStandardItem(val)
            model.appendRow(item)
        self.qlist.setModel(model)

    
    def my_range(self, start, end, step):
        while start <= end:
            yield start
            start += step
        
    def plot_values(self):        
        
        
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
            pylab.title('Intrinsic Material')
            print 'Plot is shown\
    \nEc       : Blue\
    \nEv       : Brown trianlgle\
    \nEi       : Majanta'
        else :
            pylab.title('Extrinsic Material')
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
        
    def print_values(self):
        
        self.textEdit.setVisible(True)
        self.plotBtn.setVisible(True)
        
        if self.Type_SC != 1:
            if self.Con_Nd > self.Con_Na :
                Con_N = ((self.Con_Nd - self.Con_Na)/2.0) + pow((( (self.Con_Intr*self.Con_Intr) + pow(((self.Con_Nd - self.Con_Na)/2.0),2))),0.5)
                Con_P = (self.Con_Intr*self.Con_Intr)/Con_N
            if self.Con_Nd < self.Con_Na :
                Con_P = ((self.Con_Na - self.Con_Nd)/2.0) + pow((( (self.Con_Intr*self.Con_Intr) + pow(((self.Con_Na - self.Con_Nd)/2.0),2))),0.5)
                Con_N = (self.Con_Intr*self.Con_Intr)/Con_P
            # Under Equilibrium Condition
            self.Fermi_Level = self.Intr_Ei + 0.026 * ( math.log( Con_N / self.Con_Intr ))
            
        if self.Type_SC == 1:
            str1 =  """            
            Type of material                :   Intrinsic
            Material                        :   Silicon
            Temperature                     :   300 K
            Intrinsic concentration         :   10^10 /cm^3
            The Band Gap                    :   1.12 eV
            Ei - Intrinsic Level            :   0.5527 eV (0.0073eV below mid gap)
            Ef - Fermi level                :   0.5527 eV (Same as Ei)
            Donor concentration             :   0
            Acceptor concentration          :   0
            Concentration of electrons (n)  :   10^10 /cm^3
            Concentration of holes (p)      :   10^10 /cm^3 """
            
        if self.Type_SC == 2:            
            str1 =  """            
            Type of material                :   Extrinsic
            Material                        :   Silicon
            Temperature                     :   300 K
            Intrinsic concentration         :   10^10 /cm^3
            The Band Gap                    :   1.12 eV
            Ei - Intrinsic Level            :   0.5527 eV (0.0073eV below mid gap) """
            str1 += "\n    Dopant                          :  " + self.ntype_dopant[self.Dopant_index]
            str1 += "\n    Dopant Level                    :  "+ str(self.ntype_dopant_level[self.Dopant_index]) + " eV below Ec"
            str1 +=  "\nEf -Fermi level                 :  " + str(round(self.Fermi_Level,3)) + "eV. ('" + str(1.12 - round(self.Fermi_Level,3)) + " eV below CB)"
            str1 += " \nDonor Concentration             :  " + str(self.Con_Nd) + " /cm^3"
            str1 +=  "\nAcceptor Concentration          :  " + str(self.Con_Na) + "  /cm^3"
            str1 +=   "\nConcentration of electrons (n)  :  " + str(round(Con_N,3)) + "  /cm^3"
            str1 +=   "\nConcentration of holes (p)      :  " + str(round(Con_P,3)) + " /cm^3"
        
        if self.Type_SC == 3:            
            str1 =  """            
            Type of material                :   Extrinsic
            Material                        :   Silicon
            Temperature                     :   300 K
            Intrinsic concentration         :   10^10 /cm^3
            The Band Gap                    :   1.12 eV
            Ei - Intrinsic Level            :   0.5527 eV (0.0073eV below mid gap) """
            str1 += "\n    Dopant                          :  " + self.ptype_dopant[self.Dopant_index]
            str1 += "\n    Dopant Level                    :  "+ str(self.ptype_dopant_level[self.Dopant_index]) + " eV above Ev"
            str1 +=  "\nEf -Fermi level                 :  " + str(round(self.Fermi_Level,3)) + "eV. ('" + str(round(self.Fermi_Level,3)) + " eV below CB)"
            str1 += " \nDonor Concentration             :  " + str(self.Con_Nd) + " /cm^3"
            str1 +=  "\nAcceptor Concentration          :  " + str(self.Con_Na) + "  /cm^3"
            str1 +=   "\nConcentration of electrons (n)  :  " + str(round(Con_N,3)) + "  /cm^3"
            str1 +=   "\nConcentration of holes (p)      :  " + str(round(Con_P,3)) + " /cm^3"

        self.textEdit.setText(str1)

        
app = QtGui.QApplication(sys.argv)
xScribble = MainWindow()
xScribble.show()
app.exec_()
