from PIL import Image
from PIL import ImageDraw
from random import randint
import sys


def LDRTransformImage(inputPath, outputPath = None, xOfsets = [], yOfsets = [], colorOfset = None):
	# Open the input image in memory
	with Image.open(inputPath) as im:
		draw = ImageDraw.Draw(im)

		out_im = Image.new(mode='RGBA', size=im.size, color=(0, 0, 0))
		draw = ImageDraw.Draw(out_im)

		if colorOfset == None:
			colorOfset = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

		while (len(colorOfset)>len(xOfsets)):
			xOfsets.append(randint(-10, 10));
		while (len(colorOfset)>len(yOfsets)):
			yOfsets.append(randint(-10, 10));

		

		layersNumbers = len(colorOfset);
		for j in range(im.size[1]):
			for i in range(im.size[0]):
				newPixelColor = [0, 0, 0]
				for layer in range(layersNumbers):
					if i-xOfsets[layer]>=0 and i-xOfsets[layer]<im.size[0] and j-yOfsets[layer]>=0 and j-yOfsets[layer]<im.size[1]:
						if im.load()[i-xOfsets[layer], j-yOfsets[layer]] != (0, 0, 0, 255):
							for c in range(3):
								newPixelColor[c] += colorOfset[layer][c]
				out_im.load()[i, j] = tuple(newPixelColor)

		out_im.save(outputPath if outputPath != None else ( (inputPath[:-4] + "_out.png") if inputPath[-4:] == ".png" else (inputPath + "_out.png")))
		out_im.close()


if __name__ == "__main__":
	inputPath = "input.png"
	LDRTransformImage(sys.argv[1] if len(sys.argv) >= 2 else inputPath)