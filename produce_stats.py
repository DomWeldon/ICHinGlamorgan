from collections import namedtuple
import pandas as pd
from pathlib import Path
from termcolor import colored

# config
cols = namedtuple(
    'ColourConfig',
    'info success warning error')(
    'cyan',
    'green',
    'yellow',
    'magenta')
p_value = 0.95

for f in Path('data/').glob('detected_*.csv'):
    df = pd.read_csv(f)
    print(
        colored(f.name, cols.info),
        colored(str({ l: len(df[df['detected_language'] == l]) for l in ['cy', 'en', 'unknown'] }), cols.success)
    )
