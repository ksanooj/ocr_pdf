import nltk
from nltk.tag.stanford import StanfordNERTagger

classifier1 = '/usr/share/stanford-ner/classifiers/english.conll.4class.distsim.crf.ser.gz'
classifier2 = '/usr/share/stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz'
jar = '/usr/share/stanford-ner/stanford-ner.jar'

st = StanfordNERTagger(classifier1, jar)
lt = StanfordNERTagger(classifier2, jar)


def organization_details(fp):
    with open(fp, 'r') as datafile:
        return datafile.read()


def process_with_nltk_ner():
    try:
        for item in organization_details('/home/qburst/Documents/Projects/python/ocr_pdf/project_data/extracted_text_files/BeverleyStrategicPlanningGroupLLCArticles-0.txt'):
            tokenized = nltk.word_tokenize(item)
            tagged = nltk.pos_tag(tokenized)
            # print tagged
            print(nltk.ne_chunk(tagged))

    except Exception as e:
        print str(e)


def process_with_stanford_ner():
    try:
        item = organization_details('/home/qburst/Documents/Projects/python/ocr_pdf/project_data/extracted_text_files/BeverleyStrategicPlanningGroupLLCArticles-0.txt')
        sentence = nltk.word_tokenize(item)
        tagged_list_1 = st.tag(sentence)
        entity_list = []
        # entity = []
        for item in tagged_list_1:
            if item[1] == 'ORGANIZATION':
                entity_list.append(item[0])

        # tagged_list_2 = lt.tag(entity_list)
        # for item in tagged_list_2:
        #     if item[1] == 'O':
        #         entity.append(item[0])

        business_name = " ".join(entity_list)
        print business_name
    except Exception as e:
        print str(e)

process_with_stanford_ner()
# process_with_nltk_ner()
