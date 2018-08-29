import random

def pad(literal):
    if not literal:
        return "  \n  "
    lines = ['', *literal.splitlines(), '']
    width = max(len(line) for line in lines)
    return '\n'.join(' ' + line.ljust(width) + ' ' for line in lines)

def get_random_pattern():
    pattern = ''
    for i in range(3):
        for j in range(10):
            pattern += get_random_string()
        pattern += '\n'
    return pattern

def get_random_string():
    a = random.random()
    if a < 0.5:
        return '#'
    else:
        return ' '


BLOCK = pad("""\
##
##
""")

BLINKER = pad("""\

###

""")

BLINKER3 = pad("""\
     #
###  # ###
     #
""")

PULSAR = pad("""\
  ###

#    #
#    #
#    #
  ###
""")

PENTADECATHLON = pad("""\
  #  #    # #
###  ###### ###
  #  #    # #
""")

PINWHEEL = pad("""\
 ####
#  # #
##   #
# #  #
#    #
 ####
""")

RANDOM = pad(get_random_pattern())

GLIDER = pad("""\
 #
  #
###
""")

DIEHARD = pad("""\
      #
##
 #   ###
""")

GLIDER_GUN = pad("""\
                        #
                      # #
            ##      ##            ##
           #   #    ##            ##
##        #     #   ##
##        #   # ##    # #
          #     #       #
           #   #
            ##
""")

PENTOMINO = pad("""\
 ##
##
 #
""")

BASELINE = pad("""\
######## #####   ###      ####### #####
""")

PATTERNS = [
    'BLOCK', 'BLINKER', 'BLINKER3', 'PULSAR', 'PENTADECATHLON', 'PINWHEEL', 'GLIDER', 'DIEHARD', 'GLIDER_GUN',
    'PENTOMINO', 'RANDOM', 
]

__all__ = PATTERNS[:]
