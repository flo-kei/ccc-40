def do_sublvl(i):
    lvl = '1'
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

    for idx,line in enumerate(data):
        data[idx] = str.split(str.replace(line,'\n',''),' ') 

    print(data)

    output = ''

    for idx,line in enumerate(data):
        x = int(line[0])
        y = int(line[1])

        res = (x // 3) * y
        output += str(res) + '\n'


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