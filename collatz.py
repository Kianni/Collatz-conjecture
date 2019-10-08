
import matplotlib.pyplot as plt   
counter = 1
def collatz():
    try:
        number = int(input('Enter integer number: '))
        int(number)
        
        sequenceValue = []
        sequenceIndex = []
        global counter
        maximum = 0
        
        while number != 1:
            if number%2 == 0:
                number = number//2
            else:
                number = (3*number + 1)
            sequenceValue.append(number)
            
            if number > maximum:
                maximum = number
            sequenceIndex.append(sequenceValue.index(number))
            
            print('***',number,'***')
            counter += 1
            
        print('The sequence has reached the number 1 in %s steps' % counter)
        print('Maximum value in the sequence is %s' % maximum)
        

        def plot():
            '''I have invented .index -method "bike"!!!
            y = sequence
            x = []
            for i in range (len(sequence)):
                x.append(i)'''
            
            x = sequenceIndex
            y = sequenceValue

            plt.xlabel('%s - the amount of steps' % counter)
            plt.ylabel('Value, the maximum was %s' %maximum)
            plt.title('Collitz sequence for number %s' % number)
            plt.plot(x, y, color='orange')
            plt.show()
        plot()
    except ValueError:
        print('Only integers can being typed!')
        
collatz()
