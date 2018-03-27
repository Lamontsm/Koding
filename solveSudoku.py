# Create Cell object
#   Number value
#   original or not - boolean True if original
#   Trial cell values

class Cell():
    def __init__(self,val):
        self.value = val
        self.is_orig = False
        if val != None:
            self.is_orig = True
        
            
    # print out Cell values
    def print_out(self):
        print 'the value is ', self.value,' and it is original ', self.is_orig



# Load Grid object: 9 X 9
def load_grid(Grid, file_name):
    
    # Open the file for reading
    with open (file_name):
        lines = [line.rstrip('\n') for line in open(file_name)]
    
    # Load the grid
    for row in range(0,9,1):
        input_line = lines[row]
        for col in range(0,9,1):
            if (len(input_line) == 0):
                Grid[row][col] = Cell(None)
            elif (input_line[0:1] == ','):
                Grid[row][col] = Cell(None)
                input_line = input_line[1:]
            else:
                Grid[row][col] = Cell(input_line[0:1])
                input_line = input_line[1:]
                if len(input_line) > 0:
                    input_line = input_line[1:]


# Function to print full Grid
def print_grid(Grid):
    for row in range(0,9):
        line1 = ''
        line2 = ''
        if ((row == 3) or (row == 6)):
            print '-------------------------'
        for col in range(0,9):
            if Grid[row][col].is_orig == False:
                line1 += ' '
                line2 += ' '
            else:
                line1 += str(Grid[row][col].value)
                line2 += '-'
            line1 += ' '
            line2 += ' '
            if ((col == 2) or (col == 5)):
                line1 += ' | '
                line2 += ' | '
        print line1
        print line2
            

# Function to print single Cell instance

# Brute force solution
def brute_force(Grd):
    

#
# Main runner area
#

# Create a blank 9x9 list
Grid = [[0 for i in range(9)] for j in range(9)]

load_grid(Grid,'sudoku_input.txt')

print_grid(Grid)

#
# Run brute force solution
#
Grid1 = Grid




   

