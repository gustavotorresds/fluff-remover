# Fluff Remover

## Context
Many people struggle with cutting down text for an essay for a class, for a job application and for many other purposes. Writing concisely is hard. We want to create a model that, given a textual input, outputs a more concise version of that text. Our idea is to do a twist on the text summarization problem. The topic we are exploring is different from text summarization because it does not return the “main idea” of the input passage, but the concise version of it, keeping all its original ideas intact. We chose this problem due to its novelty and the potential impact it can have.

## Setup
You'll see that we reuse a lot of code written by other people (thanks all <3). We are including the repos inside this repo. For larger files (like datasets, we're including instructions for how/where to download get them).

### Part 1
Let's setup the basics.
* Make sure you're using Python 2.7
* Clone this repo
* `cd fluff-remover`
* Create a Virtual Environment (`python -m venv env`) and activate it (`source env/bin/activate`)
* `pip install -r requirements.txt`
* Download the Pretrained Model for TF 1.2.1, as instructed in the [Pointer Generator](https://github.com/abisee/pointer-generator). Rename the folder `pretrained_model` and place it inside `fluff-remover` (this repo)
* Download the dataset `finished_files`, also using the instructions in Pointer Generator (the only thing we'll use from there is `vocab`, so feel free to remove the rest). Place the folder inside `fluff-remover`

### Part 2
We need to setup some packages for out scripts to run.
* Follow the instructions [here](https://github.com/dondon2475848/make_datafiles_for_pgn) to install the packages that make the file conversion (from .txt to .bin, which is what Pointer Generator consumes). TL;DR: stanford-corenlp-3.9.2.jar from [StanfordCoreNLP](https://stanfordnlp.github.io/CoreNLP/) (make sure you're downloading the mainCoreNLP and not one specific to a language); then run `export CLASSPATH=$HOME/Downloads/stanford-corenlp-full-2018-10-05/stanford-corenlp-3.9.2.jar` (or include this in your .bash_profile if you don't wanna run this command every time you work on this); test if it's working usign `echo "Please tokenize this text." | java edu.stanford.nlp.process.PTBTokenizer`. Note: you'll also need `java` installed on your computer, which you might already have; if not, go install it.
* We'll also need ROUGE. Follow instructions [here](https://pypi.org/project/pyrouge/). If you get lucky, running `pip install pyrouge` will be enough. I had to follow the instructions on this website. To save you some time, ROUGE-1.5.5 (which you'll need) can be found in [this repo](https://github.com/andersjo/pyrouge). Clone it and use `<wherever you clone this repo>/pyrouge/tools/ROUGE-1.5.5` as `/absolute/path/to/ROUGE-1.5.5/directory` (you'll understand when reading the instructions in the link mentioned above).

### Part 3
Let's get our dataset.
* Download it from [here](https://drive.google.com/drive/u/1/folders/19wIq4xqcoFnBJQMjGpGJ8r_Flv1KMSoQ) and place it in `fluf-remover`.
* TODO: we need to format it in a way that makes it easy for the scripts to consume the files.

## Scripts
You can find more information about what our scripts do in their respective docs :)
