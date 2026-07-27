# Recommendation Systems — Research Notes

**Synthesis from reference sources (May 16, 2026).** This is a beginner-friendly reference document. Where I quote a source by name, the citation is at the end.

## Sources used

1. **Gheewala et al. (2024)** — *In-depth survey: deep learning in recommender systems—exploring prediction and ranking models, datasets, feature analysis, and emerging trends.* Neural Computing and Applications. (Same paper hosted at the d-nb.info link.)
2. **Pang Li et al. (2024)** — *A Survey on Deep Neural Networks in Collaborative Filtering Recommendation Systems.* arXiv:2412.01378.
3. **Vector Institute Recommender Systems Survey repo** — *A Comprehensive Review of Recommender Systems: Transitioning from Theory to Practice* (covers 2017–2024).

---

## 1. What problem does a recommendation system solve?

When users land on a website with millions of items (Amazon, Netflix, Spotify, YouTube), they can't browse everything. The system needs to pick a small set of items each user is most likely to enjoy. This is **the information overload problem**.

The system uses what it knows about you (past clicks, ratings, profile) and what it knows about items (genre, content, popularity) to predict what you will like.

Recommendation systems are used in:
- E-commerce (Amazon, Flipkart, Myntra)
- Video streaming (Netflix, YouTube, JioHotstar)
- Music (Spotify, JioSaavn)
- News and social feeds (Sharechat, MX Player)
- Food delivery (Swiggy, Zomato)
- Healthcare (drug or treatment suggestions)
- Education (course or paper recommendations)

---

## 2. The three classical paradigms

Almost every survey starts here. Memorize these three — they are the foundation.

### 2.1 Collaborative filtering (CF)

**Idea:** "People similar to you liked X, so you may like X too."

The system looks at past user-item interactions (ratings, clicks, views, purchases) and finds patterns across users.

**Two sub-types:**
- **Memory-based CF** — Look at the raw user-item rating matrix. Compute similarity between users (or between items). Predict the rating a target user would give an item by averaging ratings from similar users. Older method. Simple but doesn't scale.
- **Model-based CF** — Learn a model (matrix factorization, neural networks) from the rating data. The model produces predictions. Modern approach. Scales better.

**The classic algorithm: matrix factorization (MF).** Represent each user and each item as a vector of "latent features" (say 50 numbers each). The predicted rating of a user for an item is the dot product of their two vectors. You learn the vectors by minimizing the prediction error on known ratings.

**Strengths:** Works without any item features — only needs interaction data. Captures patterns that humans wouldn't think of.

**Weaknesses:**
- **Cold start (new user):** No history to compare against. The system has nothing to work with.
- **Cold start (new item):** No one has rated it yet. The system can't recommend it.
- **Sparsity:** Real rating matrices are 99%+ empty. Most users have rated only a tiny fraction of items. Hard to find reliable patterns.
- **Scalability:** Computing similarity across millions of users is expensive.

### 2.2 Content-based filtering

**Idea:** "You liked items with property X before, so you'll like other items with property X."

The system uses item features (genre, director, actors, plot keywords, product description) and recommends similar items to ones you've liked.

**The classic technique: TF-IDF + cosine similarity.** Turn each item's description into a vector of word weights. Compute similarity between items as the cosine angle between their vectors. Recommend items similar to ones the user already liked.

**Strengths:** Solves the new-item cold start problem (you can recommend a new item if it has features). Doesn't need other users.

**Weaknesses:**
- **Over-specialization (filter bubble):** Always recommends similar items. Never surfaces new genres. Boring.
- **Requires good item features.** If features are noisy or missing, it fails.
- **Doesn't solve the new-user cold start.** You still need to know what the new user likes.

### 2.3 Hybrid

**Idea:** Combine collaborative filtering and content-based to get the strengths of both.

Three common ways to combine:
- **Weighted hybrid:** Each method produces a score; final score is a weighted sum. (E.g., 0.6 × CF score + 0.4 × content score.)
- **Switching hybrid:** Use different methods in different situations. (E.g., for new users use content-based; for established users use CF.)
- **Mixed hybrid:** Show recommendations from both methods together in the same list.

**More advanced versions:** combine multiple deep neural networks, or combine CF with side information like user tags or item metadata.

The Gheewala paper notes hybrid is the way production systems usually work because relying on any single method has clear weaknesses.

---

## 3. Two ways to define the recommendation task

This is a subtle distinction that matters a lot.

### 3.1 Rating prediction

**Goal:** Predict the numerical score a user would give an item (e.g., 4.2 out of 5).

**Type of problem:** Regression.

**Typical metrics:** RMSE (Root Mean Squared Error), MAE (Mean Absolute Error). Lower is better.

