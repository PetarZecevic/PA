import sys

class vezba1:
    """Prva vezba"""

    def primer(self):
        print('primer unosenja i ispisa teksta\n')
        list_name = input("Ime liste: ");
        pairs = [(i,i+1) for i in range(1,10,2)]
        dict_pairs = {}
        dict_pairs[list_name] = pairs
        print(dict_pairs)
        print('\n\n')
        return

    def zad1(self, N, fast=False):
        print('zad1')
        sum = 0
        if fast:
            sum = N*(N+1)//2
        else:
            for i in range(N+1):
                sum += i
        print('Suma prvih ' + str(N) + ' brojeva: ' + str(sum) + '\n\n')
        return

    def zad2(self):
        print('zad2')
        sum = 0
        N = int(sys.argv[1])
        for i in range(N+1):
            sum += i**2
        print('Suma prvih ' + str(N) + ' kvadrata, preko terminala: ' + str(sum) + '\n\n')
        return

    def zad3(self, s1, s2):
        print('zad3')
        s = ""
        s = s1[0:3]*2 + s2[len(s2)-3:len(s2)]
        print(s + '\n\n')
        return

    def zad4(self):
        print('zad4')
        nums = [i for i in range(100)]
        nums.reverse()
        print(nums)
        print('\n\n')
        return

    def zad5(self):
        print('zad5')
        words_repeat = {}
        words_file = open('dict_test.txt', 'r')
        for line in words_file:
            words = line.split(' ')
            for word in words:
                word = word.lower()
                word = clear_interrpunction(word)
                if word in words_repeat.keys():
                    words_repeat[word] += 1
                else:
                    words_repeat[word] = 1
        words_file.close()
        print(words_repeat)
        print('\n\n')
        return

    def zad6(self):
        print('zad6')
        torks = [(1,1.0,'marko'), (2,2.0,'milan'), (3,3.0,'jovan'), (4,4.0,'marko')];
        print(torks)
    
        torks = torks[1:]
        print(torks)
        print('\n\n')
        return

    def zad7(self):
        print('zad7')
        torks = {(1,1.0,'marko'), (2,2.0,'milan'), (3,3.0,'jovan'), (4,4.0,'marko')};
        print(torks)
    
        torks.remove((1,1.0,'marko'))
        print(torks)
        print('\n\n')
        return

def clear_interrpunction(word):
    cleared_word = word
    while True:
        if cleared_word.endswith(".") or cleared_word.endswith(",") or cleared_word.endswith("!") or cleared_word.endswith("?"):
            cleared_word = cleared_word[:-1]
        elif cleared_word.endswith("\n"):
            cleared_word = cleared_word[:len(cleared_word)-1]
        else:
            break
    return cleared_word

if __name__ == "__main__":
    zadaci = vezba1()
    zadaci.zad1(100)
    zadaci.zad2()
    zadaci.zad3('beograd', 'krusevac')
    zadaci.zad4()
    zadaci.zad5()
    zadaci.zad6()
    zadaci.zad7()
    
