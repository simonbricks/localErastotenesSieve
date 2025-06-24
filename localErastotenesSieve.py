def findNumsToAdd(currentMaxInFile, upperBoundToAdd):
    numbersToAdd = []

    if currentMaxInFile < 2:
        numbersToAdd.append(2)
    
    if (currentMaxInFile + 1) % 2 == 0: 
        smallestOddNum = currentMaxInFile + 2
    else:
        smallestOddNum = currentMaxInFile + 1

    for oddNumInBound in range(smallestOddNum, upperBoundToAdd + 1, 2):
        shouldAdd = checkDivisorsInFile(oddNumInBound)
        
        for addedPrime in numbersToAdd: 
            if addedPrime * addedPrime > oddNumInBound:
                break

            if oddNumInBound % addedPrime == 0:
                shouldAdd = False
                break
        
        if (shouldAdd == True):
            numbersToAdd.append(oddNumInBound)
    return numbersToAdd


def checkDivisorsInFile(number):
    shouldAdd = True
    
    # a file has to be opened deep inside this function to refresh its contents every time the function is called
    with open("sieve.txt", "r") as erastotenesSieve: 
        for line in erastotenesSieve:
            line.replace("\n", "")
            somePrime = int(line)

            if number % somePrime == 0: 
                shouldAdd = False
                break
    return shouldAdd


def addToSieve(arrayOfPrimes, file):
    for element in arrayOfPrimes:
        file.write(str(element) + "\n")


def factorizeNumber(number, file):
    outputFactors = ""

    for line in file:
        line.replace("\n", "") 
        maybeAFactor = int(line)

        while number % maybeAFactor == 0: # is a factor
            number //= maybeAFactor        
            outputFactors += f'{maybeAFactor}'

            if number != 1: # so that there wouldn't be a '*' at the end of the string
                outputFactors += " * "
    
    if number > 1:
        outputFactors += f'{number}'
    print(outputFactors)


# if the file with the Erastotenes' sieve doesn't exist, a blank one is created
erastotenesSieve = open("sieve.txt", "a") 

# first, we find the biggest prime number written in the file
with open("sieve.txt", "r") as erastotenesSieve:
    biggestPrimeInFile = 1

    for line in erastotenesSieve:
        newLine = line.replace("\n", "") 
        biggestPrimeInFile = int(newLine)

factorizedNum = int(input("Type in the number you want to factorize: "))

# then, if the factorized number is bigger than the root of the biggest prime we have in the file, 
# we check whether we need to add some primes to the file
if (factorizedNum > biggestPrimeInFile * biggestPrimeInFile):
    rootOfPrime = 1 # variable stores floor of the root of biggestPrimeInFile

    while rootOfPrime * rootOfPrime <= factorizedNum:
        rootOfPrime += 1
    
    numsToAddToSieve = findNumsToAdd(biggestPrimeInFile, rootOfPrime)

    with open("sieve.txt", "a") as erastotenesSieve:
        addToSieve(numsToAddToSieve, erastotenesSieve)

# lastly, we finally factorize the number, based on our local Erastotenes' sieve
with open("sieve.txt", "r") as erastotenesSieve:
    factorizeNumber(factorizedNum, erastotenesSieve)