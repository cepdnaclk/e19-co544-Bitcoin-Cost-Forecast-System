---
layout: home
permalink: index.html

# Please update this with your repository name and title
repository-name: e19-co544-Bitcoin-Cost-Forecast-System
title: BitPredictor
---

[comment]: # "This is the standard layout for the project, but you can clean this and use your own template"

# BitPredictor: Empowering Investments with Machine Learning

![Logo](./images/logo.png)

Welcome to BitPredictor, a cutting-edge machine learning project designed to empower cryptocurrency investments through predictive analytics. This project leverages historical Bitcoin price data to build robust predictive models, helping investors make informed decisions.

---

<!-- 
This is a sample image, to show how to add images to your page. To learn more options, please refer [this](https://projects.ce.pdn.ac.lk/docs/faq/how-to-add-an-image/)

![Sample Image](./images/sample.png)
 -->

## Team
-  E/19/091, Dissanayake P.A.M., [email](mailto:e19091@eng.pdn.ac.lk)
-  E/19/111, Galappaththi M.D., [email](mailto:e19111@eng.pdn.ac.lk)
-  E/19/166, Jayathunga W.W.K., [email](mailto:e19166@eng.pdn.ac.lk)
-  E/19/227, Madhushanka M.P.J., [email](mailto:e19227@eng.pdn.ac.lk)
-  E/19/304, Pushpakumara R.M.S.P., [email](mailto:e19304@eng.pdn.ac.lk)


## Table of Contents
1. [Abstract](#abstract)
2. [Introduction](#introduction)
3. [Problem Statement](#problem-statement)
4. [Methodology](#methodology)
5. [Results](#results)
6. [Features](#features)
7. [Keywords](#keywords)
8. [Skills & Technologies](#skills-&-technologies)
9. [Conclusion](#conclusion)
10. [Links](#links)

---

## Abstract
This project focuses on the development and deployment of a comprehensive Bitcoin price prediction system utilizing various machine learning models, including ARIMA, State Space Models (SSM), Support Vector Machines (SVM), XGBoost, Recurrent Neural Networks (RNN), and Random Forests. Among these, the Long Short-Term Memory (LSTM) model was selected for final deployment due to its superior performance in capturing temporal dependencies in the data. The LSTM model was fine-tuned and integrated into a deployment pipeline on Microsoft Azure, with a Flask web application developed to serve real-time predictions.

## Introduction

Bitcoin, a decentralized digital currency, has seen significant price volatility, making accurate price prediction essential for investors and traders. This project aims to develop a robust prediction model using LSTM, a type of RNN known for capturing long-term dependencies in time-series data. The project evaluates various models and highlights the practical application of deploying machine learning models in a cloud environment.

### What is Bitcoin?
Bitcoin is like digital money we can use on the internet. It doesn’t need banks or governments to work. It’s like having our own bank in our pocket. It uses a technology called blockchain. Think of it as a digital ledger that records all transactions made with Bitcoin. These transactions are made directly between users, not through a middleman. This is what we mean by peer-to-peer. To make sure these transactions are valid, they are checked using a process called proof-of-work. People called miners do this work of checking and they get rewarded with new Bitcoins for their effort. This is how new Bitcoins are created.

So, in simple terms, Bitcoin is a type of online money that works without a bank, where all transactions are recorded on a digital ledger called blockchain.

## Problem Statement
Knowing the future price of Bitcoin is important for people who want to invest in it. If the price of Bitcoin is low, people might not want to invest in it. Instead, they might want to put their money into other things.

The prices of cryptocurrencies like Bitcoin can change a lot in a short time, which can be a problem for users. There are many factors that cause these price changes. It’s hard to solve this problem, but techniques like machine learning, pattern recognition, and data mining can help.

Many researchers and developers are working on ways to predict cryptocurrency prices. Our goal is to create a system that can predict the cost of Bitcoin.

In simple terms, we’re trying to create a system that can tell us what the price of Bitcoin might be in the future. This can help people decide when to invest in Bitcoin.

## Methodology
1. Data Collection: Historical Bitcoin price data from Yahoo Finance, spanning from January 1, 2015, to May 23, 2024.
2. Data Preprocessing & EDA:
* Time Series Plots: Visualization of Bitcoin's historical price data.
* Missing Values Check: Ensuring data integrity.
* Histograms & Scatter Plots: Analyzing the distribution and relationships between different price metrics.
* Heat Maps & Correlations: Identifying relationships between various features.
* Density Plots & Pair Plots: Examining the distribution and interrelationships among Bitcoin’s financial metrics.
3. Model Training:
* Multivariate LSTM Model: Split data into sequences, convert to tensors, reshape tensors, define model architecture, and perform hyperparameter tuning.
4. Model Evaluation: Compare performance across different models, with LSTM showing the best results.
5. Deployment: Integrate the LSTM model into a Flask web application on Microsoft Azure for real-time predictions.

## Results
The LSTM model demonstrated superior performance in predicting Bitcoin prices compared to other models. It was fine-tuned for optimal performance and successfully integrated into a user-friendly web application, providing real-time predictions.

## Features
* Historical Data Analysis: Utilizes extensive historical Bitcoin price data to understand market trends.
* Feature Engineering: Creates meaningful features that improve prediction accuracy.
* Predictive Modeling: Implements state-of-the-art machine learning models, including Random Forest, to predict future Bitcoin prices.
* Model Evaluation: Evaluates model performance using metrics such as Mean Squared Error (MSE) and visualizes predictions against actual prices.
* Scalability: Built with PySpark to handle large datasets efficiently, ensuring scalability for extensive market data.

## Keywords
Bitcoin, Price Prediction, LSTM, ARIMA, SSM, SVM, XGBoost, RNN, Random Forest, Time-Series Forecasting, Machine Learning, Deep Learning, Neural Networks, Azure Deployment, Flask Application, Cryptocurrency

## Skills & Technologies
* Programming Languages: Python
* Libraries and Frameworks: TensorFlow, PyTorch, scikit-learn, Flask, Seaborn, Matplotlib
* Cloud Services: Microsoft Azure
* Machine Learning Models: ARIMA, State Space Models (SSM), Support Vector Machines (SVM), XGBoost, Recurrent Neural Networks (RNN), Random Forests, Long Short-Term Memory (LSTM)
* Data Analysis Techniques: Time Series Analysis, Exploratory Data Analysis (EDA), Feature Selection, Data Normalization and Standardization
* Visualization Tools: Matplotlib, Seaborn
* Deployment Tools: Flask, Microsoft Azure

## Conclusion
The project illustrates the effectiveness of LSTM in time series forecasting and its practical application in a cloud environment. It provides valuable insights and tools for navigating the volatile Bitcoin market.

.....

## Links

- [Project Repository](https://github.com/cepdnaclk/e19-co544-Bitcoin-Cost-Forecast-System)
- [Project Page](https://cepdnaclk.github.io/e19-co544-Bitcoin-Cost-Forecast-System)
- [Department of Computer Engineering](http://www.ce.pdn.ac.lk/)
- [University of Peradeniya](https://eng.pdn.ac.lk/)


[//]: # (Please refer this to learn more about Markdown syntax)
[//]: # (https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
