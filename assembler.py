import sys

binary_program = []
# Accepts a line as input. if it is empty or the first non-whitespace char is '/', 
# the line is not a command and is skipped. Else the first word is assumed to be a valid
# hack assembly command. The command parser will print an error if it is fed an invalid command.
def is_command(line):
    stripped_line = line.strip()
    if line.isspace() == True:
        return False
    elif stripped_line[0] == '/':
        return False
    else:
        return True

# Controller function for parsing a command from assembly to machine    
def parse_to_hack(command):
    command = command.strip()
    if (command[0] == '@'):
        binary_program.append(f'{parse_a_instruction(command)}\n')
    else:
        binary_program.append(f'{parse_c_instruction(command)}\n')

# parse an a instruction from hack assembly to binary
def parse_a_instruction(command):
    address = int(command[1:])
    binary_address = bin(address)
    return f'{binary_address[2:].zfill(16)}'

# split a c instruction into comp, dest, and jump components
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

# controller function for parsing c instruction
def parse_c_instruction(command):
    instructions = split_c_instruction(command)
    parsed_instruction = f'111{parse_comp(instructions[1])}{parse_dest(instructions[0])}{parse_jump(instructions[2])}'
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

def parse_jump(jump):
    if jump == '':
        return '000'
    elif jump == 'JGT':
        return '001'
    elif jump == 'JEQ':
        return '010'
    elif jump == 'JGE':
        return '011'
    elif jump == 'JLT':
        return '100'
    elif jump == 'JNE':
        return '101'
    elif jump == 'JLE':
        return '110'
    elif jump == 'JMP':
        return '111'

def parse_comp(cmp):
    if cmp == '0':
        return '0101010'
    elif cmp == '1':
        return '0111111'
    elif cmp == '-1':
        return '0111010'
    elif cmp == 'D':
        return '0001100'
    elif cmp == 'A':
        return '0110000'
    elif cmp == '!D':
        return '0001101'
    elif cmp == '!A':
        return '0110001'
    elif cmp == '-D':
        return '0001111'
    elif cmp == '-A':
        return '0110011'
    elif cmp == 'D+1':
        return '0011111'
    elif cmp == 'A+1':
        return '0110111'
    elif cmp == 'D-1':
        return '0001110'
    elif cmp == 'A-1':
        return '0110010'
    elif cmp == 'D+A':
        return '0000010'
    elif cmp == 'D-A':
        return '0010011'
    elif cmp == 'A-D':
        return '0000111'
    elif cmp == 'D&A':
        return '0000000'
    elif cmp == 'D|!':
        return '0010101'
    elif cmp == 'M':
        return '1110000'
    elif cmp == '!M':
        return '1110001'
    elif cmp == '-M':
        return '1110011'
    elif cmp == 'M+1':
        return '1110111'
    elif cmp == 'M-1':
        return '1110010'
    elif cmp == 'D+M':
        return '1000010'
    elif cmp == 'D-M':
        return '1010011'
    elif cmp == 'M-D':
        return '1000111'
    elif cmp == 'D&M':
        return '1000000'
    elif cmp == 'D|M':
        return '1010101'

with open(sys.argv[1], 'r') as f:
    for line in f:
        if is_command(line) == True:
            parse_to_hack(line)
f.close

writeF = open(f'{sys.argv[1][:-4]}.hack', 'w', encoding='utf-8')

for command in binary_program:
    writeF.write(command)

writeF.close