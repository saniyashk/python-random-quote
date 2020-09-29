import random
def main():
    #print("Keep it logically awesome.")

  f = open("quotes.txt","a+")
  quotes = f.readlines()
  x = ["old is gold","procastination is the thief of time"]
  quotes.append(x)
  f.close()
  #last = 13
  #rnd = random.randint(0,last)
  print(quotes)
  

if __name__== "__main__":
  main()
