# Austalk

2391 rows of data

3 classes: hins, hine, hinge

AusTalk is a large state-of-the-art database of modern spoken Australian English from all around the country. Recorded between June 2011 and June 2016, the final database contains full audio-visual data for 861 adult speakers (with age ranging from 18 to 83) from 15 different locations in all Australian states & territories, representing the regional and social diversity and linguistic variation of Australian English, including Australian Aboriginal English. Each speaker was recorded for one hour on three separate occasions to sample their voice in a range of scripted and spontaneous speech situations at various times (see **About AusTalk** for a more detailed description of the data collection protocol). 

In this project, we selected recording of 3 words: hin, hine and  from 428 speakers

## Files

austalk.py - the code for downloading austalk data from a open database, Aleveo. The code will also down sample the audio, convert audio into numerical value and combine all of them into a single file for deep learning.

tsc.py - the code for fixing the length difference of the data set

