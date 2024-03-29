# Towards Human-like Educational Question Generation with Large Language Models

## Abstract
We investigate the utility of large pretrained language models (PLMs) for automatic educational assessment question generation. While PLMs have shown increasing promise in a wide range of natural language applications, including question generation, they can generate unreliable and undesirable content. For high-stakes applications such as educational assessments, it is not only critical to ensure that the generated content is of high quality but also relates to the specific content being assessed. In this paper, we investigate the impact of various PLM prompting strategies on the quality of generated questions. We design a series of generation scenarios to evaluate various generation strategies and evaluate generated questions via automatic metrics and manual examination. We provide the best prompting strategy that is most likely to lead to high-quality generated questions, which are supported by our empirical evaluation results. Finally, we demonstrate the promising educational utility of generated questions using our concluded best generation strategy by presenting generated questions together with human-authored questions to a subject matter expert, who despite their expertise, could not effectively distinguish between generated and human-authored questions.


## Method

- generate.py is our method of pulling from OpenAI's API to generate text using GPT-3
  - "input" is the training data fed into the language model with an input at the end that you want to generate a question for
  - an example 5-shot input is given in the file in CTQA form, with an input at the end that should generate a missing question and answer
  - each piece of training data and the input should be seperated by empty lines and a '###' token as seen in the example
  - the user's unique OpenAI API key is needed to generate text
- In each folder there are .txt files that show what training data was used for each experiment
  - any text in parenthesis in these text files are not meant to be inputted into the language model, and are there for your reference only
  - the text in the parenthesis signify the size/length of the training data below, or describe how many "shots" it is at each point (ex: oneshot, fiveshot, etc.)
  - for all questions pulled from the Openstax Biology 2e textbook, the section they came from is given as well as the blooms level (difficulty level)
- the rest of the files in the folder are pickled files that contain results from each of the experiments
  - each pickled file is named to describe what experiment it contains
  - each name ends in t and a number, this number corresponds to the question target pair that was inputted for these results
  - these question target pairs can be found in QT_pairs.txt, where each number in parenthesis defines the target and corresponding context


Presented at AIED, 2022
