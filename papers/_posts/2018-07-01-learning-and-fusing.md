---
layout: paper
title: "Learning and Fusing Multimodal Deep Features for Acoustic Scene Categorization"
year: "2018"
shortref: 
nickname: 
journal: ACM Multimedia
volume: 
issue: 
pages:
authors: "Yifang Yin, Rajiv Ratn Shah, Roger Zimmerman"
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
peerreview: true
review: false
tags: 
---
{% include JB/setup %}

# Abstract 

Convolutional Neural Networks (CNNs) have been widely applied to audio classification recently where promising results have been obtained. Previous CNN-based systems mostly learn from two-dimensional time-frequency representations such as MFCC and spectrogram, which may tend to emphasize more on the background noise of the scene. To learn the key acoustic events, we introduce a three-dimensional CNN to emphasize on the different spectral characteristics from neighboring regions in spatial-temporal domain. A novel acoustic scene classification system based on multimodal deep fusion has been proposed in this paper, where three CNNs have been presented to perform 1D raw waveform modeling, 2D time-frequency image modeling, and 3D spatial-temporal dynamics modeling, respectively. The learnt features have been shown to be highly complementary to each other, leading to significant classification improvements based on feature fusion. A new double fusion scheme, which takes advantages of both early fusion and late fusion, is proposed to further boost the system’s performance. Comprehensive experiments have been conducted on the DCASE16 dataset for acoustic scene classification. Experimental results demonstrate the effectiveness of our proposed approach, as our solution achieves the state-of-the-art classification rates and improves the mean accuracy by 2.3% ∼ 9.2% compared to the top ranked systems in the DCASE16 challenge.