#!/usr/bin/env python3

from bits import VMCode


class testCode(VMCode):

    def writeArithmetic(self, command):
        commands = []
        if command == "delete":
            commands.append("leaw $SP, %A")         # %A = 0
            commands.append("movw (%A), %A")        # RAM[0] = 258
            commands.append("subw %A, $1, %D")      # %D = 257
            commands.append("leaw $SP, %A")         # %A = 0
            commands.append("movw %D, (%A)")        # RAM[0] = 257

        elif command == "add3":
            commands.append("leaw $SP, %A")         # %A = 0
            commands.append("movw (%A), %A")        # %A = RAM[0] = 259    
            commands.append("decw %A")              # %A = 258
            commands.append("movw (%A), %D")        # %D = RAM[258] = Z
            commands.append("decw %A")              # %A = 257
            commands.append("addw (%A), %D, %D")    # %D = RAM[258] + RAM[257] = Z + Y
            commands.append("decw %A")              # %A = 256
            commands.append("addw (%A), %D, %D")    # %D = RAM[258] + RAM[257] + RAM[256] = Z + Y + X    
            commands.append("movw %D, (%A)")        # %D = RAM[256] = Z + Y + X
            commands.append("addw %A, $1, %D")      # %D = 257
            commands.append("leaw $SP, %A")         # %A = 0
            commands.append("movw %D, (%A)")        # RAM[0] = 257

        elif command == "swap":
            commands.append("leaw $SP, %A")     # %A = 0
            commands.append("movw (%A), %A")    # RAM[0] = 258
            commands.append("subw %A, $1, %D")  # %D = 257
            commands.append("leaw $SP, %A")     
            commands.append("movw %D, (%A)")    # RAM[0] = 257
            commands.append("movw %D, %A")      # %A = 257

            commands.append("movw (%A), %D")    # %D = RAM[257]
            commands.append("leaw $5, %A")      # %A = 5
            commands.append("movw %D, (%A)")    # RAM[5] = RAM[257] = Y
            commands.append("leaw $SP, %A")     # %A = 257
            commands.append("movw (%A), %A")    # RAM[0] = 257
            commands.append("decw %A")          # %A = 256
            commands.append("movw (%A), %D")    # %D = RAM[256] = X
            commands.append("incw %A")          # %A = 257
            commands.append("movw %D, (%A)")    # X = RAM[257]

            commands.append("leaw $5, %A")      # %A = 5
            commands.append("movw (%A), %D")    # %D = RAM[5] = Y
            commands.append("leaw $SP, %A")     # %A = 257
            commands.append("movw (%A), %A")    # RAM[0] = 257
            commands.append("decw %A")          # %A = 256
            commands.append("movw %D, (%A)")    # RAM[256] = RAM[5] = Y
            commands.append("leaw $258, %A")    # %A = 258  
            commands.append("movw %A, %D")      # %D = 258
            commands.append("leaw $0, %A")      # %A = 0
            commands.append("movw %D, (%A)")    # RAM[0] = 258    
            
        # não mexer
        self.commandsToFile(commands)
