def place_vertical_tables(matrix,x,y,z,currX,currY,deskindex):
    currY = 0
    while currY+2 < y:
        for j in range(0,3):
            if(currY >= y):
                break
            matrix[currY][currX] = 1
            currY+=1
        currY+=1

        deskindex+=1

    return matrix,x,y,z,currX,currY,deskindex

def place_horizontal_tables(matrix,x,y,z,currX,currY,deskindex):
    currX = 0
    while currX+2 < x:
        for j in range(0,3):
            if(currX >= x):
                break
            matrix[currY][currX] = 1
            currX+=1
        currX+=1

        deskindex+=1

    return matrix,x,y,z,currX,currY,deskindex

def do_sublvl(i):
    lvl = '4'
    example = False
    sublvl = str(i)

    filestr = 'level'+lvl+'/inputs/level'+lvl+'_'
    if example:
        filestr+='example'                                                
    else:
        filestr+=sublvl

    filestr += '.in'

    f = open(filestr ,'r',encoding='utf8')

    data = f.readlines()

    data = data[1:]

    for idx,room in enumerate(data):
        data[idx] = str.split(str.replace(room,'\n',''),' ') 

    print(data)

    output = ''
    deskindex = 0

    for idx,room in enumerate(data):
        x = int(room[0]) # cols
        y = int(room[1]) # rows
        z = int(room[2])

        matrix = [ [0]*x for i in range(y)]

        deskcountperLine = x // 3

        currX = 0 # col
        currY = 0 # row

        while deskindex < z and currY < y :
            matrix,x,y,z,currX,currY,deskindex = place_horizontal_tables(matrix,x,y,z,currX,currY,deskindex)

            currY += 2

        while deskindex < z and currX < x :
            matrix,x,y,z,currX,currY,deskindex = place_vertical_tables(matrix,x,y,z,currX,currY,deskindex)

            currX += 2

        deskindex = 0

        
        for i in range(len(matrix)):
            for j in range(len(matrix[1])):
                if matrix[i][j] == 1:
                    output += 'X'
                else:
                    output += '.'
            output += '\n'

        output+='\n'
    


    outputfilename = 'level'+lvl+'/outputs/level'+lvl+'_'
    if example:
        outputfilename+='example'                                                
    else:
        outputfilename+=sublvl

    outputfilename += '.out'

    outputfile = open(outputfilename,'w',encoding='utf8')
    outputfile.write(output)


for i in range(1,6):
    do_sublvl(i)
