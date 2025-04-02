# mode = 'r ----> read operations
# file = open("demo.txt",mode = 'r')
# read_data = file.read()
# print(read_data)
# file.close()

#readline()
# file = open("demo.txt",mode = 'r')
# read_data = file.readline()
# print(read_data)
# file.close()

#readlines()
# file = open("demo.txt",mode = 'r')
# read_data = file.readlines()
# print(read_data)
# file.close()

# read ---> total read
# readline----> single line(first line)
# readlines----> total data into list format [list of substring]

## Mode = 'a'----> append operation
#write()
# file = open("demo.txt",mode= 'a')
# write_data = file.write("\n this is write operation performing using mode = 'a' ")
# file.close()

# file = open("demo_1.txt",mode= 'a')
# write_data = file.write("\n this is write operation performing using mode = 'a' ")
# file.close()




## Mode = 'w'
## write
# file = open("demo.txt",mode= 'w')
# write_data = file.write("this is write operation using w mode\n this is python class")
# file.close()

# # create a new file.txt
# file = open("sample.txt", mode= 'w')
# write_data = file.write("this is write operation using w mode\n this is python class")
# file.close()


## writelines ----> list of strins into file formate
# emp_data = ["vasu\n","mohan\n","ajay\n","sneha\n","deepthi\n","naidu\n","reddy"]
# file = open("demo.txt",mode= 'w')
# write_data = file.writelines(emp_data)
# file.close()


## mode = 'w+'
# file = open("santosh.txt",mode= 'w+')
# write_data = file.write("sampletest")
# print(file.tell())
# file.seek(0)
# read_data = file.read()
# print(read_data)
# file.close()

# file = open("C:\\Users\\U Sandeep\\OneDrive\\Desktop\\New Text Document.txt", mode = 'r')
# read_data= file.read()
# print(read_data)
# file.close()

# file = open("C:\\Users\\U Sandeep\\OneDrive\\Desktop\\New Text Document_123.txt",mode= 'w')
# write_data = file.write("sample data creating file on desktop")
# file.close()

## mode= 'r+'

# file = open("demo.txt",mode='r+')
# read_data = file.read()
# print(read_data)

# file = open("demo.txt",mode='r+')
# read_data_1 = file.readline()
# print(read_data_1)

# file = open("demo.txt",mode='r+')
# read_data_2 = file.readlines()
# print(read_data_2)

# file = open("santosh.txt",mode='r+')
# write_data = file.write("saleem\n naveen\n")
# file.close()

# file = open("demo.txt",mode= 'r+')
# write_data= file.write("mits\n")
# print(file.tell())
# file.seek(0)
# read_data = file.read()
# print(read_data)
# file.close()

## mode= a+
# file = open("demo.txt",mode= 'a+')
# # write_data= file.write("mits\n")
# # print(file.tell())
# file.seek(0)
# read_data = file.read()
# print(read_data)
# file.close()

file = open("C:\\Users\\U Sandeep\\OneDrive\\Desktop\\New Text Document_124.txt",mode= 'a+')
write_data = file.write("sample data creating file on desktop")
file.close()