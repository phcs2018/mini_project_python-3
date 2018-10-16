import optparse
import re


if __name__ == '__main__':
    parser = optparse.OptionParser('usage%prog -F <CC file>')
    parser.add_option('-F', dest="ccFile", type="string", help = 'Specify file with CC numbers')
    (options, args) = parser.parse_args()
    ccFile = options.ccFile

    if ccFile == None:
        print(parser.usage)
        exit(0)
        
    '''
        1) Open the file with potential credit card numbers, one on each line
        2) For each number, remove any trailing whitespace
        3) Create a regular expression to identify a valid credit card number
        4) Go through the file and print the total number of valid credit card numbers that you've found
    '''
    #### YOUR CODE HERE #####
 pattern = re.compile(r'^\d{4}-\d{4}-\d{4}-\d{4}$')
    pattern2 = re.compile(r'^\d{16}$')
    
    with open("ccnumbers.txt") as file:
        valid=0
        for ccnumber in file:
            ccnumber = ccnumber.strip()
            if pattern.match(ccnumber) or pattern2.match(ccnumber):
                print ccnumber
                valid += 1
        print(valid)
