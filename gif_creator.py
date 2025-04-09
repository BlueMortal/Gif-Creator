import imageio.v3 as iio
filenames = [ '1 (1).png', '1 (2).png', '1 (3).png', '1 (4).png', '1 (5).png', '1 (6).png', '1 (7).png', '1 (8).png', '1 (9).png', '1 (10).png', '1 (11).png', '1 (12).png', '1 (13).png', '1 (14).png', '1 (15).png', '1 (16).png', '1 (17).png', '1 (18).png']
images = [ ]
for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('goku_approves.gif', images, duration = 100, loop = 0)