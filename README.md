# script_buddy_v2
 Script Buddy v2 is a film script text generation tool built using film scripts from the world's most popular film scripts. 


![Script Buddy APP](script_buddy/images/app.gif)
 
## Project Structure 
- *imsdb_scraper* contains the scrapy spider built to crawl IMSDB.com and download the film script data that is used to train our text generation model. 

    - To run the scraper change directory to imsdb_scraper with `cd imsdb_scraper`. As I haven't built any pipelines currently to run the scraper and save it's output simply run `scrapy crawl scriptSpider  -o scripts.json -t json` and for now manually move this output file to `script_buddy/data/` and you'll be good to go. 

- *script_buddy* contains the model fine tuning notebook, utility script parsing functions, tweepy bot code, and streamlit application code. 
    - If you'd like to run the streamlit app locally 
        - `git clone https://github.com/cdpierse/script_buddy_v2.git` 
        - `pip install requirements.txt`
        - `cd script_buddy`
        - `streamlit run app.py`

    - This should open an instance of the app for you to experiment with. Running it for the first time may take a 
    while as the model needs to be downloaded from huggingface's model hub. 
