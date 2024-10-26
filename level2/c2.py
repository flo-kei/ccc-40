def do_sublvl(i):
    lvl = '2'
    example = True
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
    deskindex = 1

    for idx,room in enumerate(data):
        x = int(room[0])
        y = int(room[1])
        z = int(room[2])

        #res = (x // 3) * y

        deskcountperLine = x // 3

        while deskindex < z:
            for i in range(0,deskcountperLine):
                output += str.format('{0} ',deskindex) * 3
                deskindex+=1
            output += '\n'

        output += '\n'
        deskindex = 1


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
