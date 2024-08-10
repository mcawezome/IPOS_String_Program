class StringNumValue:
    """
    This class calculates the numeric value of any string. It can be
    initialised with a string. The string can be overriden using the {set}
    method or the user may append to it using the {append} method.

    This class returns the value of the string like this:
    a (or A) => 1
    b (or B) => 2
    ...
    z (or Z) => 26

    0 => 0
    1 => 1
    ...
    9 => 9

    In short, numeric characters retain their value and the letters of the
    alphabet are converted. Any other characters count as 0.

    If a string contains multiple characters, the value of the entire string
    is the sum of the values of each separate character. **This is not yet
    implemented and is part of the exercise!**
    """
    def __init__(self, s=''):
        self.s = s

    @property
    def value(self):
        """
        Calculate and return the value of the string based on the rules laid
        out in the docstring of the class.

        :return: The numeric value of the string
        """
        string_total = 0
        for i in range(len(self.s)):
            ord_value = ord(self.s[i])
            if ord('0') <= ord_value <= ord('9'):
                string_total += ord_value - ord('0')
            elif ord('A') <= ord_value <= ord('Z'):
                string_total += ord_value - ord('A') + 1
            elif ord('a') <= ord_value <= ord('z'):
                string_total += ord_value - ord('a') + 1
            else:
                # Do not add to the total
                pass
        return string_total

    def set(self, s):
        """
        Overwrite the value of the string.

        :param s: String to write
        """
        self.s = s

    def append(self, a):
        """
        Append a new string to the end of the existing string.

        :param a: String to append
        """
        self.s += a

    def __str__(self):
        """
        Outputs a string with the contents of the sting contained in the object and its value.
        :return: formatted string to print
        """
        return f"StringNumValue with string {self.s} and value of {self.value}"
