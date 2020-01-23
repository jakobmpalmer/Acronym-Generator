#python anagram project
import sys

ourfile = sys.argv[1]

#------------------------------------------------------------------------------
# Methods
#------------------------------------------------------------------------------

def main():
    print("Welcome to main")
    targetname = input("Please enter a name\n")
    acronym = []
    print("Ok! Your target name is,", targetname)
    targetchars = list(targetname)
    print(ourfile)
    print(targetchars)
    for letter in targetchars:
        print("Current LETTER:", letter)
        if SearchTable(letter) != None:
            print(SearchTable(letter))
            acronym.append(SearchTable(letter))
        else:
            print("_")
            acronym.append('_')
    print("your acronym is, ", acronym)

#---------------------------------------------------- |

def SearchTable(letter):
    names = open(ourfile).read().splitlines()
    for name in names:
        #print("Current Name", name)
        if name[0] == letter.capitalize():
            #print("Found a", letter)
            #print("adding", name)
            return name
    print("done searching..")



print("hello world\n----------------\n")

#------------------------------------------------------------------------------
#main()
if __name__ == "__main__":
    main()

print("\n\nGoodbye world")


