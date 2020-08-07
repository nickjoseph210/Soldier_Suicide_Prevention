# Soldier_Suicide_Prevention

This is a personal passion project revolving around the reports that between 20 and 22 veterans commit suicide every day.

I grew up in San Antonio, TX and was on my way to the MCRC before a family event stopped me in my tracks.  Since then, I have always held the men and women of our Armed Forces in high regard, and find it downright unjust that they - or any first responder - intentionally *volunteer* to fight outside evils only to succomb to one that is inside.  

Suicide itself is a complex issue, involving both psychological and physiological disturbances only understood by the person contemplating it as a possibility.  The aim of this research is to see what story the data tells, and what (if any) patterns can be observed before such a family trauma takes place.    

## On Working with GoogleSheets API and Not Excel

For this project, I am using a MacBook Pro, Model A1502.  

Throughout Codeup's Data Science program, we used Excel spreadsheet data that was provided to us either by our instructors - whenever it was read into a pandas dataframe, the dataframe reflected it in easy-to-read format with all the information we would need to conduct our research.  Sure, the data was messy and needed some cleaning, but importing it into Pandas (via Jupyter Notebook, it should be mentioned) was smooth and seamless.   

As I discovered when working on the Capstone Project ['Data and Urban Development'](https://codeup.com/curie/), importing Excel data from the wild is anything but smooth.  Even when I attempted a new subscription, I was unable to code an import - line, loop, function, whatever - that would fetch the Excel data and put it into a Pandas dataframe for analysis.  

Not sure if this is because of an issue between Apple and MS compatibilities, but that's something to resolve at another time.  I want to get this project going, so instead of using XL (the format of the original data) I have chosen to use Google Sheets.

All the info from the original XL file was copied and pasted into Google Sheets - literally: just highlighted and right-clicked from the XL files and pasted into Google Sheets; headers got the full cell contents, whereas values were copied over using 'values only' option. The decision to do so was because I was afraid any discrepancies in formatting would tarnish the original values of the cells during the transfer.  After checking over the spreadsheets, it looks like all cell values are identical, and I can proceed with confidence.

### Importing Multiple Google Sheets Into Pandas DataFrame

Whenever I import Google Sheets into Pandas, I typically use a standard coding process:

1.) Once the Sheet is ready for import, it has to be shared from Google.  During this process, the restrictions on who can view the data are lifted and the link to the sheet is copied;

2.) Switching over to my open Jupyter Notebook, I paste the link into the available cell;

3.) Google Sheet links (the ones that are shared, anyway) follow a standard format:

    https: //docs.google.com/spreadsheets/d/ SOME UNIQUE IDENTIFIER / edit?usp=sharing

That 'SOME UNIQUE IDENTIFIER' part is then assigned to a variable (usually, 'sheet_id = SOME UNIQUE IDENTIFIER'); and

4.) From there, the Sheet is read - imported - into a Pandas DataFrame as a 'csv' file, just like one would do with a standard XL file.  To do this, all one has to do is edit the last part of the link format from 'edit?usp=sharing' to 'export?format=csv' while using a formatted string to do all the work.  

**Typical codeblock for this looks like:**

```python
# Assign unique identifier to a variable

sheet_id = SOME UNIQUE IDENTIFIER

# Import the file and assign it to the variable 'df,' which is short for 'dataframe'

df = pd.read_csv(f"https: //docs.google.com/spreadsheets/d/ {sheet_id} / export?format=csv")

# Check to see how the import went by looking at the first 25 rows

df.head(25)
```

All well and good, but I ran into the problem of having multiple sheets of data - multiple tabs - I wanted to explore on the same Google Sheet.  Repeating the code block above does me no good, for all it can do is continue to import the same data as it did the first go-round.

So I had to explore something different, which led me to various suggestions of using the Google Sheets API.  