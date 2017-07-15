# Intangible Cultural Heritage in the Historic County of Glamorgan: Twitter Analysis

Real quick script to scrape some data from twitter for various hash tags, then perform some language analysis on it. Details are provided below.

## Authors

This work was conducted by Dom Weldon<sup>1</sup> and Amy Dolben<sup>2</sup>.

1. Department of Digital Humanities, King's College London: dominic.weldon@kcl.ac.uk.
2. Department of Archaeology, University of Cambridge: ad696@cam.ac.uk.

## Attribution

* AD designed the research and data to be collected.
* DW was responsible solely for the technical work to extract the data and the code to combine it with Google's language detection algorithm to produce results (as CSV files), which were then passed to AD for qualitative analysis.
* DW used `pandas` to provide summary statistics to AD and created charts which were pased to AD using `matplotlib`.

DW's research is funded by a Collaborative Doctoral Award from the Arts and Humanities Research Council in collaboration with BT and the Science Museum Group.

## Methodology

All work was conducted using python 3, and the code is available online at this repository.

### Data Extraction

* Searches were conducted for two terms related to Welsh cultural events in the region: `tafwyl` and `urdd2017`. Tweets containing these terms were extracted from the Twitter Search API using the open method as implemented in Python by [Tom Dickinson](https://github.com/tomkdickinson/Twitter-Search-API-Python).
* Tweets were gathered from anywhere in the world with no locational filter.
* Tweets were initially extracted in reverse time order over a date range covering from the date of the search (14 July 2017), to either the term's first appearance or to the 5,000th tweet from the most recent tweet - whichever was the lesser. The date ranges covered were as below.

| Search Term | Total Tweets | First Tweet Date      | Last Tweet Date       |
| ----------- | ------------ | --------------------- | --------------------- |
| `tafwyl`    | 5,000        | 2017-07-14 09:59:35   | 2015-07-06 11:37:37   |
| `urdd2017`  | 4,888        | 2017-07-06 13:28:41   | 2014-05-13 16:46:06   |

_In the case of the `urdd2017` search, one tweet, which was created by the researchers performing the analysis whilst testing the extraction method was removed from the data set._

* The tweets were stored as JSON, and then converted to CSV using the `pandas` data handling library.
* Tweets were further filtered to cover only the period from one week before the event, to one week after it.
* The fields extracted for a tweet were: `text` of the tweet, Twitter's `tweet_id`, time `created_at`, number of `favourites`, number of `retweets`, Twitter's `user_id`, the user's public `user_name` and `user_screen_name`.
* Tweets containing images were detected using a regular expression, the URL of the image was thus extracted and added as an extra field to the data.

### Language Detection and Summary Statistics

**Although this is written in the past tense, this work will be conducted in the next day or so (when I get time), and so is likely to change depending on the properties of the data.**

* A python-ported version of [Google's language detection algorithm](https://github.com/Mimino666/langdetect) termed langdetect was used to classify tweets as being written in either Welsh (`CY`), English (`EN`), or unknown (`U` - to cover cases where language could not be detected within the defined probability range, or for tweets which were most likely in a language other than English or Welsh).
* The probability threshold was set at 95% confidence.
* The following measures were produced:

  * Mean number of tweets per day for: the whole period covered, the event itself, the week before the event and the week after.
  * Differences between the means were compared using the XXX (Chi Squared??) test with a confidence threshold of 0.95.
  * The percentage of tweets in English and Welsh for each event were compared and compared using the same method.
  * The mean number of retweets for a tweet in English and in Welsh were compared using the same method.


## Results

Coming soon to a repo near you...
