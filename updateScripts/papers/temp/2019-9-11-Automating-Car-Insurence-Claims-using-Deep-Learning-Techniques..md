---
layout: paper
title: "Automating Car Insurence Claims using Deep Learning Techniques."
year: "2019"
shortref: 
nickname: 
journal: 2019 IEEE Fifth International Conference on Multimedia Big Data (BigMM)
volume: 
issue: 
pages: 
authors: "Ranjodh Singh, Meghna P Ayyar, Tata Sri Pavan, Sandeep Gosain and Rajiv Ratn Shah"
image: /assets/images/papers/default-paper.svg
pdf: 
pdflink: https://ieeexplore.ieee.org/document/8919258
github: 
pmid: 
pmcid: 
f1000: 
figshare: 
doi: https://ieeexplore.ieee.org/document/8919258
category: paper
published: true
peerreview: false
review: false
tags: 
---

{% include JB/setup %}

# Abstract

With the number of people driving a car increasing every day, there has been a proliferation in the number of cars insurance claims being registered. The life cycle of registering, processing and making a decision for each claim involves the manual examination by the service engineer who creates the damage report followed by the physical inspection by a surveyor from the insurance company which makes it a long drawn out process. We propose an end to end system to automate this process, which would be beneficial for both the company and the customer. This system takes images of the damaged car as input and gives relevant information like the damaged parts and provides an estimate of the extent of damage (no damage, mild or severe) to each part. This serves as a cue to then estimate the cost of repair which would be used in deciding insurance claim amount. We have experimented with popular instance segmentation models like the Mask R-CNN, PANet and an ensemble of these two along with a transfer learning [1] based VGG16 network to perform different tasks of localizing and detecting various classes of parts and damages found in the car. Additionally, the proposed system achieves good mAP scores for parts localization and damage localization (0.38 and 0.40 respectively).