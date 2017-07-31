# Intangible Cultural Heritage in the Historic County of Glamorgan: Twitter Analysis

Real quick script to scrape some data from twitter for various hash tags, then perform some language analysis on it. Details are provided below.

## Authors

This work was conducted by Dom Weldon<sup>1</sup> and Amy Dolben<sup>2</sup>.

1. Department of Digital Humanities, King's College London: dominic.weldon@kcl.ac.uk.
2. Department of Archaeology, University of Cambridge: ad696@cam.ac.uk.

## Attribution

* AD designed the research and data to be collected.
* DW was responsible solely for the technical work to extract the data and the code to combine it with Google's language detection algorithm to produce results (as CSV files), which were then passed to AD for qualitative analysis.
* DW used `pandas` to provide a summary count of the number of tweets in each language which were passed to AD alongside raw CSV files, which AD used to perform further qualitative and quantitative analysis.

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

### Language Detection and Summary Statistics

* A python-ported version of [Google's language detection algorithm](https://github.com/Mimino666/langdetect) termed `langdetect` was used to classify tweets according to the language they were written in. The `langdetect` algorithm calculated a set of probabilities that any given tweet was written in a particular language. DW's program, `lang_detect.py` then classified a tweet as being written in that language only if:

  * a) the tweet was assigned a probability of over 0.95 for being written in that language
  * b) the tweet was not assigned a probability of over 0.95 for being written in any other language

  tweets which could not be classified into any language within the defined probability range were classified as `unknown`.

## Results

The total number of tweets in each language for each term is recorded below as a python dictionary.

These results suggest that some outlier tweets may be erroneously assigned to another language by the detection algorithm (e.g., the tweet "@CylchgrawnGolwg @ARGRPH @Tafwyl Nice joke lads" is not in Hungarian, no matter how much the unusual combination of words and letters in the twitter handles may make it appear so). Such outliers can be further assessed by AD.

    total_tweets = {
      'tafwyl': {
          'pt': 4,
          'vi': 4,
          'af': 2,
          'ca': 1,
          'da': 3,
          'hr': 1,
          'so': 2,
          'hu': 2,
          'fi': 1,
          'unknown': 720,
          'it': 3,
          'en': 1407,
          'de': 3,
          'cy': 2838,
          'sw': 3,
          'pl': 2,
          'nl': 1,
          'sv': 1,
          'fr': 3
      },
      'urd2017': {
          'unknown': 670,
          'cy': 3407,
          'en': 812
       },
    }
