class Solution:
    def romanToInt(self, s: str) -> int:
        current_index = 0
        total = 0

        while current_index < len(s) and s[current_index] == "M":
            current_index += 1
            total += 1000

        if current_index < len(s) and s[current_index:current_index+2] == "CM":
            current_index += 2
            total += 900

        while current_index < len(s) and s[current_index] == "D":
            current_index += 1
            total += 500

        if current_index < len(s) and s[current_index:current_index+2] == "CD":
            current_index += 2
            total += 400

        while current_index < len(s) and s[current_index] == "C":
            current_index += 1
            total += 100

        if current_index < len(s) and s[current_index:current_index+2] == "XC":
            current_index += 2
            total += 90

        while current_index < len(s) and s[current_index] == "L":
            current_index += 1
            total += 50

        if current_index < len(s) and s[current_index:current_index+2] == "XL":
            current_index += 2
            total += 40

        while current_index < len(s) and s[current_index] == "X":
            current_index += 1
            total += 10

        if current_index < len(s) and s[current_index:current_index+2] == "IX":
            current_index += 2
            total += 9

        while current_index < len(s) and s[current_index] == "V":
            current_index += 1
            total += 5

        if current_index < len(s) and s[current_index:current_index+2] == "IV":
            current_index += 2
            total += 4

        while current_index < len(s) and s[current_index] == "I":
            current_index += 1
            total += 1

        return total
