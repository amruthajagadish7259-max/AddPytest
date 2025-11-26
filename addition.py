def add(a,b):
     return a+b

if __name__ == "__main__":
    if len(sys.argv)>3:
       x=sys.argv[1]
      y=sys.argv[2]
else:
     x=10
     y=20
print("Sum:",add(x,y))




