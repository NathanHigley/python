#list_example_two_0.py nh
filelist1 = ["IMG_001.png", "IMG_007.png", "IMG_011.png", "IMG_777.png"]
filelist2 = ["img-001.png", "img-002.png", "img-003.png", "img-004.png"]

for i in range(0,4):
    #print(filelist1[i], filelist2[i])
    print ("mv "+filelist1[i]+" "+filelist2[i]+";")
