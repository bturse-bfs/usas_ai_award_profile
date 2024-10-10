## Introduction
This guide describes the steps to identify awards with poor description values and download all information available on USAspending for those awards. This information can be processed by large language models to augment the information available on USAspending for each award. Transparency for awards with poor descriptions would especially benefit from LLM augmentation, but it would also be beneficial to apply this technique to other categories of awards.


## Installation and Support
This repo has only been tested on python version 3.10.11.
Users are encouraged to use a virtual environment.


## USAspending Key Resources
We recommend you review at least the **bold** materials.
- [Training videos](https://www.youtube.com/@usaspendinggov/videos)
  - **[TUTORIAL: How to Use USAspending Downloads](https://www.youtube.com/watch?v=5gMp2kyzEoo)**
  - **[TUTORIAL: How to Use USAspending API Endpoints](https://www.youtube.com/watch?v=AEKL2LOkRZY)**
- **[API documentation](https://api.usaspending.gov/) note: most download requests use POST)**
- **[Data dictionary](https://www.usaspending.gov/data-dictionary) (interpret download files)**
- [Federal spending guide](https://www.usaspending.gov/federal-spending-guide)
- [Data sources](https://www.usaspending.gov/data-sources)
- glossary (under Find Resources on USAspending.gov)


## Download an Award by ID
You can use the API to download all information about a specific award by ID.
1. Identify awards of interest (ie: awards with poor descriptions) and find an award's id.
    - Navigate to [USAspending advanced search](https://www.usaspending.gov/search).
    - Select filters of interest and run a search.
    - (Optional) Review the Award Description column in the Prime Award Results table.
    - Click the Prime Award ID in the Prime Award Results table to navigate to the award’s profile page.
    - Copy the last bit of the award profile page URL. This is the award id. Examples: `CONT_AWD_DEAC2701RV14136_8900_-NONE-_-NONE-`, `CONT_IDV_NNJ16GX08B_8000`, `ASST_NON_2105CA5MAP_7530`
2. Initate a download and receive data
   - update [`award_id` on award_profile_api_download.py](https://github.com/bturse-bfs/usas_ai_award_profile/blob/f39e56ee76f63b394038a2629228e16889b44e84/award_profile_api_download.py#L9)
   - Save and run the code snippet. This should download all relevant information about the award to a zip package on the client machine.


## Other Useful Information
[**Please complete the USAspending API developer survey!!**](https://forms.office.com/Pages/ResponsePage.aspx?id=is1pDRKeIU2V8LRAbgZxCosrFrEyW1NFiLX9Wji-iCxUQ0FHNlZMRFdCVlcyQ0VKVFNGOVRDR0lJUi4u)

Developers are encouraged to create solutions that could satisfy Treasury Department cloud security policy. For example, teams can use models available through [Amazon Bedrock](https://aws.amazon.com/bedrock/) to help ensure submissions meet these requirements.
