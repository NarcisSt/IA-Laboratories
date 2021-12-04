import nltk
import lightrdf

TEXT_FILE = 'computer-science.txt'
CREATED_FILE = 'created-file.txt'
ONTOLOGY_FILE = 'ontology.owl'
ONTOLOGY_CHECK_FILE = 'ontology-check-file'


def check_for_ontology(phrase):
    words_list = nltk.word_tokenize(phrase)
    if check_if_is_compatible(phrase):
        with open(ONTOLOGY_FILE, "rb") as file_in:
            doc = lightrdf.RDFDocument(file_in, parser=lightrdf.xml.PatternParser, base_iri=None)

            for word in words_list:
                for triple in doc.search_triples(None, None, None):
                    if triple[2].endswith("/" + word):
                        return True
                    elif triple[2].endswith("#" + word):
                        return True

    return False


def check_if_is_compatible(phrase):
    words_list = nltk.word_tokenize(phrase)
    pos_map = nltk.pos_tag(words_list)
    i = 0
    j = 0
    k = 0
    ok1 = False
    ok2 = False
    ok3 = False
    for pos in pos_map:
        if ("NN" in pos[1]) and ok1 == False:
            ok1 = True
            i += 1
            break
        else:
            i += 1

    for j in range(i, len(pos_map)):
        if ("VB" in pos_map[j][1]) and ok2 == False and ok1 == True:
            ok2 = True
            j += 1
            break
        else:
            j += 1

    for K in range(j, len(pos_map)):
        if ("NN" in pos_map[k][1]) and ok3 == False and ok2 == True and ok1 == True:
            ok3 = True
            k += 1
            break
        else:
            k += 1

    return ok1 and ok2 and ok3


if __name__ == '__main__':
    # with open(TEXT_FILE, "r", encoding="mbcs") as in_file:
    #     text = in_file.read()
    #     sentences = nltk.sent_tokenize(text)
    #
    # created_file = open(CREATED_FILE, "w", encoding="mbcs")
    # for sentence in sentences:
    #     if check_if_is_compatible(sentence):
    #         created_file.write(sentence)
    #         created_file.write('\n')

    with open(CREATED_FILE, "r", encoding="mbcs") as in_file:
        text = in_file.read()
        sentences = nltk.sent_tokenize(text)

    ontology_check_file = open(ONTOLOGY_CHECK_FILE, "w", encoding="mbcs")
    for sentence in sentences:
        if check_for_ontology(sentence):
            ontology_check_file.write(sentence)
            ontology_check_file.write('\n')
