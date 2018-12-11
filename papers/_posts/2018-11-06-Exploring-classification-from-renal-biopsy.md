---
layout: paper
title: "Exploring Classification of Histological Disease Bio-markers from Renal Biopsy Images"
year: "2019"
shortref: 
nickname: 
journal: WACV
volume: 
issue: 
pages:
authors: "Megha Ayyar, Puneet Mathur, Rajiv Ratn Shah, Shree Gopal Sharma"
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

Identification of diseased kidney glomeruli and fibrotic regions, the two most significant biomarkers for chronic kidney diseases, remains subjective and time-consuming due to complete dependence on an expert kidney pathologist. In an attempt to automate the identification of tissue-level micro-structures from biopsy images, we investigate three deep learning techniques: traditional transfer learning, pre-trained deep neural networks for feature extraction followed by supervised classification and a novel Multi-Gaze Attention Network (MGANet) that uses multi-headed self-attention through parallel residual skip connections in a CNN architecture. We simultaneously introduce a Renal Glomeruli Fibrosis Histopathological (RGFH) database
pertaining to 935 glomeruli and 927 fibrosis images. As per our experimentation, transfer learning models such as ResNet50, InceptionResNetV2,VGG19 and InceptionV3 are
empirically proven to under-perform for classification of glomeruli into normal and abnormal morphology and classification of fibrosis patches into mild, moderate and severe categories. On the other hand, the Logistic Regression model augmented with features extracted from the InceptionResNetV2 shows promising results. Additionally, the experiments effectively ascertain that the proposed MGANet architecture outperforms both the baseline techniques to establish the state of the art accuracy of 87.25% and 81.47% for glomerluli and fibrosis classification respectively.