import xml.etree.ElementTree as ET
from datetime import datetime

def ExtractHeartRateData(filePath, date):
    # Parse the XML file
    elmTree = ET.parse(filePath)

    # Get the root of the XML document
    rootElm = elmTree.getroot()

    # Find all 'Record' elements with attribute 'type' as 'HKQuantityTypeIdentifierHeartRate'
    heartRateRecords = rootElm.findall(".//Record[@type='HKQuantityTypeIdentifierHeartRate']")

    # Find all 'Record' elements with attribute 'type' as 'HKQuantityTypeIdentifierHeartRateVariabilitySDNN'
    heartRateVariabilityRecords = rootElm.findall(".//Record[@type='HKQuantityTypeIdentifierHeartRateVariabilitySDNN']")

    # Extract the 'value' attribute from each record
    heartRates = [(record.get('startDate'), record.get('value')) for record in heartRateRecords if datetime.strptime(record.get('startDate'), '%Y-%m-%d %H:%M:%S %z').date() == date]

    # Extract the 'value' and 'startDate' attributes from each HRV record
    heartRateVariabilities = [(record.get('value'), record.get('startDate')) for record in heartRateVariabilityRecords if datetime.strptime(record.get('startDate'), '%Y-%m-%d %H:%M:%S %z').date() == date]

    # Combine heart rate and HRV data
    combinedData = heartRates + heartRateVariabilities

    # Sort the combined data by timestamp
    combinedData.sort(key=lambda x: x[1])

    return combinedData


# Use the function
date = datetime.strptime('2024-05-20', '%Y-%m-%d').date()
heartRates = ExtractHeartRateData('../../../Desktop/apple_health_export/export.xml', date)
print(heartRates)
