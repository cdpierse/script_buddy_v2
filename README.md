# script_buddy_v2
 Script Buddy v2 is a dialogue completion and creation tool built using film scripts from the world's most popular film scripts. 


![Script Buddy APP](script_buddy/images/app.gif)
 
## Project Structure 
- *imsdb_scraper* contains the scrapy spider built to crawl IMSDB.com and download the film script data that is used to train our text generation model. 

    - To run the scraper change directory to imsdb_scraper with `cd imsdb_scraper`. As I haven't built any pipelines currently to run the scraper and save it's output simply run `scrapy crawl scriptSpider  -o scripts.json -t json` and for now manually move this output file to `script_buddy/data/` and you'll be good to go. 

- *script_buddy* contains the model classes and utility script parsing functions for cleaning up the film scripts to include only action descriptions, scene descriptions, and dialogue. 
