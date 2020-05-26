---
layout: paper
title: "Facefetch: An Efficient and Scalable Face Retrieval System That uses Your Visual Memory"
year: "2019"
shortref: 
nickname: 
journal: IEEE BigMM
volume: 
issue: 
pages: 338
authors: "Harsh Shrivastava, Rama Krishna P V N S, Karmanya Aggarwal, Meghna P Ayyar, Yifang
Yin, Rajiv Ratn Shah, Roger Zimmermann"
image: /assets/images/papers/default-paper.svg
pdf: 
pdflink: https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8919484
github: 
pmid: 
pmcid: 
f1000: 
figshare: 
doi: https://doi.org/10.1109/BigMM.2019.00014
category: paper
published: true
peerreview: false
review: false
tags: Face Retrieval, Relevance Feedback,Deep Convolutional Neural Network, Active Learning, UserInteraction
---

{% include JB/setup %}

# Abstract

Often in many situations in our life, we wish to envision the person we met but we could not recall what the person exactly look like except for a slight impression of the face. Yugo Sato et.al. introduced a face retrieval system for this problem, which utilises visual inputs from the users and attempts to retrieve the target face. The major drawback of their approach was that their system was slow and only applicable for small databases like Chicago Face Database. In this paper, we introduce a robust and scalable face retrieval system that is capable of retrieving the envisioned face from a large-scale database. Furthermore, instead of information specific to the target, our face retrieval system asks the user to select common face attributes that they remember their target face had, using which the system filters out the irrelevant faces thus speeding up the search process. Then our system asks the user to select several images that resemble with the envisioned face. On the basis of this selection, our system automatically reduces the "semantic gap" between human description and the computer based description of the target image. In order to evaluate our system, We conducted user studies on a large-scale database and established that our framework succeeded in beating the state of the art results in this particular task and thus proved itself to be very effective for retrieving the envisioned face image in approximately half the total number of search iterations and taking one-third of the overall search time thereby putting much less burden on the user.