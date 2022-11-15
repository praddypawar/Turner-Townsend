'''
Write a python program which takes a series of roman numerals as input and which outputs their value as a number.
'''

def roman_numerals_to_number(s):
        roman_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number_val = 0
        for i in range(len(s)):
            if i > 0 and roman_val[s[i]] > roman_val[s[i - 1]]:
                number_val += roman_val[s[i]] - 2 * roman_val[s[i - 1]]
            else:
                number_val += roman_val[s[i]]
        return number_val
try:
    n = input("Enter roman numerals: ")
    print(f"Input: {n}")
    ans = roman_numerals_to_number(n)
    print(f"Outputs: {ans}")
except Exception as e:
    print(f"Error: {e}")
