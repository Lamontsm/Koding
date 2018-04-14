

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
                Grid[row][col] = Cell(0)
            elif (input_line[0:1] == ','):
                Grid[row][col] = Cell(0)
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
            if Grid[row][col].value == 0:
                line1 += ' '
                line2 += ' '
            elif not Grid[row][col].is_orig:
                line1 += str(Grid[row][col].value)
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

#
# Brute force solution
#
def brute_force(Grd):
    # Load opens list with spaces to fill
    opens = [(0,0)]
    for row in range(0,9):
        for col in range(0,9):
            if (not Grd[row][col].is_orig):
                opens.append([row,col])
    del opens[0] # remove starter pair
    
    # Loop through opens
    opens_index = 0
    
    while (opens_index < len(opens)):
        added_value = False
        # print opens
        # print opens_index
        row = opens[opens_index][0]
        col = opens[opens_index][1]
        # print row, col
        # print
        #if Grd[row][col].value == 0:
        Grd[row][col].value += 1
        while ((Grd[row][col].value <= 9) and (not added_value)):
            chk_value = Grd[row][col].value
            # print 'Trying ',chk_value,' in row ',row,' col ',col
            if (chk_row(Grd, row, col, chk_value) \
                and (chk_col(Grd, row, col, chk_value)) \
                and (chk_sqr(Grd, row, col, chk_value))):
                added_value = True
                print ('Found a match for row {}, col {}, value {}, and index {}'.format(row, col, chk_value, opens_index))
            else:
                Grd[row][col].value += 1
        if (added_value):
            opens_index += 1
            added_value = False
        else:
            opens_index -= 1
            Grd[row][col].value = 0    # Reset the one we were working on]
            print 'Go back  a level to index ',opens_index
            if opens_index < 0:
                print "No valid solution exists"   # We must have exhausted all possibilities
                return
            
    # print 'We are done!'
    # print_grid(Grd)
    return

def chk_row(Grd, row, col, val):
    for i in range(0,9):
        if (Grd[row][i].value == val) and (col != i):
            return False
    return True
    
def chk_col(Grd, row, col, val):
    for i in range(0,9):
        if (Grd[i][col].value == val) and (row != i):
            return False
    return True
    
def chk_sqr(Grd, row, col, val):
    st_row = (int)(row/3) * 3
    st_col = (int)(col/3) * 3
    for i in range(st_row, st_row + 3):
        for j in range(st_col, st_col + 3):
            if (Grd[i][j].value == val) and (row != i) and (col != j):
                return False
    return True
    
#
# Random Value solution
#
def random_value(Grid):
    # Create list of empty cell locations, with counter
    opens = [(0,0,0,0)]
    for row in range(0, 9):
        for col in range(0, 9):
            if (not Grid[row][col].is_orig):
                opens.append(Opens(row, col))
    del opens[0] # remove starter pair
    
    # Fill each empty cell with random number
    # random.randint(1, 10)  # Integer from 1 to 10, endpoints included
    for i in range (0,len(opens)):
        rand = randint(1, 9)
        opens[i].val = rand
        Grid[opens[i].row][opens[i].col].value = rand
        print
        print_grid(Grid)
    
    # Set boolean for solved to False
    
    # Run loop until solved 
    
        # Count number of collisions for each cell - by row, col, and box
        
        # Check if no collisions, return if none
        
        # Select cell with most collisions. Consider weighted selection for randomization
        
        # Put different random number in selected cell

# Create Cell object
#   Number value
#   original or not - boolean True if original
#   Trial cell values

class Cell():
    def __init__(self,val):
        self.value = (int)(val)
        self.is_orig = False
        if val != 0:
            self.is_orig = True
        
    # Try function to set cell value
    # May not be needed
    # def reset_value(self, new_val):
    #     print 'I am in function to reset my value'
    #     self.value = new_val
        
            
    # print out Cell values
    def print_out(self):
        print 'the value is ', self.value,' and it is original ', self.is_orig

#
# Set up object for holding open cells in random function
# row is row
# col is column
# val is random value set
# weight is weighted value
#
class Opens():
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.val = 0
        self.weight = 0
        
    
# Experimenting with lists
# a = [(None,None)]
# print a
# print a[0][0]
# a.append([3,2])
# print a
# del a[0]
# print a
# print a[0][1]    

#
# Main runner area
#



#
# Run brute force solution
#
# Create a blank 9x9 list
Grid = [[0 for i in range(9)] for j in range(9)]
load_grid(Grid,'sudoku-almost-filled2.txt')

# Run brute force model
# TODO need to add timing
# print_grid(Grid) # turned off while adding functions
# Grid1 = Grid
# brute_force(Grid1)
# print
# print_grid(Grid1)

# Run random model
Grid2 = Grid
from random import randint
print_grid(Grid2)
print
random_value(Grid2)


    