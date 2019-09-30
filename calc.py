from elements import masses

def calcMass(compound):
    elmLst = []
    coeffs = []
    currentElement = []
    currentPosition = 0
    isGroup = False
    parenCtr = 0
    currCoeff = []
    while currentPosition < len(compound):
        if compound[currentPosition].isnumeric(): #Add digit to currentCoeff
            currCoeff.append(compound[currentPosition])
        elif compound[currentPosition] == '(':
            if len(currentElement) != 0:
                if len(currCoeff) == 0: #If empty, default coefficient to 1
                    coeffs.append(1)
                else: #Join coeff list and turn into an int
                    coeffs.append(int(''.join(currCoeff)))
                    currCoeff = []
                elmLst.append(''.join(currentElement))
                currentElement = []
            parenCtr = 1
            while True: #Start recognition of sub group
                currentPosition += 1
                if compound[currentPosition] == '(':
                    parenCtr += 1
                elif compound[currentPosition] == ')':
                    parenCtr -= 1
                    if parenCtr == 0:
                        break
                currentElement.append(compound[currentPosition])
        elif compound[currentPosition].isalpha(): #Check if letter
            if compound[currentPosition].isupper(): #Notice that an element has been ended, so put in currentElement
                if len(currentElement) != 0:
                    if len(currCoeff) == 0: #If empty, default coefficient to 1
                        coeffs.append(1)
                    else: #Join coeff list and turn into an int
                        coeffs.append(int(''.join(currCoeff)))
                        currCoeff = []
                    elmLst.append(''.join(currentElement))
                    currentElement = []
            currentElement.append(compound[currentPosition])
        currentPosition += 1
    if len(currentElement) != 0: #Plop whatever is left in currentElement into elmLst
        if len(currCoeff) == 0: #If empty, default coefficient to 1
            coeffs.append(1)
        else: #Join coeff list and turn into an int
            coeffs.append(int(''.join(currCoeff)))
            currCoeff = []
        elmLst.append(''.join(currentElement))
        currentElement = []
    subTotal = 0
    # print(elmLst)
    # print(coeffs)
    for pos in range(len(elmLst)):
        if elmLst[pos] in masses: #Check if element
            subTotal += masses[elmLst[pos]] * coeffs[pos]
        else: #Otherwise calculate mass of sub compound
            subTotal += calcMass(elmLst[pos]) * coeffs[pos]
    return subTotal

print('To exit the program, type in quit')
while True:
    try:
        inputCompound = input('What compound do you want the molar mass of?\n')
        if inputCompound.lower() == 'quit':
            break
        outputMass = calcMass(inputCompound)c        print(f'The molar mass of {inputCompound} is {outputMass} atomic mass units.')
    except:
        print("Invalid input. Please try again.")