# WebScrap Wuzzf    | Jobs [Project]
# Made By Arrow-Dev | (Ali-Hany)
# Made in 2/9/2024  | Last Update 2/9/2024
# visit us https://arrow-dev.rf.gd/bio





# Import Needed Library's
import requests
from bs4 import BeautifulSoup
import termcolor
import csv
import os
# Function That Will Unpack Elements
def unpack(soup : BeautifulSoup,list : list):
    for content in soup:
        if content:
            list.append(content.text.strip())

# The Job That User is Searching For | And The Variables We Will Use
            
jobs =  []
links = []
locations  =  []
exp = []

# Uncomment This Line After Finish
print(termcolor.colored("-> You Are Searching For : ",color="green"),end="")
job = input("").lstrip().lower()

# Requesting The Page

request = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q={job}").content
soup = BeautifulSoup(request,"lxml")

# Get Results Data

# 1 | Job Titles

job_titles = soup.find_all("a",{"class":"css-o171kl","rel":"noreferrer"})
# We Will Unpack Jobs Title But After Links Because We Will Extract Links From Jobs Titles

# 2 | Location
locations_soup = soup.find_all("span",{"class":"css-5wys0k"})
unpack(locations_soup,locations)

# 3 | Exp
exp_soup = soup.find_all("div",{"class":"css-y4udm8"})
unpack(exp_soup,exp)

# 4 | Links
for link in job_titles:
    links.append(link.attrs["href"])
# Now Lets Unpack Jobs Titles After We Got The Links
unpack(job_titles,jobs)

# 5 The Last Setup | Export The data | I'am Done So I told chatgpt to make this setup :v

# Combine all the lists into a list of tuples
result_data = list(zip(jobs, links, locations, exp))

# Specify the CSV file name
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
csv_path = os.path.join(desktop_path, 'result.csv')
# Writing to CSV file
with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write the header row
    csv_writer.writerow(['Job Title', 'Link', 'Location', 'Experience'])

    # Write the data rows
    csv_writer.writerows(result_data)

print(termcolor.colored(f"\n-> Results have been saved in {csv_path}", color="yellow"))