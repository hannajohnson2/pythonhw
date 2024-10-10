def computePower(x, y):
    base = x
    for i in range(y - 1):
        x *= base
    return x


#2 

def temperatureRange(readings):
    return (min(readings), max(readings))


#3

def isWeekend(day):
    if day == 6 or day == 7:
        return True
    else:
        return False
    
#4

def fuel_efficiency(distance, fuel):
    return distance / fuel

#5   

def decodeNumbers(n):
    first = n//10 
    remainder = n%10 
    
    power = 0

    while n > 10:
        n = n / 10
        power += 1
    
    return first + (remainder * (10**power))

print(decodeNumbers(12345))

#6   

#6.1

def find_min_with_for_loop(nums):
    absolute = nums[0]
    current = nums[0]
    for num in nums:
        if num < current:
            current = num
        if current < absolute:
            absolute = num
    return absolute

def find_max_with_for_loop(nums):
    absolute = nums[0]
    current = nums[0]
    for num in nums:
        if num > current:
            current = num
        if current > absolute:
            absolute = num
    return absolute


#6.2

def find_max_with_while_loops(nums):
    absolute = nums[0]
    current = nums[0]
    i = 0
    while i < len(nums):
        if nums[i] > current:
            current = nums[i]
        if current > absolute:
            absolute = nums[i]
        i += 1
    return absolute

def find_min_with_while_loops(nums):
    absolute = nums[0]
    current = nums[0]
    i = 0
    while i < len(nums):
        if nums[i] <  current:
            current = nums[i]
        if current < absolute:
            absolute = nums[i]
        i += 1
    return absolute
        
#7

def vowel_and_consonant_count(text):
    lowercase = text.lower()
    vowel = 0
    consonants = 0
    for letter in lowercase:
        if letter.isAlpha():
            if letter == "a" or letter == "e" or letter == "i"  or letter == "o" or letter == "u":
                vowel += 1
            else:
                consonants += 1
    return(vowel, consonants)

#8

def digital_root(num):
    add = 0
    for i in str(num):
        add += int(i)
    return add