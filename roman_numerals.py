import roman
class Solution(object):
    def fromRoman(self, roman_value):
        """
        :type s: str
        :rtype: int
        """
        try:
            roman_value = roman_value.upper()
        except ValueError as e:
            print(f"Error: {e}")
            return
        try: 
            integer_value = roman.fromRoman(roman_value)
            return integer_value
        except roman.InvalidRomanNumeralError as e:
            print(f"Error: {e}")
            return
solution = Solution()


roman_value = input("Please enter a Roman numeral to convert to integer: ")
integer_value = solution.fromRoman(roman_value)
if integer_value is not None:
    print(f"The integer value of Roman numeral {roman_value.upper()} is: {integer_value}")  
else:
    print("Conversion failed due to invalid input.")
