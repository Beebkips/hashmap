import exifread
# Open image file for reading (binary mode)

def getExifinImage( imageinput ):
	f = open(imageinput, 'rb')
	tags = exifread.process_file(f)
	return tags

imageinput = '/Users/vikasmohandoss/Documents/hashmap/images/IMG_0953.jpg'
tags = getExifinImage( imageinput )
for tag in tags.keys():
    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
        print "Key: %s, value %s" % (tag, tags[tag])
