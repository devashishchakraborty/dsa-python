from stack import Stack

def convert_int_to_bin(stack, dec_num):
    binary = ""
    while dec_num >= 0:
        if dec_num == 0:
            remainder = dec_num % 2
            stack.push(remainder)
            break

        else:
            remainder = dec_num % 2
            dec_num = dec_num // 2
            stack.push(remainder)
    
    while not stack.is_empty():
        binary += str(stack.pop())
    
    return int(binary)
    

stack = Stack()
integer = 12
print(convert_int_to_bin(stack, integer))
