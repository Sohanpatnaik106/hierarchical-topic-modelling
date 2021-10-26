# Hierarchical-Topic-Modelling

1. Clone the repository
2. Download wiki-news-300d-1M.vec and place it inside the cluhtm directory
3. In order to generate the text data, run the file generate_title_abstract.py inside cluhtm directory by specifying respective path to the json file.
4. To get the topics, run the main.py file as python ./cluhtm/main.py -d titles_and_abstracts from the main directory which contained the cloned cluhtm directory.
5. A directory with the heirarchical topics will be created. Experiments can be done by varying the depth of the heirarchy inside the function generate_topics in script_functions.py file.
