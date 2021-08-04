def solution(s):
    # Your code here
    
    if len(s) < 200:
        
        for x in range(1, len(s)):
            substring = s[:x]

            if substring * (len(s)//len(substring))+(substring[:len(s)%len(substring)]) == s:
                #print(substring)
                break

    count = s.count(substring)
    return count

solution("abcabcabcabc")