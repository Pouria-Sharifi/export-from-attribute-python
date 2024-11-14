# export-from-attribute-Python
This repository contains a Python script that extracts and exports data from an attribute table.
Shapefile Filter and Export Script:

Overview:
This project provides a utility for filtering features from a shapefile's attribute table based on specific conditions and exporting the filtered results to a new shapefile. The tool is built using Python and ArcPy to streamline data extraction and processing within GIS workflows.

Key Features:
Filters shapefile features based on specified column values or conditions.
Exports filtered results to a new shapefile for further analysis or use.
Simple and customizable configuration for specifying input data and filtering criteria.

Requirements:
ArcGIS Pro or a compatible Python environment with ArcPy installed.
A valid input shapefile.

Installation:
Ensure you have ArcGIS Pro installed with access to the ArcPy package.
Place the input shapefile in a directory accessible by your Python environment.

Usage:
Configure the tool by specifying the input shapefile path, output file path, column to filter, and values or conditions for filtering.
Execute the script through the ArcGIS Pro Python window or any Python IDE with ArcPy access.
The filtered features will be saved to the specified output location.

Customization:
Users can modify the filter conditions to match their data needs (e.g., filter by specific values, ranges, or string patterns).
The output file format can be changed based on the requirements (e.g., export to GeoJSON or other formats supported by ArcPy).

Notes:
Ensure that the specified filter conditions align with the data type of the field being filtered (e.g., numeric, string).
Proper permissions may be required to read and write to the specified file locations.

License:
This project is licensed under the MIT License.


Example code:
import arcpy

# Set the input shapefile and output path
input_shapefile = r'C:\path\to\your\landcover.shp'  # Update with your path
output_shapefile = r'C:\path\to\output\filtered_landcover.shp'  # Update with your output path

# Define the column (field) and filter values
field_name = '2013'  # Field name to filter
filter_values = (200, 215)  # Values to filter on

# Create a SQL expression for filtering features
sql_expression = f"{field_name} IN {filter_values}"  # This will create "2013 IN (200, 215)"

# Select features based on the SQL expression
arcpy.env.workspace = r'C:\path\to\workspace'  # Set workspace if needed
arcpy.management.SelectLayerByAttribute(input_shapefile, "NEW_SELECTION", sql_expression)

# Export the selected features to a new shapefile
arcpy.management.CopyFeatures(input_shapefile, output_shapefile)
 
