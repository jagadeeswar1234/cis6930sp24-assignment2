# CIS 6930 Data Augmentation Assignment

## Author
Name: Jagadeeswara Reddy Gummi Reddy
UFID : 50955833

## Introduction
Building upon the groundwork laid in the first assignment, this next phase in our series focuses on the refinement of police incident data previously compiled. The objective here is to enrich these foundational records with critical enhancements, including the precise timing of incidents and the weather conditions at those moments. This step is undertaken with a keen emphasis on ensuring equity and minimizing bias throughout the dataset. Such detailed augmentation not only deepens our capacity for insightful analysis but also prepares the dataset for subsequent processes in an elaborate data workflow.

## Running instructions

To run the assignment2.py script effectively, ensure you have Python 3.11.0 and the required libraries (requests, PyPDF2, geopy, etc.) installed on your system.

## Setting Up the Environment

# Python Installation:
Verify the installation of Python 3.11.0 on your system. You'll also need pipenv to manage the project's virtual environment and its dependencies:

pip install pipenv

## Installing Dependencies

# Project Dependencies:

In the project's root directory, install the necessary dependencies by executing:

pipenv install

## Activating the Virtual Environment
# Virtual Environment:

Activate your project's virtual environment with the following command:

pipenv shell

Alternatively, you can run commands directly within the virtual environment by using pipenv run before your script command.

## executing the script
# Script execution
Launch the assignment2.py script using the command below:

pipenv run python assignment2.py --urls <Path to your CSV file>

Ensure to replace <Path to your CSV file> with the actual file path leading to your CSV document, which must enumerate the URLs to the incident report PDFs.

Following these instructions will enable you to successfully execute the script and analyze the enhanced dataset it generates.

## Function descriptions

# fetch_pdf(url)
Description: Downloads a PDF document from the provided URL and saves it to a specified local directory.
Parameters: url (string) - The web address of the PDF file to download.
Outcome: Does not return a value. The PDF is stored locally.

# parse_incidents(pdf_path)
Description: Parses incident information from the specified PDF file, organizing data into a structured format.
Parameters: pdf_path (string) - The file path to the downloaded PDF document.
Outcome: Returns a list of structured incident data extracted from the PDF.

# rank_locations(incidents)
Description: Determines the ranking of each incident location based on occurrence frequency, sorting ties appropriately.
Parameters: incidents (list) - A collection of incident records.
Outcome: Produces a mapping of location names to their respective frequency-based ranks.

# weekday_from_date(date_time_str)
Description: Translates a datetime string into a numerical representation of the week's day.
Parameters: date_time_str (string) - A string representing date and time.
Outcome: Yields an integer symbolizing the day of the week.

# hour_of_incident(date_time_str)
Description: Extracts the hour from a datetime string, indicating when an incident occurred.
Parameters: date_time_str (string) - The datetime string from the incident data.
Outcome: An integer indicating the hour of the day (0-23).

# fetch_weather_condition(api_key, date_time_str)
Description: Retrieves specific weather conditions using an external API based on the incident's datetime and location.
Parameters:
api_key (string) - The API key for accessing the weather service.
date_time_str (string) - The datetime string for the incident.
Outcome: Returns an integer representing the weather condition according to a predefined code mapping.

# geocode_location(location_name, try_count=1, max_tries=3)
Description: Converts a textual location into geographical coordinates using a retry mechanism for reliability.
Parameters:
location_name (string) - The name of the location to geocode.
try_count (int) - The current attempt count (used for retries).
max_tries (int) - The maximum number of geocoding attempts.
Outcome: A tuple of latitude and longitude, or (None, None) if unsuccessful.

# calculate_direction(center_lat, center_lon, incident_lat, incident_lon)
Description: Computes the directional bearing from a central point to the incident's location.
Parameters:
Latitude and longitude of both the town center and the incident site.
Outcome: A floating-point number indicating the bearing in degrees.

# identify_town_quadrant(bearing)
Description: Determines which quadrant of the town the incident occurred in based on bearing.
Parameters: bearing (float) - The computed bearing to the incident location.
Outcome: A string indicating the town quadrant (e.g., 'NE', 'SW').

# assign_incident_ranks(incidents)
Description: Ranks incident types by their frequency of occurrence, resolving ties equitably.
Parameters: incidents (list) - A list of incident entries.
Outcome: A dictionary associating incident types with their rank.

# evaluate_ems_involvement(incident, all_incidents, index)
Description: Checks whether an incident involved EMS services based on specified criteria.
Parameters:
incident (list) - The current incident under evaluation.
all_incidents (list) - The complete list of incidents.
index (int) - Index of the current incident in the list.
Outcome: Boolean indicating EMS involvement.

# enhance_incident_data(incidents, location_ranks, type_ranks, weather_api_key)
Description: Enriches each incident record with additional data, including weather conditions and temporal details.
Parameters:
Lists of incidents and their ranks, along with the weather service API key.
Outcome: An augmented list of incidents with added details for each record.

# retrieve_urls_from_file(file_path)
Description: Extracts a list of PDF file URLs from a specified CSV file.
Parameters: file_path (string) - Path to the CSV file containing PDF URLs.
Outcome: A list of URLs for processing.

# display_augmented_data(augmented_records)
Description: Outputs the enhanced incident

## Testing Procedure

# validate_time_extraction(): 
Confirms that the time extraction from a datetime string functions as expected.

# verify_weekday_calculation(): 
Checks that the calculation for identifying the weekday from a datetime string is accurate.

These testing methods are housed within the tests/ folder and are designed for assessing the reliability and accuracy of their corresponding features.

## Assumptions

The process of extracting information from PDFs presupposes a uniform format across all police incident reports, especially regarding the positioning of critical details such as date-time, location, nature of the incident, and other pertinent data.

For the transformation of incident report locations into geographic coordinates, it is assumed that these textual descriptions can be precisely mapped to latitude and longitude values utilizing the capabilities of the Geopy library.

Retrieving weather data depends on the reliable function of an external service (OpenWeatherMap), with the expectation that it consistently provides accurate historical weather conditions for the given locations and times.

Identifying instances where emergency medical services were involved, denoted by the EMSSTAT flag, is based on the expectation of encountering specific indicators or keywords within the text of the incident reports.

The enhancement of the dataset with additional attributes—such as the day of the week, time of day, and weather conditions—rests on the assumption that the original incident reports offer a comprehensive and accurate foundation from which these features can be derived.







