import json
from tqdm import tqdm
import sys

class TitleAndAbstract():

    def __init__(self, file_path, json_file_name, save_file_path):

        self.file_path = file_path
        self.json_file_name = json_file_name
        self.save_file_path = save_file_path
        f = open(file_path + json_file_name, 'r')
        self.data = json.load(f)
        f.close()
        self.number_of_documents = 0

    def get_title_abstracts_file(self):

        with open(self.save_file_path + 'title_and_abstract_documents.txt', 'wb') as f:
            for key, value in tqdm(self.data["train"]["papers"].items()):
                self.number_of_documents += 1
                title = value["title"]
                abstract = value["abstract"]
                # title = title.decode("utf-8")
                # abstract = abstract.decode("utf-8")
                text = title + ' ' + abstract
                f.write(text.encode('utf-8'))
                f.write('\n'.encode('utf-8'))
            f.close()

    def get_class(self):

        with open(self.save_file_path + 'title_and_abstract_class.txt', 'w') as f:
            for i in tqdm(range(self.number_of_documents)):
                f.write('0')
                f.write('\n')
            f.close()

def main():

    FILEPATH = 'E:/Document Similarity of Electronic Manuals/'
    JSON_FILE_NAME = 'papers_titles_and_abstracts.json'
    SAVE_FILEPATH = 'E:/Document Similarity of Electronic Manuals/HTM/cluhtm/titles_and_abstracts/'

    title_and_abstracts = TitleAndAbstract(FILEPATH, JSON_FILE_NAME, SAVE_FILEPATH)
    title_and_abstracts.get_title_abstracts_file()
    title_and_abstracts.get_class()

if __name__ =='__main__':
    main()
