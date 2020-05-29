s=sorted(input('enter the string')) #taking input as a sorted list.
#print(s)
for i in range(len(s)):
    if s[i]==s[i+1]: # after sorting if two consecutive are same then it must be first reoccuring.
        print(s[i])
        break  # breaking loop after finding.
