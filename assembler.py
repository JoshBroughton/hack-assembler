import sys

with open(sys.argv[1], 'r') as f:
    program = f.read()

# Accepts a line as input. if it is empty or the first non-whitespace char is '/', 
# the line is not a command and is skipped. Else the first word is assumed to be a valid
# hack assembly command. The command parser will print an error if it is fed an invalid command.
def is_command(line):
    stripped_line = line.strip()
    if line.isspace() == True:
        return False
    elif stripped_line[0] == '/':
        return False
    
def parse_to_hack(command):
    command = command.strip()
    if (command[0] == '@'):
        parse_a_instruction(command)
    else:
        parse_c_instruction(command)

def parse_a_instruction(command):
    address = int(command[1:])
    binary_address = bin(address)
    return f'{binary_address[2:].zfill(16)}'

def parse_c_instruction(command):
    dest_command = ''
    comp_command = ''
    comp_index = 0
    jump_command = ''
    jump_index = 0
    try:
        index = command.index('=')
        dest_command = command[0:index]
        comp_index = index + 1
    except:
        pass

    try:
        index = command.index(';')
        comp_command = command[comp_index:index]
        jump_index = index +  1


    


