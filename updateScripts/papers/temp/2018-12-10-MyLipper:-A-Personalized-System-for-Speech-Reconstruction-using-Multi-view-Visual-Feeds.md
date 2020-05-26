---
layout: paper
title: "MyLipper: A Personalized System for Speech Reconstruction using Multi-view Visual Feeds"
year: "2018"
shortref: 
nickname: 
journal: IEEE International Symposium on Multimedia (ISM)
volume: 
issue: 
pages: 159
authors: "Yaman Kumar, Rohit Jain, Mohd Salik, Rajiv Ratn Shah, Roger Zimmermann, Yifang
Yin"
image: /assets/images/papers/default-paper.svg
pdf: 
pdflink: https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8603277
github: 
pmid: 
pmcid: 
f1000: 
figshare: 
doi: https://doi.org/10.1109/ISM.2018.00-19
category: paper
published: true
peerreview: false
review: false
tags: Multi-layer neural network, Signal reconstruc-tion, Speech synthesis, Linear predictive coding
---

{% include JB/setup %}

# Abstract

Lipreading is the task of looking at, perceiving, and interpreting spoken symbols. It has a wide range of applications such as in surveillance, Internet telephony, speech reconstruction for silent movies and as an aid to a person with speech as well as hearing impairments. However, most of the work in lipreading literature has been limited to the classification of speech videos into text classes formed of phrases, words and sentences. Even this has been based on a highly constrained lexicon of words which, then subsequently translates to restriction on total number of classes (i.e, phrases, words and sentences) that are considered for the classification task. Recently, research has ventured into generating speech (audio) from silent video sequences. In spite of non-frontal views showing the potential of enhancing performance of speech reading and reconstruction systems, there have been no developments in using multiple camera feeds for the same. To this end, this paper presents a multi-view speech reading and reconstruction system. The major contribution of this paper is to present a model, namely MyLipper, which is a vocabulary and language agnostic and a real-time model that deals with a variety of poses of a speaker. The model leverages silent video feeds from multiple cameras recording a subject to generate intelligent speech for that speaker, thus being a personalized speech reconstruction model. It uses deep learning based STCNN+BiGRU architecture to achieve this goal. The results obtained using MyLipper show an improvement of over 20% in reconstructed speech's intelligibility (as measured by PESQ) using multiple views as compared to a single view visual feed. This confirms the importance of exploiting multiple views in building an efficient speech reconstruction system. The paper further shows the optimal placement of cameras which would lead to the maximum intelligibility of speech. Further, we demonstrate the reconstructed audios overlaid on the corresponding videos obtained from MyLipper using a variety of videos from the dataset.