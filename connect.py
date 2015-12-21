from PIL import Image

x_min = 0
y_min = 0
x_max = 19
y_max = 19

file_name_prefix = '030000'
file_name_suffix = 'png'

tile_width = 550
tile_height = 550

output_width = 550 * (x_max+1)
output_height = 550 * (y_max+1)

im_destination = Image.new('RGB', (output_width, output_height))

for i in range(x_min, x_max+1):
    for n in range(y_min, y_max+1):
        in_file = file_name_prefix+"_"+str(i)+"_"+str(n)+"."+file_name_suffix

        left_pos = tile_height*(i)
        right_pos = tile_height*(i+1)
        top_pos = tile_width*(n)
        bottom_pos = tile_width*(n+1)

        try:
            print "Openning image: "+in_file
            im_input = Image.open(in_file)

            box = (left_pos, top_pos, right_pos, bottom_pos)
            print box

            im_destination.paste(im_input, box)
        except IOError:
            print("cannot create thumbnail for ", in_file)

im_destination.show()

im_input.close()
im_destination.close()
