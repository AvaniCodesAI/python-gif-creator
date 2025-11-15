import imageio.v3 as iio 

filenames = ['Didi1.png', 'Didi2.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('didi.gif', images , duration = 500, loop = 0) 