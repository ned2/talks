#!/usr/bin/env python


import math
from collections import Counter
from pathlib import Path
from glob import glob
from itertools import chain

import spacy
from jinja2 import Environment, FileSystemLoader


nlp = spacy.load("en_core_web_sm")


class Doc:

    
    def __init__(self, text, corpus=None, identifier=None):
        self.text = text
        self.corpus = corpus
        self.id = identifier
        self.cleaned_text = self.clean(self.text)
        self.tokens = Counter(self.cleaned_text.split())
        
    def clean(self, text):
        doc = nlp(text, disable=['parser', 'ner'])
        return ' '.join(
            token.lemma_.lower()
            for token in doc
            if not (token.is_stop or token.is_punct or token.is_space)
        )

    def vector(self, tfidf=False):
        """Return a vector representation for this document"""
        if self.corpus is None:
            return None

        if tfidf:
            # weight the counts with TF-IDf weighting
            return [
                self.tokens[token]*self.corpus.idf(token)
                for token in self.corpus.vocab
            ]
        else:
            return [self.tokens[token] for token in self.corpus.vocab]

    def __str__(self):
        return f"Document {self.id}"

    def __repr__(self):
        return f"<{Doc:self.id}>"

class Corpus:

    def __init__(self, texts):
        self.docs = [
            Doc(text, identifier=i+1, corpus=self)
            for i, text in enumerate(texts)
        ]
        self.vocab = set(
            chain.from_iterable(
                doc.tokens
                for doc in self.docs
            )
        )
        self.doc_freqs = Counter(
            chain.from_iterable(
                doc.tokens for
                doc in self.docs
            )
        )
        
    def idf(self, token, roundto=2):
        """Get the inverse document frequency of a token in this corpus."""
        return round(math.log(len(self) / self.doc_freqs[token] + 1), 2)

    def __len__(self):
        return len(self.docs)
    
    def __iter__(self):
        return iter(self.docs)
    
    def __getitem__(self, index):
        return self.docs[index]

    
def make_slides():
    path = Path(".")/"templates"
    env = Environment(loader=FileSystemLoader(str(path)))

    docs = [
        """The cat sat on the mat.""",
        """A kitten lies on the rug.""",
        """Monkeys live in the trees.""",
    ]

    corpus = Corpus(docs)
    template = env.get_template("slides.html")
    html = template.render(corpus=corpus)
    return html


if __name__ == "__main__":
    print(make_slides())

# page1
# -- doc1 printed
# -- doc1 cleaned
# -- doc1 vectorised in a table

# page4 -- 
    
