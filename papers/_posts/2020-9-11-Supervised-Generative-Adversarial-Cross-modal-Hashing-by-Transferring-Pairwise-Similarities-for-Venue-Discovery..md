---
layout: paper
title: "Supervised Generative Adversarial Cross-modal Hashing by Transferring Pairwise Similarities for Venue Discovery."
year: "2020"
shortref: 
nickname: 
journal: IEEE BigMM
volume: 
issue: 
pages: 321
authors: "Himanshu Aggarwal, Rajiv Ratn Shah, Suhua Tang, Feida Zhu"
image: /assets/images/papers/default-paper.svg
pdf: 
pdflink: https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8919431
github: 
pmid: 
pmcid: 
f1000: 
figshare: 
doi: https://doi.org/10.1109/BigMM.2019.000-2
category: paper
published: true
peerreview: false
review: false
tags: Cross-modal retrieval; Hashing;Generative  Adversarial  Network
---

{% include JB/setup %}

# Abstract

Venue discovery using real-world multimedia data has not been investigated thoroughly. We are referring to business and travel locations as venues in this study and aim to improve the efficiency of venue discovery by hashing. Most existing supervised cross-modal hashing methods map data in different modalities to Hamming space, where the semantic information is exploited to supervise data of different modalities during the training stage. However, previous works neglect pairwise similarity between data in different modalities, which lead to degraded performance of hashing function learning. To address this issue, we propose a supervised Generative Adversarial Cross-modal Hashing method by Transferring Pairwise Similarities (SGACH-TPS). This work has three significant contributions: i) we propose a model for making efficient venue discovery, ii) the supervised generative adversarial network can construct a hash function to map multimodal data to a common hamming space. iii) a simple transfer training strategy for the adversarial network is suggested to supervise data in different modalities where the pairwise similarity is transferred to the fine-tuning stage of training. Evaluation on the new WikiVenue dataset confirms the superiority of the proposed method.