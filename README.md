## Ookla NetIndex Data

Estimates of Internet speed by city, country, and region between 2008--2014, 2010--2014, and . 

The data on Internet speed estimates from 2008--2014 are from the now defunct http://www.netindex.com/, a website run by [http://www.ookla.com/](http://www.ookla.com/)). They can be downloaded from [http://dx.doi.org/10.7910/DVN/UL7NYU](http://dx.doi.org/10.7910/DVN/UL7NYU). Please read the readme file, which has the licensing information, before using the data.

[netindex_by_year.py](netindex_by_year.py) groups city daily speeds data by year and calculates average speed per year, and joins the data with [town to zip code crosswalk](data/zip_code_town.csv). The final output is at: [data/netindex_by_year.csv](data/netindex_by_year.csv). 

### Notes

* Only 18 cities have download speeds of less than 200 kbps.
* They are some regions/cities that do not match with any zip code.
* The script is from 2014
