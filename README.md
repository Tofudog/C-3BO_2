# C-3BO_2
The next and ultimate version of C-3BO... I decided not to include this in my original one repo. since this is much more grand. Amazingly, this project was awarded second place by the CIA at ISEF 2023.

## Current Abstract for ISEF 2022-23; check on the following [ISEF database](https://abstracts.societyforscience.org/): 
The American Society of Clinical Oncology estimates a national shortage of over two-thousand hematologists and oncologists by 2025, yet leukemia is consistently among the ten most prevalent forms of cancer worldwide. Deep learning (DL), through the utilization of neural networks, offers considerable promise to these rampant issues. Unfortunately, the biggest barrier to the usage of DL in healthcare is echoed by the black box problem, where a model is too complex to be easily explained or visually interpreted. In lieu of such a problem, this project aimed to expand upon Cancer-3 Blood Oncologist (C-3BO), a previously developed program that accurately detects leukemia, to interpret its diagnoses. First, images of leukemia subtypes were sourced from various hematology databases and applied to preprocessing functions for data augmentation. A deep custom convolutional neural network was meticulously trained to accurately diagnose leukemia and its subtypes. Then, a novel algorithm was developed to recursively reverse-propagate a predicted output value to the original image, in which the most significant features are accentuated. Significantly, this algorithm produces a higher average confidence per image than both experimental patching and sensitivity analysis, two popular techniques in explainable DL. To increase the accessibility of C-3BO, a multilingual website was developed for hematologists to use and provide a personal evaluation of interpretability. Experimental results and examinations suggest that not only is C-3BO a robust and available model, but it also interprets its diagnoses visually.

### check more out on [this paper](https://docs.google.com/document/d/1R0bJ_uDOb27c8gyS7W0VdUe1rOztjpCqi6WRH2BNvYg/edit)


#### the following are intended changes in C-3BO's subsequent version
* Flask will replace Django for web. development
* More algorithms will be compared to Reverse Propagation
* The testing method for various interpretative will change (tbd)
* and much more will be presented here

The time frame for the development of C-3BO is over 2.5 years! Since then, this project has been growing exponentially. Commencing as a normal leukemia binary classifier ([paper_1](https://docs.google.com/document/d/17uJWoE8gqPTfz0yZE0a_Q3HpVYpWcqx1lji7vLFfbFU/edit)) to a multi-leukemia detector with genetics ([paper_2](https://docs.google.com/document/d/1Px5ljJkMrgZpUHBKWMDIMD_oA6sYNWNazDugSxHR8fU/edit)), there is so much promise in this innovative technology. One day, I envision a hospital where high-stage leukemia will have been eradicated. C-3BO is, I hope, the next step to this goal.

***Em homenagem ao meu maravilhoso avô, que de repente foi diagnosticado com leucemia mielóide crônica.***
