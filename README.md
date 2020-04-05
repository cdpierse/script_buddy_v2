# script_buddy_v2
 Script Buddy v2 is a film script text generation tool built using film scripts from the world's most popular film scripts. 

 Read more about the project on [Medium](https://towardsdatascience.com/film-script-generation-with-gpt-2-58601b00d371?source=friends_link&sk=934ac3ac7079d34bae215ce9a558986a) 

 I'm also a bot on twitter
 <blockquote class="twitter-tweet"><p lang="en" dir="ltr">28:orbs to<br> illuminate his face.<br><br> INT. WOODWARD&#39;S APARTMENT - NIGHT<br><br> Jac... <a href="https://t.co/AC7Bf1v6dj">pic.twitter.com/AC7Bf1v6dj</a></p>&mdash; Tales From The Script (@script_buddy) <a href="https://twitter.com/script_buddy/status/1246813191612641280?ref_src=twsrc%5Etfw">April 5, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> 


![Script Buddy APP](script_buddy/images/app.gif)
 
## Project Structure 
- *imsdb_scraper* contains the scrapy spider built to crawl IMSDB.com and download the film script data that is used to train our text generation model. 

    - To run the scraper change directory to imsdb_scraper with `cd imsdb_scraper`. As I haven't built any pipelines currently to run the scraper and save it's output simply run `scrapy crawl scriptSpider  -o scripts.json -t json` and for now manually move this output file to `script_buddy/data/` and you'll be good to go. 

- *script_buddy* contains the model fine tuning notebook, utility script parsing functions, tweepy bot code, and streamlit application code. 
    - If you'd like to run the streamlit app locally 
        - `git clone https://github.com/cdpierse/script_buddy_v2.git` 
        - `pip install -r requirements.txt`
        - `cd script_buddy`
        - `streamlit run app.py`

    - This should open an instance of the app for you to experiment with. Running it for the first time may take a 
    while as the model needs to be downloaded from huggingface's model hub. 
