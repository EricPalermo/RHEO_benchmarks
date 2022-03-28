fin = open('data_equilibrated', 'r')
fout = open('data_with_grain', 'w')

# Simply copy first 5 lines until reaching the box size
for i in range(5):
    line = next(fin)
    fout.write(line)

line = next(fin)
fout.write(line)

# Remove the newline character and break the line into a list
row = line.strip().split()
xlo = float(row[0])
xhi = float(row[1])

box_length = xhi - xlo

# Copy header of data file up until the atom data
# (could of course also skip a fixed # of lines as before)
for line in fin:
    fout.write(line)
    if '# rheo' in line: break

# Skip the extra blank line
fout.write('\n')
next(fin)

# Finish reading the data file, processing each atom
# If an atom is in a sphere located in the middle with a radius of 5, change the phase
# Note the columns are:
# id type density temperature phase x y z
for line in fin:
    
    row = line.strip().split() 
    
    # Break from loop after processing all atoms (there's a blank line)
    if len(row) == 0: 
        fout.write('\n')
        break
    
    # Calculate position relative to center of box (7.937, 7.937, 7.937)
    x = float(row[5]) - box_length*0.5
    y = float(row[6]) - box_length*0.5
    z = float(row[7]) - box_length*0.5
    
    r = (x*x + y*y + z*z)**0.5
    
    # Change phase if within sphere
    if r <= 5:
        row[4] = '5'
        
    # turn list back into a string and write it to the data file
    output = ' '.join(row) + '\n'
    fout.write(output)

# Copy remaining lines to new file (velocity data)
for line in fin:
    fout.write(line)

fin.close()
fout.close()