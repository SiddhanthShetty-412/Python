class conditionalStatements:
    def checkString (self, s : str) -> bool:
        c=0
        length=len(s)
        for i in range(0,length-1):
            if s[i]<= s[i+1]:
                c+=1
            
        if c==(len(s)-1):
            print("the string value is in right sequence")
        else:
            print("the string value is not in right sequence")
            
            
if __name__== '__main__':
    object= conditionalStatements()
    s='bbb'
    object.checkString(s)
    
        

                