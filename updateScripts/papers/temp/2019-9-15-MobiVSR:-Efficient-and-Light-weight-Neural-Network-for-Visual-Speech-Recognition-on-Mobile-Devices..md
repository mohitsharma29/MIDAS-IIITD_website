---
layout: paper
title: "MobiVSR: Efficient and Light-weight Neural Network for Visual Speech Recognition on Mobile Devices."
year: "2019"
shortref: 
nickname: 
journal: Interspeech, 2019
volume: 
issue: 
pages: 
authors: "Nilay Shrivastava, Astitwa Saxena, Yaman Singla, Rajiv Ratn Shah, Amanda, Debanjan
Mahata, Preeti Kaur, Roger Zimmermann,"
image: /assets/images/papers/default-paper.svg
pdf: 
pdflink: 
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

Visual speech recognition (VSR) is the task of recognizing spo-ken language from video input only, without any audio. VSRhas many applications as an assistive technology, especially ifit could be deployed in mobile devices and embedded systems.The need for intensive computational resources and large mem-ory footprint are two major obstacles in deploying neural net-work models for VSR in a resource constrained environment.We propose a novel end-to-end deep neural network architec-ture for word level VSR called MobiVSR with a design param-eter that aids in balancing the model’s accuracy and parametercount. We use depthwise 3D convolution along with channelshufﬂing for the ﬁrst time in the domain of VSR and show howit makes our model efﬁcient. MobiVSR achieves an accuracyof 70% on a challenging Lip Reading in the Wild dataset with6 times fewer parameters and 20 times smaller memory foot-print than the current state of the art. MobiVSR can also becompressed to 6 MB by applying post training quantization.Index Terms: video speech recognition,