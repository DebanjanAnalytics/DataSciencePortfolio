# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 12:18:26 2021

@author: Deb
"""

import re
import nltk

from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

from nltk.stem import WordNetLemmatizer

para = """Sourav Ganguly Known as the Bengal Tiger of the Indian cricket team, Sourav Ganguly is arguably one of the most successful captains ever in the history of Indian cricket., and one of the greatest ODI batsmen of all time.

His aggressive form of leadership heralded a new era in Indian cricket and helped the team secure many memorable wins at home and overseas in the early 2000s

Some of the milestones set by this cricketer include 22 ODI centuries and as many as 20 century opening-partnerships with Sachin Tendulkar. Sourav Ganguly is the third player to score 10,000 ODI runs and second-fastest after Sachin Tendulkar. Ganguly was also awarded with Padma Shri in 2004 for his magnanimous contribution to the world of cricket. 

Currently, Sourav is the President of the Cricket Association of Bengal and President of the Editorial Board with Wisden India. Sourav Ganguly is also one of the four members of the Indian Premier League's Governing Council, responsible for all the functions of the tournament. 

Sourav Ganguly, the man who fought all odds , is an epitome of guts and glory resulted in appearing as the finest batsman and captain of Indian cricket team. Today as India climbs to its new heights as an international cricket team, one cannot but be in awe of the amazing work which Sourav put in to make its foundations being a great mentor who identified and gave talent the opportunity to flourish. Being a very influential figure in Indian cricket history he is the person who changed the perception of Indian cricket and cricketers abroad. His hunger to achieve success and passion for the game of cricket is truly an inspiring tale. 

Sourav Ganguly's life is the story of a man who faced several struggles, betrayals and setbacks on his way to sporting greatness. Many credit him for turning relatively inexperienced players into a match-winning unit.

He says he followed a simple formula for success: 

"I picked talented players from all parts of the country. And I backed them and gave them enough space. The main thing was taking the fear of failure and insecurity away from them," he says.

Sourav Ganguly’s story is a message of perseverance for all. Sourav Ganguly will forever rank as one of Indian cricket’s best leaders. Even more a leader of men than just a player, he is rightly credited for having changed the mindset of the Indian cricket team at the turn of the century. Ganguly injected positivity and taught the art of competing and even winning, his single-biggest contribution to Indian cricket. At the root of this transformation was his mindset. Not to give up in the face of adversity.

As a Motivational Speaker Sourav ​gives us a detailed insight into this never-say-die mindset."""


sentences = nltk.sent_tokenize(para)
stemmer = PorterStemmer()

for i in range(len(sentences)):
    words=nltk.word_tokenize(sentences[i])
    words=[stemmer.stem(word) for word in words if not word in set(stopwords.words('english'))]
    sentences[i]=' '.join(words)

lemmtizer = WordNetLemmatizer()
sentences_lemm = nltk.sent_tokenize(para)

for i in range(len(sentences)):
    words_lemm=nltk.word_tokenize(sentences[i])
    words_lemm=[lemmtizer.lemmatize(word) for word in words_lemm if not word in set(stopwords.words('english'))]
    sentences_lemm[i]=' '.join(words_lemm)
