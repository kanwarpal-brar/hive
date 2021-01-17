# Hive
Streamlined ML Data Collection Platform Powered by the Dropbase API

# What It Does
Hive is a streamlined Machine Learning data collection platform. It aims to allow users to build Machine Learning datasets collaboratively and easily, so they can focus on the important parts of their project instead of having to get bogged down in trying to gather data. 

Users who are seeking data for a project can make a public post on the platform with the details on what type of data they want, and what they're collecting it for. From here, other users will be able to see the post and contribute their data by uploading files, thereby fostering a collaborative environment wherein users can assist one another in assembling robust datasets for use in machine learning projects of all shapes and sizes.

More specifically, when files are uploaded by a user, they are preprocessed according to their data type, stored in a temporary CSV file, and then added onto a database within a Dropbase project using the Dropbase API.

# How It Works 
Hive is a web app built using Django and Firebase, with the Tailwind CSS library used for front end styling. File uploading, preprocessing, and all related functions are handled through Python. All data is pushed to and retrieved from a Dropbase database, which is interfaced with through its API, using the Python requests module.