**Used when:** The platform explicitly asks users for ratings (Netflix's "rate this movie", Amazon's 5-star reviews).

**Strengths:**
- Personalizes well.
- Easy to evaluate with clear quantitative metrics.

**Limitations:**
- Cold start hurts heavily — without past ratings from a user, you can't predict anything.
- Struggles with sparse data.
- A great rating prediction doesn't always translate to good "what to show next."

### 3.2 Top-N ranking

**Goal:** Pick the N best items to show the user out of millions of candidates.

**Type of problem:** Classification / ranking.

**Typical metrics:** Precision@K, Recall@K, NDCG (Normalized Discounted Cumulative Gain), MAP (Mean Average Precision), MRR (Mean Reciprocal Rank), Hit@K. Higher is better.

**Used when:** The platform doesn't ask for ratings, only tracks clicks/views (most modern systems — YouTube, TikTok, Instagram).

**Strengths:**
- Provides diverse recommendations.
- Encourages exploration.
- Flexible for many domains.

**Limitations:**
- May favor popular items over personalized ones (popularity bias).
- Struggles with "long-tail" niche items.
- Evaluation is harder — there's no single ground-truth "right answer."

> **Important:** When you commit to a project, choose one task. They use different metrics, different loss functions, and different evaluation protocols. Most modern industry systems care about top-N ranking, but rating prediction is easier for a first project.

---

## 4. The deep learning era (2015–present)

Around 2015, deep learning took over recommender systems. The reason: classical methods (matrix factorization, TF-IDF) only capture linear relationships between users and items. Neural networks capture non-linear, complex patterns.

The Pang Li paper says clearly: "Deep neural networks can encode more complex abstract concepts in higher-level data representations" — that's the core claim.

### 4.1 Neural Collaborative Filtering (NCF) — the bridge

NCF (He et al., 2017) replaced the dot product in matrix factorization with a neural network. The user and item embeddings are still learned, but the prediction is computed by a multi-layer perceptron (MLP) instead of a dot product.

Why this matters: it lets the model learn non-linear interactions. A dot product can only express linear relationships; a neural net can express arbitrary functions.

NCF is the conceptual starting point for all "deep CF" work. Worth understanding the architecture deeply.

### 4.2 Traditional deep learning architectures used in rec sys

The Pang Li survey lists seven core architectures. The Gheewala survey adds attention and LLM as the "modern" extensions.

| Architecture | What it does | Why used in rec sys |
|---|---|---|
| **MLP** (Multilayer Perceptron) | Stack of fully-connected layers with non-linear activations | The foundation. NCF is built on MLP. Captures complex user-item interactions. |
| **CNN** (Convolutional Neural Network) | Local feature extraction via convolutions | Used to extract features from item images, reviews, or sequences. |
| **RNN** (Recurrent Neural Network, includes LSTM, GRU) | Processes sequences | Used for sequential/session-based recommendation: "what should I show next given the user's last 10 clicks." |
| **GNN** (Graph Neural Network) | Operates on graph-structured data | Treats users and items as nodes in a graph; learns by passing messages across edges. Captures higher-order relationships ("friend of friend liked this"). |
| **Autoencoder** (AE, VAE, DAE) | Encodes input → decodes back | Used to learn dense user/item representations from sparse rating matrices. Variational versions (VAE) are popular for top-N ranking. |
| **GAN** (Generative Adversarial Network) | Generator vs discriminator | Used for synthetic data generation, augmenting sparse data. Less common but growing. |
| **RBM** (Restricted Boltzmann Machine) | Two-layer stochastic network | One of the earliest neural approaches to CF. Mostly historical now. |

### 4.3 Modern deep learning architectures (2022–2024)

The Gheewala paper specifically singles out three "modern" categories that current SOTA work uses:

- **Attention networks (DAN)** — Learns which past interactions or which item features matter most for a specific user. The "self-attention" mechanism (from Transformer models) gave a big boost to recommendation accuracy.
- **Graph Neural Networks (GNN)** — Specifically LightGCN, KGAT, and graph-augmented CF models. These are arguably the most active research direction right now.
- **Large Language Models (LLM)** — Use LLMs (GPT, LLaMA) to either generate recommendations directly from text descriptions or augment traditional models with semantic understanding.

The Vector Institute survey lists these advanced categories explicitly:
- Neural Collaborative Filtering (NCF)
- Variational Autoencoders (VAE)
- LightGCN, KGAT, Graph Neural Networks
- BERT4Rec (a BERT-style transformer adapted for sequential recommendation)
- Knowledge graph approaches
- Deep reinforcement learning
- LLM-based recommendation agents
- Multimodal systems (visual + text features)

### 4.4 Specialized recommendation directions

These aren't algorithms but problem framings that need different techniques:

