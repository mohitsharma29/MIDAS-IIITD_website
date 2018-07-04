---
layout: paper
title: "Aspect-Based Financial Sentiment Analysis using Deep Learning"
year: "2018"
shortref: 
nickname: 
journal: WWW '18 Companion Proceedings of the The Web Conference 2018
volume: 
issue: 
pages: 1961-1966
authors: "Hitkul Jangid, Shivangi Singhal, Rajiv Ratn Shah, Roger Zimmermann"
image: /assets/images/papers/WWW-aspect.jpg
pdf: 
pdflink: https://dl.acm.org/citation.cfm?id=3191827
github: https://github.com/Hitkul/Sentiment-analysis
pmid: 
pmcid: 
f1000: 
figshare: 
doi: 10.1145/3184558.3191827
category: paper
published: true
peerreview: true
review: false
tags: [ Aspect-based sentiment analysis, Deep learning, Convolutional Neural Networks, Recurrent neural networks, Bidirectional LSTM]
---
{% include JB/setup %}

# Abstract 

Aspect based sentiment analysis aims to detect an aspect (i.e. features) in a given text and then perform sentiment analysis of the text with respect to that aspect. This paper aims to give a solution for the FiQA 2018 challenge subtask 1. We perform aspect-based sentiment analysis on the microblogs and headlines of financial domain. We use a multi-channel convolutional neural network for sentiment analysis and a recurrent neural network with bidirectional long short-term memory units to extract aspect from a given headline or microblog. Our proposed model produces a weighted average F1 score of 0.69 for the aspect extraction task and predicts sentiment intensity scores with a mean squared error of 0.112 on 10-fold cross validation. We believe that the developed system has direct applications in the financial domain.