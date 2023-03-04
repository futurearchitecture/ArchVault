Tags: #Reference 

## GPT-3 is superior to all earlier models in terms of producing text that appears to have been produced by a person

GPT-3 is a neural network ML model that can generate any type of text from internet data. It was created by OpenAI, and it only needs a tiny quantity of text as an input to produce huge amounts of accurate and complex machine-generated text.

About 175 billion ML parameters make up the deep learning neural network used in GPT-3. To put things in perspective, Microsoft’s Turing NLG model, which has 10 billion parameters, was the largest learned language model before GPT-3. GPT-3 will be the biggest neural network ever created as of early 2021. As a result, GPT-3 is superior to all earlier models in terms of producing text that appears to have been produced by a person.

##### Parameters of GPT-3

Predictive text can be produced using the OpenAI GPT-3 ML model via an API. We may utilize several models from OpenAI, but “text-davinci-002” is by far the most powerful.

##### Engine

The prediction-generating AI model is specified by the engine parameter.

##### Max tokens

The maximum number of tokens that can be created by the model is specified by the “max tokens” option. A token can be thought of as a word fragment.

##### Temperature

The model generates unnormalized values that haven’t yet been converted to probabilities (logits). The logits are often converted into probabilities using a method like softmax.

However, we can utilize a thermodynamics-inspired approach to scale the logits with the temperature parameter before using the softmax function, i.e., softmax (logits/temperature).

The logits are fed directly through the softmax function if the temperature parameter is near 1. The model gets more predictable and will always output the same set of tokens following a particular sequence of words if the temperature is near zero, making the highest probability tokens more likely relative to the other tokens.

##### Top p

An inference time sampling threshold is specified by the top p parameter. A method for sampling potential model outcomes is known as top p sampling (also known as nucleus sampling).

Imagine that the model must forecast the token that will come after the phrase “I want to eat” to better grasp this idea. For the sake of simplicity, let’s assume that a token is a term and that the model generates the probabilities shown below:

-   carrots (2% likely),
-   cucumbers (1.5% likely),
-   aubergines (1% likely),
-   Spinach (0.5% likely),
-   Broccoli (0.3% likely),
-   ….

This set of words constitutes a probability distribution “P (Word | “I want to eat”),” and the cumulative distribution function (CDF) looks like this:

-   2% with carrots,
-   3.5% with carrots and cucumbers,
-   4.5% with carrots, cucumbers, and aubergines
-   …

The model will sample and randomly choose between carrots and cucumbers based on their likelihood of the top p-parameter being set to 3.5 percent. The model will choose a word at random from the list of carrots, cucumbers, and aubergines with a top p of 4.5 percent.

The top p parameter regulates the model’s uniqueness and randomness, just like the temperature does.

##### Frequency penalty

The model’s propensity to repeat predictions is controlled by the frequency penalty parameter. The likelihood of already-generated words is decreased by the frequency penalty. Depending on how many times a word has already been in the prediction, there will be a penalty.

##### Presence penalty

The model is encouraged to create new predictions by the presence penalty parameter. The presence penalty reduces a word’s probability if it has previously been used in the projected text. The presence penalty does not rely on how frequently terms appear in previous forecasts, in contrast to the frequency penalty.


now express these parameters as yaml with number ranges

engine:
  type: text-davinci-002

max_tokens:
  min: 0
  max: 1000
  
temperature:
  min: 0.0
  max: 1.0
  
top_p: 
  min: 0.0
  max: 1.0  
  
frequency_penalty: 
  min: 0.0
  max: 1.0  
  
presence_penalty: 														    	
min : 0.0                                            
max : 1.0

GPT-3 currently offers three different engine types:

- Davinci: This engine is the most powerful of the three and is capable of generating text from a tiny amount of input. It is suitable for many tasks, including natural language processing, question answering, and summarization.

- Ada: This engine is slightly less powerful than Davinci but has been optimized for tasks such as machine translation and text classification.

- Babbage: This engine is the least powerful of the three but has been optimized for tasks such as sentiment analysis and document understanding.