- **Sequential/Session-based** — "Given the user's recent clicks, what's the next click?" (RNN-based, BERT4Rec.)
- **Context-aware** — Incorporates time, device, location into the recommendation. ("What movie does this user want on a Sunday evening on mobile?")
- **Cross-domain** — Use data from one domain (movies) to recommend in another (books).
- **Knowledge-based** — Uses external knowledge graphs (Wikipedia, domain ontologies).
- **Explainable** — Don't just recommend; explain *why*.
- **Fairness-aware** — Don't disadvantage certain users or items based on demographic or popularity bias.
- **Review-based / aspect-based** — Mines text reviews for fine-grained preference signals.

---

## 5. Datasets you'll actually encounter

These keep coming up across all 3 sources:

| Dataset | What it has | Why used |
|---|---|---|
| **MovieLens** (100K / 1M / 10M / 20M / 25M) | Movie ratings from real users (GroupLens) | Standard benchmark for almost every rec sys paper. Free. Multiple size variants. Start here. |
| **Netflix Prize** | 100M+ movie ratings from Netflix | The dataset that drove the field 2006–2009. Free on Kaggle. |
| **Amazon Reviews** | Product ratings + reviews across categories | Big dataset, good for hybrid (CF + content + text reviews). |
| **Yelp** | Business ratings, reviews, social network | Used for location/POI recommendation, review-based methods. |
| **LastFM** | Music listening history | Used for music recommendation, sequential modeling. |
| **Pinterest** | Pin-board interactions | Used for image-based and graph-based recommendation. |
| **Epinions** | Product ratings with trust/distrust network | Used when social trust matters. |
| **Citeulike** | Academic paper bookmarks | Used for paper recommendation, citation-based research. |

For a first project, **MovieLens 1M is the canonical starting point**. It's small enough to run on a laptop and supported by every library.

---

## 6. Evaluation metrics — the practical list

### For rating prediction
- **RMSE (Root Mean Squared Error):** average of squared errors, square-rooted. Penalizes large errors heavily.
- **MAE (Mean Absolute Error):** average of absolute errors. Easier to interpret. More forgiving of outliers.

### For top-N ranking
- **Precision@K:** Of the top K recommendations, what fraction are relevant?
- **Recall@K:** Of all relevant items, what fraction appear in the top K?
- **F1@K:** Harmonic mean of precision and recall.
- **NDCG@K (Normalized Discounted Cumulative Gain):** Rewards relevant items appearing higher in the ranked list.
- **MAP (Mean Average Precision):** Averages precision over multiple recall points.
- **MRR (Mean Reciprocal Rank):** Average of 1/rank of first relevant item.
- **Hit@K:** Did at least one relevant item appear in the top K? Yes/no per user.

### Beyond accuracy
The Gheewala paper specifically notes that "modern systems address concerns beyond accuracy":
- **Diversity:** Are recommendations spread across categories?
- **Coverage:** What fraction of the item catalog does the system ever recommend?
- **Novelty:** Are recommended items genuinely new to the user?
- **Serendipity:** Do recommendations include pleasantly unexpected items?
- **Fairness:** Do recommendations work equally well across user demographics?
- **Explainability:** Can you justify why this item was recommended?

A real ML engineer reports both accuracy and at least one beyond-accuracy metric. Reporting only RMSE is now considered weak.

---

## 7. The five big open problems

Almost every survey lists the same handful. These are where ML thinking lives — knowing how each affects each approach is the depth bar.

### 7.1 Cold start
- **User cold start:** New user with no history. CF can't help. Content-based and demographic methods can.
- **Item cold start:** New item with no ratings. CF can't help. Content-based methods can.
- **System cold start:** New platform with no data at all. Hardest case.

### 7.2 Sparsity
Most real rating matrices are 99%+ empty. Users have rated 0.1% of items. CF methods that need many overlapping ratings between users struggle here. Deep learning approaches help by learning compact representations from sparse data.

### 7.3 Scalability
With millions of users and millions of items, computing similarities or running neural net inference per request becomes expensive. Most production systems use two stages:
- **Candidate generation (retrieval):** Cheap method that reduces millions of items to ~hundreds.
- **Ranking:** Expensive deep model that ranks those hundreds.
This "two-tower" or "retrieval + ranking" architecture is industry standard.

### 7.4 Filter bubble / popularity bias
Always recommending similar or popular items reduces user discovery. The system becomes self-reinforcing — popular items get recommended more, get more views, become more popular. Active research direction: how to inject diversity without hurting accuracy.

### 7.5 Explainability and fairness
- **Explainability:** Users (and regulators) want to know *why* something was recommended. Black-box deep models hide this.
- **Fairness:** Do recommendations underserve minority users? Do they suppress long-tail items? Are they biased by gender, age, location?
- **Privacy:** Can we recommend without storing sensitive user data? (Federated learning is one answer.)

