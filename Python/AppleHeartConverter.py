import xml.etree.ElementTree as ET

def ExtractHeartRateData(filePath):
    # Parse the XML file
    elmTree = ET.parse(filePath)

    # Get the root of the XML document
    rootElm = elmTree.getroot()

    # Find all 'Record' elements with attribute 'type' as 'HKQuantityTypeIdentifierHeartRate'
    heartRateRecords = rootElm.findall(".//Record[@type='HKQuantityTypeIdentifierHeartRate']")

    # Find all 'Record' elements with attribute 'type' as 'HKQuantityTypeIdentifierHeartRateVariabilitySDNN'
    heartRateVariabilityRecords = rootElm.findall(".//Record[@type='HKQuantityTypeIdentifierHeartRateVariabilitySDNN']")

    # Extract the 'value' attribute from each record
    heartRates = [record.get('value') for record in heartRateRecords]

    return heartRates

# Use the function
heartRates = ExtractHeartRateData('../../../Desktop/apple_health_export/export.xml')
print(heartRates)
