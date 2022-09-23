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

def split_c_instruction(command):
    dest_command = ''
    comp_command = ''
    comp_index = 0
    jump_command = ''
    jump_index = 0
    if command.find('=') != -1:
        index = command.find('=')
        dest_command = command[0:index]
        comp_index = index + 1
    
    if command.find(';') != -1:
        index = command.find(';')
        comp_command = command[comp_index:index]
        jump_index = index +  1
        jump_command = command[jump_index:]
    else:
        comp_command = command[comp_index:]

    return [dest_command, comp_command, jump_command]

def parse_c_instruction(command):
    instructions = split_c_instruction(command)
    parsed_instruction = f'111{parse_dest(instructions[0])}'
    return parsed_instruction

def parse_dest(dest):
    binary_dest = ''
    a_find = dest.find('A')
    d_find = dest.find('D')
    m_find = dest.find('M')

    if a_find != -1:
        binary_dest += '1'
    else:
        binary_dest += '0'

    if d_find != -1:
        binary_dest += '1'
    else:
        binary_dest += '0'

    if m_find != -1:
        binary_dest += '1'
    else: binary_dest += '0'

    return binary_dest

print(parse_dest(''))
    


