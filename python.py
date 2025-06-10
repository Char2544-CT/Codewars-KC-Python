# 1. Check if a number is even or odd
def even_or_odd(number):
    
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
# 2. Convert number to string
def number_to_string(num):
    
    return str(num)

# 3. Remove string spaces
def no_space(x):
    
    return x.strip().replace(' ', '')

#4. Vowel count
def get_count(sentence):
    
    count = 0
    
    for v in sentence:
        if v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u':
            count += 1
            
    return count