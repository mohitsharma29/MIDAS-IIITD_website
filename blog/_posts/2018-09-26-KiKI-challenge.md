---
layout: post
title: "Kiki Challenge Dataset Release"
author: "Nupur Baghel"
author_handle: "Nupur"
category: blog
tags: [other]
---
{% include JB/setup %}
#Kiki Kills : Not Every Challenge is worth taking
## Introduction 
### What is this challenge about? 
One of the most famous online social media challenge these days is the Kiki challenge. Also known as “In My Feelings Challenge” or “Do The Shiggy”, it originated when a comedian Shiggy released a video, dancing on the road to the tunes of this song by Drake. Since then people have considered it to be a challenge in which they need to get down of a moving car, and dance alongside the traffic risking their lives and getting their video captured.

### How popular is the challenge ?
There is no country which has been left untouched when it comes to this. It originated in Canada and spread over the world including United States, Mexico, United Kingdom, India, South Africa, Costa Rica, Egypt, Argentina and so on. People are sharing thousands of tweets commonly involving their videos on a daily basis on social platforms like Twitter and Facebook.

## What’s wrong !!?
While it is good to dance and burn some calories, but when it comes to the road it is not such a brilliant idea. There has been many reported incidents where people have been hit by speedy vehicles, fallen off the car and collided head-start with electric poles. It possesses a serious risk to life if not taken with precautions and may even lead to death. 

<iframe width="560" height="315" src="https://www.youtube.com/embed/YuEbz_Qkx3Q?rel=0&autoplay=0
&amp;start=15;end=22" frameborder="0"></iframe>

## Our contributions
Realising the importance and implications that this challenge has on the life of so many people, MIDAS decided to build a system which can detect the danger in a given video. The exact methodology followed by us was -

### 1. Analysing the common hashtags used
We started with collecting tweets for the last 15 days using the Tweepy API. Next, we scanned through the data to find out what were the top 20 most commonly used hashtags during the July-August duration using their frequency of occurrence.
Results of this analysis can be found here - [Distribution of Hashtags in Twitter data](https://drive.google.com/file/d/1mCIu4Wk6xog8ATUOdIORmClCUgyT7sNt/view?usp=sharing)

### 2. Creating a dataset from social platforms
- Tweet Collection: The common hashtags discovered in the previous step were used as keywords for further searching of tweets for the complete duration of late June to September. Data from hashtags such as #mumbai police and #egypt police which had comparatively smaller frequency were collected separately.

- Video Collection: After we had a good set of tweets, we used the URLs provided as a parameter inside tweets to download corresponding videos.

- Annotation: Two annotators worked through the complete list of videos categorising them as either safe or dangerous. Removal of retweeted videos as well as irrelevant videos which seemed to not relate was simultaneously done.
Cross annotation parameter was also calculated by labelling 400 videos for each of the annotators to ensure there was consistency. This test was successful and we obtained a high value (0.95) of Cohen’s Kappa.

### 3. Building a model for detecting dangerous incidents 
We built a video classification model with VGG16 as the base model. This was appended with a subtle combination of flatten, fully connected dense layers, max pooling layers and dropout layers.
The model works by taking as input a batch of data containing captured frames of the video we want to classify. The output produced is the probabilities of video between safe and dangerous. Thus we classify the category of the video after rounding the probabilities to the nearest possible values.
![Structure of Model](https://drive.google.com/file/d/1-CAxz-_l6hG_AHbv3azHr9g5D2xdIfZz/view?usp=sharing)

### 4. Evaluation of models to judge their consistency 
We used model checkpointing to store the weights of the best model. Further, to determine the consistency of our model we evaluated it on the test set. An accuracy of 87 percent was obtained, along with a precision of 0.96, and recall score of 0.9.

## Future Work
Although the current model is fair enough to generate good results, it can surely be improved to account for time analysis using recurrent neural network models. 
We also plan to create a hybrid model which can take into account both the textual and visual data in a tweet and generate results more accurately.

### The following video provides a complete summary:
<iframe src="https://drive.google.com/file/d/1cU8REZhDGT3eEpz_txBRLxauRTKHdY15/preview" width="640" height="480"></iframe>


## About Us: 
### The authors involved for this project are:
**Nupur Baghel, Yaman Kumar, Paavini Nanda, Rajiv Ratn Shah, Debanjan Mahata and Roger Zimmermann** 
All of us are members of the MIDAS community.

To help on improving research in this domain we are hereby releasing the dataset which contains more than 2.3k videos of the KIKI challenge collected from Twitter. 
## KIKI Datasets Download
For the time being the dataset is avalable on request. Anyone intrested can send us a request via E-mail stating there purpose of use (We did some work for you, just click [here](mailto: yamank.co@nsit.net.in?subject=Request For KiKi challenge dataset)). We will respond within 7 days. 

Please refre our dataset as below 

Nupur Baghel, Yaman Kumar, Paavini Nanda, Rajiv Ratn Shah, Debanjan Mahata and Roger Zimmermann : Kiki Kills: Identifying Dangerous Challenge Videos from Social Media (2018).






