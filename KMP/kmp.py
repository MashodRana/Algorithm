def create_pie_table(pattern, length):
    table = [0 for i in range(length)]
    # print('IN the def')
    i=1
    j=0

    while i < length:
        if pattern[i]==pattern[j]:
            j+=1
            table[i]=j
            i+=1
        elif pattern[i]!=pattern[j] and j!=0:
            j=table[j-1]
        else:
            table[i]=0
            i+=1
    # print(table)
    return table


def find_string( string, pattern):
    len_string = len(string)
    len_pattern = len(pattern)
    
    table = create_pie_table( pattern, len_pattern )
    
    i=0
    j=0
    
    while i < len_string:
        if string[i]==pattern[j]:
            i+=1
            j+=1
        else:
            if j==0:
                i+=1
            else:
                j=table[j-1]
        if j==len_pattern:
            return 'Found the pattern into the string'
    
    return 'Pattern is not found into the string'

pattern = input()
string = input()

print( find_string( string, pattern ) )