---

## 8. Current trends (2024–2026)

What's hot in research right now according to the surveys:

1. **LLM-based recommendation** — Using GPT/LLaMA as the recommendation engine, or as an augmentation to traditional models. Combines world knowledge with collaborative signal.
2. **Graph Neural Networks (especially LightGCN derivatives)** — Considered the most active research direction by the Gheewala paper.
3. **Multimodal recommendation** — Combining text, images, audio, video features.
4. **Sequential / transformer-based** — BERT4Rec, SASRec, GPT-like models for next-item prediction.
5. **Federated learning** — Train recommendation models without centralizing user data (privacy).
6. **Explainable recommendation** — Producing justifications alongside recommendations.
7. **Fairness-aware** — Demographic and item-side fairness constraints.
8. **Conversational recommendation** — User and system have a back-and-forth dialogue to refine recommendations.
9. **Reinforcement learning** — Treat recommendation as a long-term reward-optimization problem (Netflix, YouTube use this).

---

## 9. The industry-academic gap

The Vector Institute survey is unusually honest about this:

> "Specific recommender system methodologies from academia should be applied across various industry sectors strategically."

Translation: most academic papers benchmark on MovieLens at small scale with offline metrics. Real industry rec sys (Netflix, Spotify, Pinterest) deal with:
- Billions of items.
- Real-time inference (~100ms budget).
- Online A/B testing as the real evaluation.
- Business-driven metrics (revenue, retention, engagement) that aren't in academic papers.
- Multi-stage retrieval-then-ranking pipelines.

For a portfolio project as a learner, you can't replicate industry scale. But you *can* show that you understand the gap. Mentioning that your offline NDCG number doesn't equal a production win is itself a sign of ML engineering maturity.

---

## 10. Glossary of terms

| Term | Meaning |
|---|---|
| **Embedding** | A learned vector of numbers that represents an entity (user, item, word). Similar entities have similar vectors. |
| **Latent factor** | Same idea as embedding — features that aren't directly observed but are learned from data. |
| **Implicit feedback** | User actions that signal interest but aren't ratings (clicks, views, time spent). Mostly binary or one-class. |
| **Explicit feedback** | User actions where they explicitly state preference (1–5 star rating, thumbs up/down). |
| **User-item interaction matrix** | A big sparse matrix where rows = users, columns = items, and entries = ratings or interactions. |
| **Matrix factorization (MF)** | Decompose the user-item matrix into two smaller matrices (user features × item features). The classic CF method. |
| **SVD (Singular Value Decomposition)** | A mathematical method for matrix factorization. In rec sys, "SVD" often means "MF trained with gradient descent" (Simon Funk's version), not the linear algebra version. |
| **BPR (Bayesian Personalized Ranking)** | A loss function for top-N ranking that learns from pairs: "user prefers item A over item B." |
| **One-class problem** | When you only have positive feedback (clicks) and no negative feedback (no "dislikes"). Most modern data looks like this. |
| **Negative sampling** | Randomly picking unseen items as "negatives" during training, since you don't have explicit negative labels. |
| **Two-tower model** | Production architecture where one network produces user embeddings, another produces item embeddings, and similarity is computed at retrieval time. |
| **Candidate generation / Retrieval** | First stage of production rec sys — narrows millions of items to hundreds quickly. |
| **Ranker** | Second stage — orders the candidates carefully using a heavier model. |
| **DER, MAE, RMSE, NDCG, MAP, MRR, Hit@K, Precision@K, Recall@K** | Evaluation metrics — see Section 6. |

---

## 11. Limits of this synthesis

- The 3 sources I read are all DL-focused. They under-represent classical (non-DL) methods like FunkSVD, ALS, item-item CF, and content-based methods. For those, Andrew Ng's Course 3 + the Microsoft Recommenders repo are more practical references.
- This document is a *starting point*, not a substitute for reading the papers yourself when you want to dig into a specific technique.

---

## 12. Citations (full)

- Gheewala, S., Xu, S., & Yeom, S. (2025). *In-depth survey: deep learning in recommender systems—exploring prediction and ranking models, datasets, feature analysis, and emerging trends.* Neural Computing and Applications, 37: 10875–10947. https://doi.org/10.1007/s00521-024-10866-z
- Li, P., Mohd Noah, S. A., & Mohd Sarim, H. (2024). *A Survey on Deep Neural Networks in Collaborative Filtering Recommendation Systems.* arXiv:2412.01378.
- Vector Institute Recommender Systems Survey. https://github.com/VectorInstitute/Recommender-Systems-Survey (companion repo to "A Comprehensive Review of Recommender Systems: Transitioning from Theory to Practice" covering 2017–2024).
