from django.shortcuts import render
from .csv_generator import createCSV, imagePreprocess, textPreprocess, audioPreprocess
from .dropbase_requests import uploadViaPresignedURL
from os import remove
import json
from uuid import uuid4
def index(request):
	return render(request, 'main/index.html')

def getstarted(request):
	return render(request, 'main/getstarted.html')

def contribute(request):
	# Set default variables 
	preprocessFunc = imagePreprocess

	if request.method == "POST":
		filesList = request.FILES.getlist('file_field')
		
		# Check the uploaded file type and set the appropriate preprocessing function
		fileType = filesList[0].content_type

		if fileType == "image/jpeg":
			preprocessFunc = imagePreprocess
		elif fileType == "text/plain":
			preprocessFunc = textPreprocess
		elif fileType[:5] == "audio":
			preprocessFunc = audioPreprocess

		# Generate a CSV file using the uploaded data and send the data to the Dropbase database
		csvFile = createCSV(filesList, preprocessFunc)
		uploadInfo = uploadViaPresignedURL(csvFile)
		remove(csvFile)

	return render(request, 'main/contribute.html')

def faq(request):
	return render(request, 'main/faq.html')