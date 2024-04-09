## Data Sheet for Assignment 2

# Motivation
Why was the dataset created?

This dataset was generated within the scope of an educational assignment for CIS 6930, Spring 2024. The primary objective was to apply data augmentation methods to police incident records extracted from publicly available reports. By augmenting the dataset, the aim was to enhance its analytical potential while also considering aspects of fairness and bias.
Who created the dataset and on behalf of which entity?

The dataset was collaboratively created by students enrolled in the CIS 6930 course, under the auspices of the University of Florida's Department of Computer & Information Science & Engineering.

# Dataset Description:

This dataset encompasses augmented data extracted from police incident reports available on a public police department website. Each record within the dataset has been enriched to include not only the original incident details but also additional contextual information such as the day of the week, time of day, prevailing weather conditions at the incident location, and more. This augmentation process aims to enhance the dataset’s utility for deeper analysis and application in subsequent data processing stages.

# Methodology:

The augmentation process involved:

Extracting incident records from PDF files.
Augmenting records with the day of the week, time of day, weather conditions, location and incident ranks, and the presence of EMS (Emergency Medical Services) as denoted by an EMSSTAT flag.
Utilizing external APIs for geocoding (Geopy library) and weather data retrieval (OpenWeatherMap).
Ensuring the structured data format for ease of analysis.

# Attributes:
Day of the Week: Integer (1-7, where 1 = Sunday and 7 = Saturday)
Time of Day: Integer (0-24, representing the hour of the day)
Weather: Integer (WMO weather code representing the weather condition)
Location Rank: Integer (Frequency-based rank of the incident location)
Side of Town: String (N, S, E, W, NW, NE, SW, SE, based on the incident location's orientation from the town center)
Incident Rank: Integer (Frequency-based rank of the incident type)
Nature: String (Direct text of the incident type from the source record)
EMSSTAT: Boolean (True if EMS was involved, based on specific criteria)

# Data Collection Process:
Data was extracted using a Python script (assignment2.py) capable of parsing PDF files, extracting URLs from a provided CSV (files.csv), and performing data augmentation.

# Data Preprocessing:
Preprocessing steps included normalization of date and time formats, geocoding location names to latitude and longitude, and mapping weather conditions to standardized WMO codes.

# Distribution
How will the dataset be distributed?

The dataset, accompanied by the code used for its creation, will be made accessible through the course's designated online repository. Distribution is limited to educational use and is available to students and faculty members involved in the course.

