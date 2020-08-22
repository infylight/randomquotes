# create a file using a quotes_source.txt as name in same file directory 
# make the quotes end with "***" to separate them 
import random
import math 
from time import perf_counter_ns
f = open("quotes_source.txt","r")
quotes = f.read()
quotes_list = quotes.split("***\n")
quotes_list_1 = []
start = perf_counter_ns()
for x in quotes_list:
    x = x.replace("\n"," ",100)
    quotes_list_1.append(x)
no_of_quotes = len(quotes_list_1) -1
stop = perf_counter_ns()
random.seed(start*stop+512)
random_quote_no = random.randint(0,no_of_quotes-1)
print(quotes_list_1[random_quote_no])








