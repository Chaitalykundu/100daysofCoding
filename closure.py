######### FUNCTION RETURNING FUNCTION ########
######## CLOSURE PRACTICE ##########

def to_power(x):
    def cal_power(n):
        return n**x
    return cal_power

cube= to_power(3)
print(cube(2))  #o/p:8

sq= to_power(2)
print(sq(9))    #o/p:81
