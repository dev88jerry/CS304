"""
Expression class
LinkStack is the underlying data structure
Postfix and Infix expression can only evaluate 1 digit
There are no checks to the validity of each character in the string

The converting method will automatically print the input string and the converted string
"""

from LinkedStack import LinkedStack


class Expression:

    def __init__(self, input, direction):
        self._stack = LinkedStack()
        self._input = input
        self._direction = direction
        self._infix = ""
        self._postfix = ""

    @staticmethod
    def _precedence(text):
        """
        Method to determine the order of operations
        :param text: char from expression
        :return: int for order
        """
        if text == '+' or text == '-':
            return 1
        elif text == '*' or text == '/':
            return 2
        elif text == '^':
            return 3

        return -1

    @staticmethod
    def _is_operator(text):
        """
        Method to determine if the character is an operator
        :param text: char from expression
        :return: bool value
        """
        if text == '+' or text == '-' or text == '*' or text == '/' or text == '^' or text == '%':
            return True

        return False

    @staticmethod
    def _is_operands(text):
        """
        Method to determine if character is 0-9 or a-z or A-Z
        :param text: char from expression
        :return: bool value
        """
        if ('0' <= text <= '9') or ('a' <= text <= 'z') or ('A' <= text <= 'Z'):
            return True

        return False

    def in_to_post(self):
        """
        Method to convert infix input to postfix notation
        """
        self._infix = self._input

        if not self._stack.is_empty():
            for i in range(len(self._stack)):
                self._stack.pop()

        result = ""
        size = len(self._input)
        i = 0
        while i < size:
            if self._is_operands(self._input[i]):
                #  When getting a operands
                result += str(self._input[i])
            else:
                if self._stack.is_empty() or self._input[i] == '(':
                    #  Base case or open parenthesis or stack is empty
                    self._stack.push(self._input[i])
                elif self._input[i] == ')':
                    #  Need to remove stack element until the close bracket
                    while not self._stack.is_empty() and self._stack.top() != '(':
                        #  Get top element
                        result += self._stack.pop()

                    if self._stack.top() == '(':
                        #  Remove stack element
                        self._stack.pop()
                else:
                    #  Remove stack element until precedence of
                    #  top is greater than current infix operator
                    while not self._stack.is_empty() and self._precedence(self._input[i]) <= self._precedence(
                            self._stack.top()):
                        #  Get top element
                        result += self._stack.pop()

                    #  Add new operator
                    self._stack.push(self._input[i])

            i += 1

        #  Add remaining elements
        while not self._stack.is_empty():
            result += self._stack.pop()

        self._postfix = result

        # Display result
        print("Infix    :", self._infix)
        print("Postfix  :", self._postfix)

    def post_to_in(self):
        """
        Method to convert postfix input to infix notation
        """
        self._postfix = self._input

        # Get the size of input
        size = len(self._input)

        # Variables to be used for the expression
        auxiliary = ""
        op1 = ""
        op2 = ""
        isValid = True
        i = 0

        while i < size and isValid:
            #  Check whether given postfix location
            #  at [i] is an operator or not
            if self._is_operator(self._input[i]):
                #  When operator exist
                #  Check that two operands exist or not
                if len(self._stack) > 1:
                    op1 = self._stack.pop()
                    op2 = self._stack.pop()
                    auxiliary = op2 + self._input[i] + op1
                    self._stack.push(auxiliary)
                else:
                    isValid = False

            elif self._is_operands(self._input[i]):
                #  When get valid operands
                auxiliary = self._input[i]
                self._stack.push(auxiliary)
            else:
                #  Invalid operands or operator
                isValid = False

            i += 1

        self._infix = self._stack.pop()

        print("Postfix :", self._postfix)
        print("Infix   :", self._infix)

    def evaluate(self):
        """
        Calculate the postfix expression
        :return: result of the expression
        """
        exp = self._postfix
        s = self._stack

        if '=' not in exp:
            for char in exp:
                # if char is digit push to stack
                if char.isdigit():
                    s.push(char)
                # else do the operation
                elif char in '*-/+':
                    operand1 = int(s.pop())
                    operand2 = int(s.pop())

                    if char == '+':
                        s.push(operand1 + operand2)
                    elif char == '-':
                        s.push(operand2 - operand1)
                    elif char == '*':
                        s.push(operand1 * operand2)
                    elif char == '/':
                        s.push(operand2 / operand1)

        # final result is element in stack
        ret = s.pop()

        return ret
