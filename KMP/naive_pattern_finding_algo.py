def naive_algorithm( string, pattern ):
    len_string = len(string)
    len_pattern = len(pattern)
    
    i=0
    
    while i < len_string:
        j=0
        k=i
        while k<len_string and j<len_pattern and pattern[j]==string[k]:
            print(string[k])
            j+=1
            k+=1
            
        
        if j==len_pattern:
            print('found the pattern into the string')
            return
        else:
            i+=1
        
    print("Pattern is not in the string")
    return

pattern = input()
string = input()

naive_algorithm( string, pattern )
