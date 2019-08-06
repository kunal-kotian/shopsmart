# shopsmart
Paper presented at IEEE Consumer Communications and Networking Conference:
https://ieeexplore.ieee.org/document/8651723

## Background
-	As a part of my Master's degree in Data Science at USF, we were required to complete a 7-week-long project demonstrating a solution to a problem leveraging data and to make a viable product out of it.
-	We focused on health supplement buyers on Amazon.  These buyers face an overwhelming amount of options.
-	It can be hard to distinguish between highly rated health supplements – one must spend hours reading through several reviews or risk making a less-than-optimal purchase that could impact your health in an unexpected way.
- **Motivation: Equip health supplement shoppers with information to help them easily make informed purchases**

## Our Data Product - ShopSmart.ml
- A webapp that displays topic scores for 3 categories for each product.  Categories are ‘Efficacy’, ‘Cost’, ‘Service’. Scores represent the extent to which the topics were discussed in the product’s reviews.
- Scores calculated by a rules-based model using counts of occurrences of category-specific words in reviews.
- The category-specific words that the rules-based model looks for were found using word similarity on a custom-trained word2vec model.
- Additional aspects of the product naturally emerging from reviews – e.g. taste or texture – were found using topic modeling and reported on the website.

### Where is the App Now?
- We killed the server that the app ran on last year once we started running out of AWS credits.

## Teamwork
- This was a group project.  My teammates: Deena Liz John, Ernest Kim, Ker Yu Ong, Tyler White.
- Each of us focused on different aspects of the project (data acquisition, data engineering, web server setup, etc.).  I led the modeling effort.

## Navigating this repository
Unfortunately, the code in the notebooks here is somewhat chaotic - the result of super-tight grad school deadlines :-). Here are the most important documents to navigate this work:
- Presentation on the work:  https://github.com/kunal-kotian/shopsmart/blob/master/shopsmart_presentation.pdf
  - This excludes the CorEx topic modeling approach; explains the LDA approach instead.
- Notebook showing text pre-processing + rules-based topic scoring model for Efficacy, Cost, Service (ECS) + LDA for uncovering other (non-ECS) topics:  https://github.com/kunal-kotian/shopsmart/blob/master/Notebooks/kk_topic_modeling_v2.ipynb
- Notebook showing text pre-processing + rules-based topic scoring model for ECS + CorEx for uncovering other (non-ECS) topics: https://github.com/kunal-kotian/shopsmart/blob/master/Notebooks/kk_topic_modeling_v3_cleaned.ipynb
