import string

def data_valid(user_expression):
    user_expression=user_expression.lower()
    for letter in string.ascii_lowercase:
        if user_expression.count(letter):
            user_expression=data_valid(raw_input("Don`t use letter in math expression. Try once more: "))
            break
    for math_sign in ['+','-','*','/']:
        for math_sign2 in ['+','-','*','/']:
            if user_expression.count(math_sign+math_sign2):
                user_expression=data_valid(raw_input("Don`t use 2 or more math signs in a raw. Try once more: "))
    return user_expression


def lst_to_int_convert(user_expression):
    for cur_list_elem in xrange(0,len(user_expression),2):
        user_expression[cur_list_elem]=int(user_expression[cur_list_elem])
    return user_expression


def calculate_expression(valid_user_expression):
    cur_elem_of_expression=0
    while valid_user_expression[cur_elem_of_expression]!='endkey':
        flag=0
        if valid_user_expression[cur_elem_of_expression]=='*':
            valid_user_expression.insert(cur_elem_of_expression-1,
                                             valid_user_expression.pop(cur_elem_of_expression-1)*
                                             valid_user_expression.pop(cur_elem_of_expression))
            valid_user_expression.pop(cur_elem_of_expression)
            flag+=1

        if valid_user_expression[cur_elem_of_expression]=='/':
            valid_user_expression.insert(cur_elem_of_expression-1,
                                             valid_user_expression.pop(cur_elem_of_expression-1)/
                                             valid_user_expression.pop(cur_elem_of_expression))
            valid_user_expression.pop(cur_elem_of_expression)
            flag+=1

        if flag==0:
            cur_elem_of_expression+=1

    cur_elem_of_expression=0
    while valid_user_expression[cur_elem_of_expression]!='endkey':
        flag=0
        if valid_user_expression[cur_elem_of_expression]=='+':
            valid_user_expression.insert(cur_elem_of_expression-1,
                                             valid_user_expression.pop(cur_elem_of_expression-1)+
                                             valid_user_expression.pop(cur_elem_of_expression))
            valid_user_expression.pop(cur_elem_of_expression)
            flag+=1

        if valid_user_expression[cur_elem_of_expression]=='-':
            valid_user_expression.insert(cur_elem_of_expression-1,
                                             valid_user_expression.pop(cur_elem_of_expression-1)-
                                             valid_user_expression.pop(cur_elem_of_expression))
            valid_user_expression.pop(cur_elem_of_expression)
            flag+=1

        if flag==0:
            cur_elem_of_expression+=1


def splitting(string_user_expression, elem_oper, char='+', shift_in_gen_mas=0):
    simple_oper = elem_oper.split(char)
    for count_sign in xrange(len(simple_oper) - 1):
        string_user_expression.insert(len(string_user_expression) - shift_in_gen_mas, char)
        shift_in_gen_mas += 1
    for count_elem_oper in xrange(len(simple_oper)):
        operation_count = 4
        for char_2 in ('+', '-', '*', '/'):
            if simple_oper[count_elem_oper].count(char_2):
                # n-=1
                shift_in_gen_mas = splitting(string_user_expression, simple_oper[count_elem_oper], char_2, shift_in_gen_mas)
                break
            else:
                operation_count -= 1
                if operation_count == 0:
                    string_user_expression.insert(len(string_user_expression) - shift_in_gen_mas, simple_oper[count_elem_oper])
                    shift_in_gen_mas -= 1
    return shift_in_gen_mas


def main():
    user_expression = raw_input("Input some equation, use only math signs and numbers: ")
    user_expression=data_valid(user_expression)
    string_user_expression = []
    splitting(string_user_expression, user_expression)
    string_user_expression=lst_to_int_convert(string_user_expression)
    string_user_expression.append('endkey')
    calculate_expression(string_user_expression)
    print "Answer is ",string_user_expression[0]


if __name__ == '__main__':
    main()
