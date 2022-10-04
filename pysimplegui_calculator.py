import PySimpleGUI as g


def digit_input(button_key, keys_displayed):
    global percent
    global hold_operand

    if percent:
        keys_displayed = ''
        values['input'] = ''
        percent = False
        hold_operand = False
    if button_key == '.':
        if button_key in keys_displayed:
            pass
        elif keys_displayed == '':
            keys_displayed = '0.'
        else:
            keys_displayed = keys_displayed + '.'
    elif keys_displayed == '0' and button_key != '0':
        keys_displayed = button_key
    elif keys_displayed == '0' and button_key == '0':
        pass
    else:
        keys_displayed += button_key
    return keys_displayed


def calc(op, operand_1, operand_2):  # function which performs the given operation (op) on two given operands.

    global hold_operand

    if op == '/':
        try:
            result = str(float(operand_1) / float(operand_2))
        except (ZeroDivisionError, ValueError):
            result = 'Error'
    elif op == 'x':
        try:
            result = str(float(operand_1) * float(operand_2))
        except ValueError:
            result = 'Error'
    elif op == '-':
        try:
            result = str(float(operand_1) - float(operand_2))
        except ValueError:
            result = 'Error'
    elif op == '+':
        try:
            result = str(float(operand_1) + float(operand_2))
        except ValueError:
            result = 'Error'
    return result


def sign_display(sign, keys_displayed):  # function which handles the +/- sign display of any current operand.

    if sign:
        key_list = list(keys_displayed)
        del key_list[0]
        sign = False
        return ''.join(key_list)
    else:
        sign = True
        return '-' + values['input']


in_elem = g.Input(size=(30, 1), do_not_clear=True, key='input')
# setup for calculator GUI layout.
layout = [
    [in_elem],
    [g.ReadFormButton('AC'), g.ReadFormButton('+/-'), g.ReadFormButton('%'), g.ReadFormButton('/')],
    [g.ReadFormButton('1'), g.ReadFormButton('2'), g.ReadFormButton('3'), g.ReadFormButton('x')],
    [g.ReadFormButton('4'), g.ReadFormButton('5'), g.ReadFormButton('6'), g.ReadFormButton('-')],
    [g.ReadFormButton('7'), g.ReadFormButton('8'), g.ReadFormButton('9'), g.ReadFormButton('+')],
    [g.ReadFormButton('.'), g.ReadFormButton('0'), g.ReadFormButton(''), g.ReadFormButton('=')],
]

form = g.FlexForm('Keypad', default_element_size=(5, 2), auto_size_buttons=False)
form.Layout(layout)

keys_entered = '0'
keys_entered_1 = ''
operator = ''
hold_operand = False
negative = False
percent = False
calculate = False

in_elem.Update(keys_entered)
while True:
    button, values = form.Read()
    if button is None:  # if the X button clicked, just exit.
        break
    if button is 'AC':  # clear all entries and flags if 'AC' is pressed.
        keys_entered = '0'
        keys_entered_1 = ''
        negative = False
        operator = ''
        hold_operand = False
        percent = False
    elif button in '1234567890.':
        if calculate:  # calculate flag is set to True immediately after = has been pressed, so new key_entered
            keys_entered = ''  # is began with appropriate flags reset.
            keys_entered_1 = ''
            operator = ''
            calculate = False
        if operator != '':  # If operator has been entered, store the 2nd operand in keys_entered_1 and flag
            hold_operand = True  # with hold_operand.
            keys_entered_1 = digit_input(button, keys_entered_1)
        else:  # If operator has not be entered, store digits in 1st operand.
            keys_entered = digit_input(button, keys_entered)
    elif button is '%':  # % is special because operand (either 1st or 2nd) must be divided by 100.
        percent = True  # % flag is set to allow detection of new operand input if a digit is entered after %.
        if hold_operand:
            keys_entered_1 = str(float(keys_entered_1) / 100)
        else:
            keys_entered = str(float(keys_entered) / 100)
    elif button in '/x-+':
        if hold_operand:
            hold_operand = False
            keys_entered = calc(operator, keys_entered, keys_entered_1)
        operator = button
        keys_entered_1 = ''
        calculate = False
        percent = False
    elif button is '+/-':
        if hold_operand:
            keys_entered_1 = sign_display(negative, keys_entered_1)
        else:
            keys_entered = sign_display(negative, keys_entered)
    elif button is '=':
        if keys_entered_1 != '':
            keys_entered = calc(operator, keys_entered, keys_entered_1)
            hold_operand = False
            calculate = True
        else:
            keys_entered = values['input']
            in_elem.Update(keys_entered)

    if hold_operand and keys_entered_1 != '':
        in_elem.Update(keys_entered_1)
    else:
        in_elem.Update(keys_entered)