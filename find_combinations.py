import sys

def main():
    line_count = 0
    for line in sys.stdin:
        if line_count == 0:
            #do stuff with headers if you want
            pass
        else:
            #removes whitespace and the end line characters "\n" "\r"
            line = line.rstrip()
            print(line.split(','))
        line_count+=1

if __name__ == "__main__":
    main()