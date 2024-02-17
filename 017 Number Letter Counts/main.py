
WORDS = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred", "thousand"]

def len_of_words(number) -> int:
    if number > 999:
        return len(WORDS[1]) + len(WORDS[-1])
    elif number < 21:
        return len(WORDS[number])
    elif number < 100:
        return len(WORDS[(number // 10) + 18]) + len(WORDS[number % 10])
    else:
        if number % 100 == 0:
            return len(WORDS[number // 100]) + len(WORDS[-2])
        else:
            return len(WORDS[number // 100]) + len(WORDS[-2]) + len("and") + len_of_words(number % 100)




def main():
    res = 0
    for num in range(1, 1001):
        res += len_of_words(num)
    print(res)

main()
