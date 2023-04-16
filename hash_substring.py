# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    modee = input()
    if "I" in modee:
        pattern = input().rstrip()
        text = input().rstrip()

    elif "F" in modee:
        num = "06"
        with open("./tests/"+ num, mode="r") as fails:
            txt = fails.read()
            x = txt.splitlines()
            pattern = x[0].rstrip()
            text = x[1].rstrip()      
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    return (pattern, text)

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    main_text_len = len(text)
    pattern_len = len(pattern)
    Q = 256
    B = 13
    h, p, t = 1, 0, 0
    output = ""
    
    for i in range (pattern_len -1):
        h = (h * Q) % B
        
    for i in range(pattern_len):
        p = (Q * p + ord(pattern[i])) % B
        t = (Q * t + ord(text[i])) % B
        
    for i in range(main_text_len - pattern_len + 1):
        if p == t:
            for j in range(pattern_len):
                if text[i+j] != pattern[j]:
                    break
            j += 1
            if j == pattern_len:
                output += str(i)
                output += " "
        
        if i < main_text_len - pattern_len:
            t = (Q * (t-ord(text[i]) * h) + ord(text[i+pattern_len])) % B   
             
            if t < 0:
                t = t + B      
    # and return an iterable variable
    
    return [output]

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

