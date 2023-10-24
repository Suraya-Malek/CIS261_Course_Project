#SurayaMalek
#CIS261
#Course Project 1

def GetEmpName():
    empname = input("Enter employee name:")
    return empname

def GetHoursWorked():
    hours = float(input("Enter amount of hours worked:"))
    return hours

def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate:"))
    return hourlyrate

def GetTaxRate():
    taxrate = float(input("Enter tax rate:"))
    return taxrate
def CalcTaxAndNetpay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay):
    print(empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")
    
def printTotals(TotEmployees, TotHours, TotGrosspay, TotTax, TotNetpay):
    print()
    print(f"Total Number Of Employees:{TotEmployee}")
    print(f"Total Hours Worked:{TotHours:,.2f}")
    print(f"Total Grosspay:{TotGrosspay:,.2f}")
    print(f"Total Income Tax:{TotTax:,.2f}")
    print(f"Total Net Pay:{TotNetpay:,.2f}")
    
if __name__ == "__main__":
    TotEmployee = 0
    TotHours = 0
    TotGrosspay = 0.00
    TotTax = 0.00
    TotNetpay = 0.00
while True:
    empname = GetEmpName()
    if (empname.upper() == "END"):
        break
    hours = GetHoursWorked()
    hourlyrate = GetHourlyRate()
    taxrate = GetTaxRate()
    grosspay, incometax, netpay = CalcTaxAndNetpay(hours, hourlyrate, taxrate)
    printinfo(empname,hours,hourlyrate,grosspay,taxrate,incometax,netpay)
    TotEmployee +=1
    TotHours += hours
    TotGrosspay += grosspay
    TotTax += incometax
    TotNetpay += netpay
    
printTotals(TotEmployees, TotHours, TotGrosspay, TotTax, TotNetpay)
        
    
    
    
    