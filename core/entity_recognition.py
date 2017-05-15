import nltk
import ner
import enchant
import os
# from nltk.tag.stanford import StanfordNERTagger
from nltk.metrics import edit_distance


class SpellingReplacer(object):

    def __init__(self, dict_name='en_US', max_dist = 2):
        self.spell_dict = enchant.Dict(dict_name)
        self.max_dist = 2

    def replace(self, word):
        if self.spell_dict.check(word):
            return word
        suggestions = self.spell_dict.suggest(word)

        if suggestions and edit_distance(word, suggestions[0]) <= self.max_dist:
            return suggestions[0]
        else:
            return word


def spell_check(word_list):
    checked_list = []
    for item in word_list:
        replacer = SpellingReplacer()
        r = replacer.replace(item)
        checked_list.append(r)
    return checked_list

# classifier1 = '/usr/share/stanford-ner/classifiers/english.conll.4class.distsim.crf.ser.gz'
# classifier2 = '/usr/share/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz'
# jar = '/usr/share/stanford-ner/stanford-ner.jar'

# st = StanfordNERTagger(classifier1, jar)
# lt = StanfordNERTagger(classifier2, jar)

with open(os.environ['ENTITY_BLACK_LIST'], 'r') as excluded:
    entity_black_list = excluded.read().decode("utf-8")


def organization_details(fp):
    with open(fp, 'r') as datafile:
        return datafile.read().decode("utf-8")


def process_with_nltk_ner(fp):
    try:
        for item in organization_details(fp):
            tokenized = nltk.word_tokenize(item)
            tagged = nltk.pos_tag(tokenized)
            # print tagged
            print(nltk.ne_chunk(tagged))

    except Exception as e:
        print str(e)


# def process_with_stanford_ner(fp):
#     try:
#         item = organization_details(fp)
#         sentence = nltk.word_tokenize(item)
#         tagged_list_1 = st.tag(sentence)
#         entity_list = []
#         # entity = []
#         tagger = ner.SocketNER(host='localhost', port=8090)
#         entities = tagger.get_entities(item)['ORGANIZATION']
#         print entities
#         for item in tagged_list_1:
#             if item[1] == 'ORGANIZATION':
#                 entity_list.append(item[0])
#
#         # tagged_list_2 = lt.tag(entity_list)
#         # for item in tagged_list_2:
#         #     if item[1] == 'O':
#         #         entity.append(item[0])
#
#         business_name = pp.parse(" ".join(entity_list))
#         print business_name
#     except Exception as e:
#         print str(e)

def process_with_stanford_ner(pages):
    # try:
        entity_list = []
        tagger = ner.SocketNER(host='localhost', port=8090)
        for page in pages:
            # words = nltk.word_tokenize(page)
            # page = spell_check(words)
            entities = tagger.get_entities(page).get('ORGANIZATION')
            if entities:
                for entity in entities:
                    if entity not in entity_black_list:
                        entity_list.append(entities)
        return entity_list
    # except Exception as e:
    #     print str(e)

if __name__ == '__main__':
    from core.utils import data_file_names
    from core import PDF_DIR
    process_with_stanford_ner(data_file_names(PDF_DIR))
    # process_with_nltk_ner()
