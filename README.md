# component_extractor
Python tool for extracting electrical component information from technical PDFs. Runs in the terminal. It does the following:

1. take in PDF input and JSON template of the desired information
2. Extract text from PDF
3. Run OCR on any text images, and combine any unique text with that previously extracted
4. Send a API request to chatGPT to populate the JSON data. Data not found in the provided text is left blank.
5. Outputs a .json file in the provided format with the appropriate component data filled out.

This tool can be used to automate library creation of electrical components from datasheets. I've mainly tested it with json data templates for electrical connectors, but it could easilly be used with any kind of datasheet information.

**To-do**
- Provenance identification. The ultimate goal is to highlight where data came from within the datasheet for each field. This allows quick and simple verification by the user.
- Automatic error identification of values
