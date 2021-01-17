from csv import writer
from base64 import b64encode
from uuid import uuid4
from PIL import Image
from os import remove
from .dropbase_requests import databaseQuery
from librosa import load

# Convert images to base64 strings for storage
def imagePreprocess(inputFile):
	filename = "main/static/data/" + str(uuid4()) + ".jpg"
	rawImgFile = open(filename, "wb")
	rawImgFile.write(inputFile.read())
	rawImgFile.close()

	img = Image.open(filename).resize((100,100)).save(filename)

	updatedImg = open(filename, "rb")
	updatedImgData = updatedImg.read()
	updatedImg.close()
	remove(filename)

	return [filename[17:], b64encode(updatedImgData)]

def textPreprocess(inputFile):
	return [inputFile.name, inputFile.read().decode("latin-1")]

def audioPreprocess(inputFile):
	return [inputFile.name, load(inputFile)]

# Generate CSV file using given input files
def createCSV(fileList, func):
	csvFilename = "main/static/data/" + str(uuid4()) + ".csv"

	with open(csvFilename, "w", newline="") as csvFile:
		csvWriter = writer(csvFile)
		csvWriter.writerow(["id", "filename", "data"])

		i = databaseQuery()[-1]['id']
		for file in fileList:
			i += 1
			processResult = func(file)
			csvWriter.writerow([i, processResult[0], processResult[1]])

	return csvFilename