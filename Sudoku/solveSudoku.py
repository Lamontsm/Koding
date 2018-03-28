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
    # Load opens list with spaces to fill
    opens = [(None,None)]
    for row in range(0,9):
        for col in range(0,9):
            if (not Grd[row][col].is_orig):
                opens.append([row,col])
    del opens[0] # remove starter pair
    
    # Loop through opens
    opens_index = 0
    
    while (opens_index < len(opens)):
        added_value = False
        print opens
        print opens_index
        row = opens[opens_index][0]
        col = opens[opens_index][1]
        if Grd[row][col].value == None:
            Grd[row][col].value = 1
        while ((Grd[row][col].value <= 9) and (not added_value)):
            chk_value = Grd[row][col].value
            if (chk_row(Grd, row, col, chk_value) and (chk_col(Grd, row, col, chk_value)) and (chk_sqr(Grd, row, col, chk_value))):
                added_value = True
            else:
                Grd[row][col].value += 1
        if (added_value):
            opens_index += 1
        else:
            opens_index -= 1
            
    return

def chk_row(Grd, row, col, val):
    not_found = True
    for i in range(0,9):
        if (Grd[row][i].value == val) and (col != i):
            not_found = False
            return
    return
    
    
def chk_col(Grd, row, col, val):
    for i in range(0,9):
        if (Grd[i][col].value == val) and (row != i):
            not_found = False
            return
    return
    
def chk_sqr(Grd, row, col, val):
    st_row = (int)(row/3)
    st_col = (int)(col/3)
    for i in range(st_row, st_row + 3):
        for j in range(st_col, st_col + 3):
            if (Grd[i][j].value == val) and (row != i) and (col != j):
                not_found = False
                return
        return
    
    
    
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

# Create a blank 9x9 list
Grid = [[0 for i in range(9)] for j in range(9)]

load_grid(Grid,'sudoku-almost-filled.txt')

print_grid(Grid)


#
# Run brute force solution
#
Grid1 = Grid

brute_force(Grid1)

print_grid(Grid1)



   

