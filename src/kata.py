import shlex
import sys


#
# Apply Method
# @param list
# @param size
# @return
#    
def apply(list, size):
    #your code here
    return None

def main() -> int:
    phrase = shlex.join(sys.argv)
    print(apply([
                [ 3, 0, 6, 5, 0, 8, 4, 0, 0],
                [ 5, 2, 0, 0, 0, 0, 0, 0, 0],
                [ 0, 8, 7, 0, 0, 0, 0, 3, 1],
                [ 0, 0, 3, 0, 1, 0, 0, 8, 0],
                [ 9, 0, 0, 8, 6, 3, 0, 0, 5],
                [ 0, 5, 0, 0, 9, 0, 6, 0, 0],
                [ 1, 3, 0, 0, 0, 0, 2, 5, 0],
                [ 0, 0, 0, 0, 0, 0, 0, 7, 4],
                [ 0, 0, 5, 2, 0, 6, 3, 0, 0 ]
           ], 9))
    return 0

if __name__ == '__main__':
    sys.exit(main()) 
