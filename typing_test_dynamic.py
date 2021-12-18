import matplotlib.pyplot as plt
import time as t
times = []
mistakes = 0
print("this program will help you to type faster")
h = input("enter the word you want to type: ")
print("write the word", h , "5 times")
input("press enter to continue ")
while len(times) < 5:
    start = t.time()
    word = input("the word is: ")
    end = t.time()
    time_taken = end - start
    times.append(time_taken)
    if(word.lower() != h):
        mistakes = mistakes+1
print("you made",mistakes,"mistake(s)")
print("now let's see your evolution")
t.sleep(3)
x = ["1","2","3","4","5"]
y = times
plt.plot(x,y)
plt.ylabel("times in seconds")
plt.xlabel("attempts")
plt.title("your typing evolution")
plt.show()
plt.bar(x,y)