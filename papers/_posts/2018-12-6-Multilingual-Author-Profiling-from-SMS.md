---
layout: paper
title: "Multilingual Author Profiling from SMS"
year: "2018"
shortref: 
nickname: 
journal: FIRE 2018 challenge
volume: 
issue: 
pages: 
authors: "Deepanshu Gaur, Meghna Ayyar, Ashutosh Kumar Singh, Rajiv Ratn Shah"
image: /assets/images/papers/default-paper.svg
pdf: 
pdflink: http://ceur-ws.org/Vol-2266/T4-8.pdf
github: 
pmid: 
pmcid: 
f1000: 
figshare: 
doi: 
category: paper
published: true
peerreview: false
review: false
tags: 
---

{% include JB/setup %}

# Abstract

This paper presents our solution for the Author Profiling task in the FIRE challenge 2018. This task mainly focuses on finding the age and gender of people from South Asian countries such as India, Pakistan, Nepal, and Bangladesh from their short messaging services (SMS). Since most of these people use a combination of languages such as Hindi, English and Roman Urdu (i.e., multilingual text) on social media platforms such as WhatsApp, Facebook, and Twitter, they also follow the same practice in SMS while communicating. Thus, we aim to perform author profiling by identifying gender and age of people by analyzing their multilingual SMS. In this paper, we classify the gender of a person into male or female categories. Moreover, we classify age into the following
three age groups: (i) 15-19, (ii) 20-24, and (iii) above 25. After preprocessing steps including tokenization and normalization, we provide the results of an experiment with several machine learning models like SVM, Random Forest, and Naive Bayes. Experimental results show that Naive Bayes provides competitive results when used with bilingual dictionary for translation and count vectorizer for feature extraction.