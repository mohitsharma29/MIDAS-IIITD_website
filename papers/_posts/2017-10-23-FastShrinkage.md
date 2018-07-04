---
layout: paper
title: "FastShrinkage: Perceptually-aware Retargeting Toward Mobile Platforms"
year: "2017"
shortref: 
nickname: FastShrinkage
journal: ACM Multimedia Conference, United States, October 23-27
volume: 
issue: 
pages: 501-509
authors: "Zhenguang Liu, Zepeng Wang, Luming Zhang, Rajiv Ratn Shah, Yingjie Xia, Yi Yang, and Xuelong Li"
image: /assets/images/papers/default-paper.svg
pdf: 
pdflink: https://ink.library.smu.edu.sg/cgi/viewcontent.cgi?referer=https://www.google.co.in/&httpsredir=1&article=4876&context=sis_research
github: 
pmid: 
pmcid: 
f1000: 
figshare: 
doi: 10.1145/3123266.3123377
category: paper
published: true
peerreview: true
review: false
tags: [Deep feature, Mobile platform, Perceptual, Probabilistic model, Retarget]
---
{% include JB/setup %}

# Abstract 

Retargeting aims at adapting an original high-resolution photo/video to a low-resolution screen with an arbitrary aspect ratio. Conventional approaches are generally based on desktop PCs, since the computation might be intolerable for mobile platforms (especially when retargeting videos). Besides, only low-level visual features are exploited typically, whereas human visual perception is not well encoded. In this paper, we propose a novel retargeting framework which fast shrinks photo/video by leveraging human gaze behavior. Specifically, we first derive a geometry-preserved graph ranking algorithm, which efficiently selects a few salient object patches to mimic human gaze shifting path (GSP) when viewing each scenery. Afterward, an aggregation-based CNN is developed to hierarchically learn the deep representation for each GSP. Based on this, a probabilistic model is developed to learn the priors of the training photos which are marked as aesthetically-pleasing by professional photographers. We utilize the learned priors to efficiently shrink the corresponding GSP of a retargeted photo/video to be maximally similar to those from the training photos. Extensive experiments have demonstrated that: 1) our method consumes less than 35ms to retarget a 1024 × 768 photo (or a 1280 × 720 video frame) on popular iOS/Android devices, which is orders of magnitude faster than the conventional retargeting algorithms; 2) the retargeted photos/videos produced by our method outperform its competitors significantly based on the paired-comparison-based user study; and 3) the learned GSPs are highly indicative of human visual attention according to the human eye tracking experiments.