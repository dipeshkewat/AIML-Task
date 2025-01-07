# File Handling


file = open("input.txt", "r") 
content = file.read()  
file.close() 

  
words = content.split() 
word_count = len(words) 

result_file = open("output.txt", "w") 
result_file.write(f"The file contains {word_count} words.\n") 
result_file.close()  

print("Word count has been written to 'output.txt.")
