# Most frequent letter

rand_words =  ["hotel", "travel", "python", "analysis", "booking",
         "client", "database", "excel", "automation", "script",
         "import", "export", "rate", "server", "network"]

def freq_letter(words):
    # Count letter in each word
    print('-'*50)
    print(f'Checking word: {word}')
    
    dict_count = {}

    for letter in words.lower():
        if letter not in dict_count:
            count = word.count(letter)
            dict_count[letter] = count


    for letter, count in dict_count.items():
        print(f'{letter} used {count} times.')

    # Find the max frequency letter

    max_count = max(dict_count.values())
    max_letters = []
    for k,v in dict_count.items():
        if v == max_count:
            max_letters.append(k)

    print(f'The Most Frequesnt Letter {max_letters}')

# Overall letter count and the maximum number 1 letter occured across all words

big_dict = {}

for word in rand_words:
    most_freq = freq_letter(word)
    for letter in word:
        overall_count = word.count(letter)
        if letter not in big_dict:
            big_dict[letter] = overall_count
        else:
            big_dict[letter] += overall_count
max_letter = max(big_dict, key=big_dict.get) 
max_value = big_dict[max_letter]   
print(f'Overall Letter Frequency: {max_letter}  {max_value} many times.')
print(big_dict)