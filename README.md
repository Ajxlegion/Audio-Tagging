# Audio Tagging using BERT and GNN

This repository contains an implementation of audio tagging using BERT (Bidirectional Encoder Representations from Transformers) for text-based feature extraction and Graph Neural Network (GNN) for modeling temporal relationships in audio segments.

## Introduction

Audio tagging is the task of assigning one or more labels to an audio clip, indicating the presence of specific sound events or classes. In this project, we utilize state-of-the-art natural language processing (NLP) techniques alongside graph-based modeling to improve audio tagging accuracy and robustness.

## Features

- **BERT for Audio Features**: Leveraging pre-trained BERT models to extract high-level features from audio transcripts.
- **Graph Neural Network (GNN) for Temporal Modeling**: Modeling temporal dependencies between audio segments using GNNs.
- **Mermaid Workflow Representation**: Visual representation of the audio tagging workflow using Mermaid.

## Workflow

```
    A[Audio File] --> B(BERT for Audio Features);
    B --> C(Graph Construction);
    C --> D[Graph Neural Network (GNN)];
    D --> E[Tag Prediction];
```

## Install dependencies

```
cd audio-tagging-bert-gnn
pip install -r requirements.txt
```
