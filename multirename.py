import glob, os, re
for file in glob.glob("*.mp4"):

    serialnumber=re.findall('\d+',re.sub(r'\.mp4$', '', file))[0]
    filename=re.sub(r'\.mp4$', '', file)
    digitcut=re.sub(r'\d+', '', filename)
    newfilename=serialnumber+" "+digitcut
    os.rename(file, file.replace(filename,newfilename))
    print (1)
