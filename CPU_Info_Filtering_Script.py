#script with different functions to filter output of cpu monitoring in text file

import string

#first argument array of lines of txt file
#second argument is the number of top CPU usage processes you would like to see
def certainNumberTopProcesses(lines, num):

    processCounter = 0
    outputProcesses = False

    stringOutput = ''

    #look through file until we get to CPU process list
    for line in lines:
        arrayLineItems = line.split()
        if len(arrayLineItems) > 0 and arrayLineItems[0] == 'PID':
            outputProcesses = True
        if outputProcesses and processCounter <= num:
            stringOutput += line
            if processCounter == num:
                stringOutput += '\n'
            processCounter += 1
        else:
            processCounter = 0
            outputProcesses = False

    #output stringOutput to text file
    with open('cpu_info_refined.txt', 'w') as f:
        f.write(stringOutput)

def main():
    
    with open('cpu_info.txt') as f:
        lines = f.readlines()
    certainNumberTopProcesses(lines, 10)

if __name__ == "__main__":
    main()


