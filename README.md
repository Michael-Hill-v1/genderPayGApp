Gender Pay G App
Version 1.0
29 April 2025
Michael Hill

The UK government requires employers with 250 or more employees to publish gender pay gap statistics.  These are made available via gov.uk.
This project allows the user to generate a PDF report of a selected employer's gender pay gap statistics.
To help improve understanding of what the statistics represent, the report includes details of how the statistics are calculated and comments on those calculations.
Additionally, the reported statistics are used in some further calculations to generate new information about the gender pay gap.
The code and the report text have not been reviewed.  For some employers, there will be odd-looking output reports.

This project contains two main Python scripts, GPG_DataDownload.py and GPG_ReportWriter.py.
The scripts use the following Python modules which may need to be installed before the scripts can be run:
- requests
- os
- pandas
- tkinter
- matplotlib
- FPDF2

Run script GPG_DataDownload.py first.
GPG_DataDownload.py copies all available gender paygap statistics from gov.uk to the 'data' folder in the project.

When the data download is complete, run GPG_ReportWriter.py.
From the pop-up box, select which year's data to report on.
Use the 'Search Names' box to search for an employer.
Use the 'Select output folder' to tell the script where to create the PDF.
Click 'Run report for selection' button to generate the PDF.

A draft version of this code produced additional PDF pages which compared the employer to a peer group.  However, different companies in the same industry can have very different structures.  The levels of pay at the median and the quartiles etc can potentially be very different from one company to the next.  There are no common reference points between the pay gap statistics for different companies, so it is not possible to make fair comparisons.
