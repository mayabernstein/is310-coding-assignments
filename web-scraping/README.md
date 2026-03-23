### **Fairy Tail - Fandom Wiki** 

#### Fandom Wiki
Wiki: Fairy Tail

Page scraped: https://fairytail.fandom.com/wiki/Fairy_Tail_(Guild)

robots.txt: https://fairytail.fandom.com/robots.txt

#### Terms and Conditions 
Upon looking at the robots.txt, there are no restrictions on the webpage I have chosen, so I can scrape it.

#### Why this fandom wiki and what did I scrape? 
I chose this fandom wiki because it is the anime that got my childhood friend and me as close as we are now. From this wiki, I am interested in scraping the characters within the Fairy Tail guild (the main guild in the show). From there, I would like to include a webpage to each corresponding character. 

#### Why I think the data I scraped might be of interest or useful to researchers? 
I think the data I scraped would be useful to researchers because it provides a structured dataset of characters within the Fairy Tail guild, including their names, statuses, and links to detailed character pages. This allows for the data to be easily analyzed compared to the unstructured format from a webpage. 

Researchers that are interested in character networks and animated storytelling could use this dataset to examine relationships between characters, track the current character roles (e.g. active vs. left guide). The includion of the links to each character's webpage allows for deeper data collection of the character's backgrounds and development arcs throughout the series. 

#### Output File 

| Column Name | Description | Possible Values / Notes |
|------------|------------|------------------------|
| **Name** | Name of the Fairy Tail character | e.g. Happy, Lucy |
| **Status** | The character's current state within the fandraise | e.g., Active, Left Guild, Deceased, Excommunicated |
| **Link** | A link to the corresponding character's webpage | e.g. /wiki/Happy |

Example:

```csv
name,status,link
Makarov Dreyar,Active,/wiki/Makarov_Dreyar
Gildarts Clive,Active,/wiki/Gildarts_Clive
Laxus Dreyar,Active,/wiki/Laxus_Dreyar
```