import arcpy

# Set the input shapefile path
input_shapefile = r'C:\path\to\your\shapefile.shp'  # Update with your path
output_shapefile = r'C:\path\to\output\filtered_output.shp'  # Update with your output path

# Define the column and condition for filtering
field_name = 'X'  # Replace 'X' with your field name
filter_value = 'Y'  # Replace 'Y' with the value to filter on

# Create a SQL expression to filter features
sql_expression = f"{field_name} = '{filter_value}'"  # Use appropriate syntax for your data type

# Select features based on the SQL expression
arcpy.env.workspace = r'C:\path\to\workspace'  # Set workspace if needed
arcpy.management.SelectLayerByAttribute(input_shapefile, "NEW_SELECTION", sql_expression)

# Export the selected features to a new shapefile
arcpy.management.CopyFeatures(input_shapefile, output_shapefile)
