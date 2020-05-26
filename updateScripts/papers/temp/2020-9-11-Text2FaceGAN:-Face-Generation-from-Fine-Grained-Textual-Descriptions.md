---
layout: paper
title: "Text2FaceGAN: Face Generation from Fine Grained Textual Descriptions"
year: "2020"
shortref: 
nickname: 
journal: IEEE BigMM
volume: 
issue: 
pages: 58
authors: "Osaid Rehman Nasir, Shailesh Kumar Jha, Manraj Singh Grover, Yi Yu, Ajit Kumar, Rajiv
Ratn Shah"
image: /assets/images/papers/default-paper.svg
pdf: 
pdflink: https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8919389
github: 
pmid: 
pmcid: 
f1000: 
figshare: 
doi: https://doi.org/10.1109/BigMM.2019.00-42
category: paper
published: true
peerreview: false
review: false
tags: Datasets, Generative Adversarial Networks, Textto Image, Facial Attributes, Face Generation
---

{% include JB/setup %}

# Abstract

In recent years, powerful generative adversarial networks (GAN) have been developed to automatically synthesize realistic images from text. However, most existing tasks are limited to generating simple images such as flowers from captions. In this paper, we extend this problem to the less addressed domain of face generation from fine-grained textual descriptions of face, e.g., "A person has curly hair, oval face, and mustache". We are motivated by the potential of automated face generation to impact and assist critical tasks such as criminal face reconstruction. Since current datasets for the task are either very small or do not contain captions, we generate captions for images in the CelebA dataset by creating an algorithm to automatically convert a list of attributes to a set of captions. The generated captions are meaningful, versatile and consistent with the general semantics of a face. We then model the highly multi-modal problem of text to face generation as learning the conditional distribution of faces (conditioned on text) in same latent space. We utilize the current state-of-the-art GAN (DC-GAN with GAN-CLS loss) for learning conditional multi-modality. The presence of more fine-grained details and variable length of the captions makes the problem easier for a user but more difficult to handle compared to the other text-to-image tasks. We flipped the labels for real and fake images and added noise in discriminator. Generated images for diverse textual descriptions show promising results. In the end, we show how the widely used inceptions score is not a good metric to evaluate the performance of generative models used for synthesizing faces from text.