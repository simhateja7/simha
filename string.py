def most_frequent(string):
    count_letters = {}
    for letter in set(string):
        count_letters[letter] = string.count(letter)

    sorted_keys = sorted(count_letters,key=count_letters.get,reverse = True)
    print(sorted_keys)
    for i in sorted_keys:
        print(i,'=',count_letters[i])
        

            
        
            

string= input("please enter a string:")

most_frequent(string)
    
