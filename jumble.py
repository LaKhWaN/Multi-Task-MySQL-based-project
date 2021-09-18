import random

#Main Loop
def start():
    file = open("Jumble Words\words.txt",'r')
    words = file.read()
    word_list = words.split()
    ans = 'y'
    word = random.choice(word_list)
    wordlist = list(word)
    length = len(wordlist)
    jumbledword = []
    for i in range(length):
        rndmnum = random.randrange(length)
        jumbledword.append(wordlist.pop(rndmnum))
        length-=1
    print('The jumbled word is: ',end = '')
    for letter in jumbledword:
        print(letter,end='')
    print('')
    for i in range(2,-1,-1):
        ask = input('Enter the correct answer here: ')
        if ask==word:
            print('Correct!')
            start()
        else:
            print('Incorrect!')
            print('You have {} tries left!'.format(i))
    print('The correct answer is: {}'.format(word))

    ans = input('Would you like to play again?(y/n): ')
    if ans == 'y':
        start()

if __name__ == "__main__":
    start()