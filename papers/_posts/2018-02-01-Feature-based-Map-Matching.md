---
layout: paper
title: "Feature-based Map Matching for Low-Sampling-Rate GPS Trajectories"
year: "2018"
shortref: 
nickname: 
journal: ACM Transactions on Spatial Algorithms and Systems
volume: 
issue: 
pages: 
authors: "Yifang Yin, Rajiv Ratn Shah, Guanfeng Wang, Roger Zimmermann"
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

With the increasing availability of GPS-equipped mobile devices, location-based services have become an
integral part of people’s everyday life. Among one of the initial steps of positioning data management, map
matching aims to reduce the uncertainty in a trajectory by matching the GPS points to the road network on
a digital map. Most existing work has focused on estimating the likelihood of a candidate route based on the
GPS observations, while neglecting to model the probability of a route choice from the perspective of drivers.
In this work, we propose a novel feature-based map matching algorithm that estimates the cost of a candidate
route based on both GPS observations and human factors. To take human factors into consideration is highly
important especially when dealing with low sampling rate data where most of the movement details are lost.

Additionally, we simultaneously analyze a subsequence of coherent GPS points by utilizing a new segment-
based probabilistic map matching strategy, which is less susceptible to the noisiness of the positioning data.

We have evaluated both the offline and the online versions of our proposed approach on a public large-scale
GPS dataset, which consists of 100 trajectories distributed all over the world. The experimental results show
that our method is robust to sparse data with large sampling intervals (e.g., 60 s ∼ 300 s) and challenging track
features (e.g., u-turns and loops). Measurements including map matching accuracy and system efficiency have
been thoroughly evaluated and discussed. Compared with two state-of-the-art map matching algorithms,
our method substantially reduces the route mismatch error by 6.4% ∼ 32.3% (either offline or online with the
window size set to 360 s) with a slight increase in terms of the processing time. The experimental results show
that our proposed method obtains the state-of-the-art map matching results in all the different combinations
of sampling rates and challenging features.