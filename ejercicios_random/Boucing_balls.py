#Given an array (arr) as an argument complete the 
# function countSmileys that should return the total number 
# of smiling faces.
#Rules for a smiling face:
#Each smiley face must contain a valid pair of eyes. 
# Eyes can be marked as : or ;
#A smiley face can have a nose but it does not have to. 
# Valid characters for a nose are - or ~
#Every smiling face must have a smiling mouth that should 
# be marked with either ) or D
#No additional characters are allowed except for those mentioned.

#Valid smiley face examples: :) :D ;-D :~)
#Invalid smiley faces: ;( :> :} :]

def count_smileys(arr):
    ojos = [":",";"]
    nariz = ["-","~"]
    boca = [")","D"]
    cont_caritas_felices = 0
    
    for simbolos in arr:
        if len(simbolos) == 2:
            if simbolos[0] in ojos and simbolos[1] in boca:
                cont_caritas_felices += 1
        elif len(simbolos) ==3:
            if simbolos[0] in ojos and simbolos[-1] in boca and simbolos[1] in nariz:
                cont_caritas_felices += 1
    return cont_caritas_felices
print (count_smileys([':D', ':(', ':o(', ':D', ':oD', ';o(', ';-(', ';D', ':(']))