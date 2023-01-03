def generateOrderedNumbers(maxValue):

    decimalPlaces = int(np.log10(maxValue))
    stopTest = 0
    numberList = ["0"*(decimalPlaces+1)]
    
    for dP in range(decimalPlaces+1):
        
        for numeral in range(10**(dP+1)-10**dP):
            
            number = (decimalPlaces-dP)*"0"+str(numeral+10**dP)
            numberList.append(number)
            
            if number == str(maxValue-1):
                stopTest = 1
                break
            
        if stopTest == 1:
            break
        
    return numberList
