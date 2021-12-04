import sys
import lightrdf

ONTOLOGY_FILE = 'ontology.owl'

if __name__ == '__main__':
    with open(ONTOLOGY_FILE, "rb") as file_in:
        word = str(input("\nPlease enter the word to be searched in the ontology: "))

        if " " in word:
            print("Invalid number of arguments! Expected one, the word to be searched in the ontology!")
            exit(1)

        doc = lightrdf.RDFDocument(file_in, parser=lightrdf.xml.PatternParser, base_iri=None)

        ok = 0
        for triple in doc.search_triples(None, None, None):
            if triple[2].endswith("/" + word) and triple[1].endswith("/cso#superTopicOf"):
                print(triple, triple[2].split("/")[-1])
                ok = 1
            elif triple[2].endswith("#" + word) and triple[1].endswith("/cso#superTopicOf"):
                print(triple, triple[2].split("#")[-1])
                ok = 1

        if ok == 0:
            print("The word wasn't found !")
