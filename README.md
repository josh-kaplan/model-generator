# Model Generator 

Model Generator is a Python module for generating arbitrary and random model
data for testing. Model elements have a randomly generated UUID and a name where 
the name is just two random words from the [word list](data/wordlist_1000.txt).

Names are guaranteed to be unique. This may change in the future, but the intent
is to generate a complex model consisting of relatively simple elements.

Elements can be of type *Block*, *Link*, *Package*, or *Model* and are defined
as follows:

- Element: A base class that all other elements extend.
- Block: This simplest extension of Element, it adds no fields.
- Link: Adds *source* and *target* fields to the base class. Used to link to 
  other elements together and represent relationships.
- Package: Adds a *contains* field. Used to store other elements and define the
  model tree.
- Model: A special type of package, it is the top-most package with no parent.


To run the generator, run `python -m src <H> <W>` from the project root 
directory. Where `<H>` is the maximum height of the tree and `<W>` is the width.
Width is the number of children under each package which are each randomly 
chosen to be either a *block*, *link*, or *package*. 


## Sources 

- [data/wordlist_1000.txt](data/wordlist_1000.txt) [https://gist.github.com/deekayen/4148741](https://gist.github.com/deekayen/4148741)