main_string="ABCDCDC"
sub_string="CDC"

count=0

for i in range(len(main_string)-len(sub_string)+1):
    if main_string[1:1+len(sub_string)]==sub_string:
        count+=1
print("main string:",main_string)
print("substring:",sub_string)
print("number of occurrences:",count)
