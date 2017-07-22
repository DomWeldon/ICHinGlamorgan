"""Quick script to classify as either Welsh or English or unknown."""
from collections import namedtuple
import pandas as pd
from pathlib import Path
from termcolor import colored
import langdetect

# config
cols = namedtuple(
    'ColourConfig',
    'info success warning error')(
    'cyan',
    'green',
    'yellow',
    'magenta')
p_value = 0.95

# set seed at 0
langdetect.DetectorFactory.seed = 0

# do it iteratively for all csv files
p = Path('./data')

for f in p.glob('*.csv'):
    results, confidences = [], []
    df = pd.read_csv(f)
    print(
        'Opening',
        colored(str(f), cols.info),
        'containing',
        colored(str(len(df)), cols.info),
        'tweets')
    for t in df['text']:
        try:
            # detect the language
            langs = langdetect.detect_langs(t)
            print(
                'Detecting tweet:',
                colored(str(t), cols.info),
                'as',
                colored(langs, cols.success)
            )
        except (TypeError, langdetect.lang_detect_exception.LangDetectException):
            # or dont
            print(
                colored('Failed to detect for tweet', cols.error),
                colored(str(t), cols.warning)
            )
            results.append('unknown')
            confidences.append('')
        else:
            # can we work out a confidence level?
            # do we have one and only one language with p >= p_valie?
            r = [l for l in langs if l.prob > p_value]
            if len(r) == 1:
                # yes
                results.append(r[0].lang)
            else:
                # no
                results.append('unknown')
            confidences.append(';'.join([str(l) for l in langs]))
            del langs

    # put back into the data frame
    df['detected_language'] = pd.Series(results)
    df['language_confidences'] = pd.Series(confidences)
    df.to_csv('data/'+'detected_'+f.name)
