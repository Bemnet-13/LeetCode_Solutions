class Solution:
    def interpret(self, command):
        interpreted_command = ""
        for i in range(len(command)):
            if command[i] == 'G':
                interpreted_command += 'G'
            elif command[i] == '(' and command[i+1] ==')':
                interpreted_command += 'o'
            elif command[i] == '(' and command[i+1] !=')':
                interpreted_command += "al"
        
        return interpreted_command
    
trial = Solution()
print(trial.interpret("(al)G(al)()()G"))
            