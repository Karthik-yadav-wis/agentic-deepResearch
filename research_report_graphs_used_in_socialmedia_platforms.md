# Research Report: graphs used in socialmedia platforms

# Graphs Used in Social Media Platforms

## Table of Contents
1. [Overview](#overview)
2. [Types of Graphs Used in Social Media](#types-of-graphs-used-in-social-media)
3. [How Social Media Platforms Use Graphs](#how-social-media-platforms-use-graphs)
4. [Common Graph Algorithms and Analytics](#common-graph-algorithms-and-analytics)
5. [Platform Examples](#platform-examples)
6. [Technical and Design Considerations](#technical-and-design-considerations)
7. [Conclusion](#conclusion)
8. [Sources](#sources)

## Overview

Social media platforms rely heavily on **graph data structures** and **graph theory** to represent and analyze relationships between users, content, and interactions. In simple terms, a graph consists of **nodes (vertices)** and **edges (links)**. On social platforms, users can be nodes, and friendships, follows, likes, comments, shares, and message links can be edges.

Graphs are foundational for:
- friend/follow recommendations,
- feed ranking,
- community detection,
- spam/fraud detection,
- content propagation analysis,
- and social network modeling.

These uses align with standard graph concepts discussed in computer networks, distributed systems, and data mining literature, where graph-based models are central to representing connected systems and extracting patterns from them [1][2][3].

## Types of Graphs Used in Social Media

### 1. Social Network Graphs
The most common graph in social media is the **social graph**:
- **Nodes:** users, pages, accounts
- **Edges:** relationships such as follow, friend, subscribe, block

Examples:
- Facebook-style friendship graph
- Instagram/Twitter/X follower graph
- LinkedIn professional connection graph

### 2. Interaction Graphs
These graphs model how users engage with content:
- **Nodes:** users, posts, videos, hashtags
- **Edges:** likes, comments, shares, retweets, mentions

These graphs help platforms understand engagement patterns and virality.

### 3. Bipartite Graphs
A bipartite graph has two different node sets with edges only across sets.

Examples:
- users ↔ posts
- users ↔ hashtags
- users ↔ groups

These are useful for recommendation systems and content discovery [2].

### 4. Directed Graphs
Most social media graphs are **directed**:
- A follows B does not necessarily mean B follows A.
- A mentions B creates a directional edge.

This matters for influence modeling and feed generation.

### 5. Weighted Graphs
Edges may carry weights to indicate:
- frequency of interaction,
- strength of relationship,
- recency of engagement,
- trust or relevance score.

Weighted graphs improve recommendation quality and ranking [2].

### 6. Dynamic Graphs
Social media graphs change continuously as users:
- follow/unfollow,
- post,
- like,
- comment,
- join/leave communities.

This makes them **dynamic graphs**, which require continuous updating and scalable processing [3].

## How Social Media Platforms Use Graphs

### 1. Friend and Follower Recommendations
Platforms use graph structure to suggest connections:
- mutual friends,
- common interests,
- shared communities,
- second- and third-degree links.

This is typically driven by graph traversal and link prediction methods [2].

### 2. News Feed and Content Ranking
Graphs help rank content by analyzing:
- who posted it,
- who interacted with it,
- how closely related the user is to the content’s spreaders.

The stronger the graph proximity or interaction history, the more likely content appears in the feed.

### 3. Community Detection
Platforms identify groups of users with dense connections:
- fandoms,
- local communities,
- interest clusters,
- professional circles.

Community detection is a standard graph mining task [2].

### 4. Viral Content Tracking
Graph propagation models track how content spreads from node to node:
- original poster → followers → reshares → wider audience

This is useful for:
- trend detection,
- influencer analysis,
- marketing analytics.

### 5. Fraud, Spam, and Bot Detection
Graph anomalies can reveal suspicious behavior:
- many accounts connected in unnatural patterns,
- dense clusters of fake interactions,
- repetitive bot-driven sharing.

Graph-based anomaly detection is widely used in data mining [2].

### 6. Search and Discovery
Graphs improve search by linking:
- topics,
- hashtags,
- accounts,
- pages,
- related content.

This supports “people you may know,” “topics to follow,” and “related videos/posts.”

## Common Graph Algorithms and Analytics

### 1. BFS and DFS
Used to traverse connections and explore neighborhoods in the network.

### 2. Shortest Path Algorithms
Help determine:
- degrees of separation,
- connection distance,
- routing through social ties.

### 3. Centrality Measures
Used to identify influential nodes:
- **Degree centrality**: number of connections
- **Betweenness centrality**: bridge nodes
- **Eigenvector/PageRank-like measures**: influence through influential neighbors

These are especially important for influencer ranking and network analysis [2].

### 4. Link Prediction
Predicts likely future connections based on:
- shared neighbors,
- interaction history,
- graph embeddings,
- node similarity.

### 5. Community Detection Algorithms
Examples include modularity-based clustering and label propagation.

### 6. Graph Embeddings
Convert graph nodes into vectors for machine learning:
- recommendation,
- classification,
- anomaly detection.

Graph-based machine learning is an active area connected to modern data mining approaches [2][5].

## Platform Examples

### Facebook
- Core **social graph** of friendships and follows.
- Uses graph data for friend suggestions, feed ranking, and community detection.

### Instagram
- Uses follower and engagement graphs.
- Recommendation systems rely on user-content interaction graphs.

### X (Twitter)
- Strong directed follower graph.
- Retweet/mention graphs help identify trends and influence.

### LinkedIn
- Professional connection graph.
- Strong use of graph traversal for job and contact recommendations.

### TikTok / YouTube
- User-content interaction graphs are critical.
- Recommendation systems depend heavily on graph-based relationship modeling between users, videos, and engagement patterns.

## Technical and Design Considerations

### Scalability
Social graphs can contain billions of nodes and edges, so platforms need:
- distributed storage,
- graph partitioning,
- caching,
- incremental updates.

Distributed systems principles are important here because graph computations must scale across machines [3].

### Real-Time Processing
Feeds, recommendations, and spam detection often require near-real-time updates.

### Privacy and Access Control
Not all graph relationships should be visible or exposed.
Platforms must protect:
- private connections,
- hidden interactions,
- sensitive network patterns.

### Data Quality
Graphs can be noisy due to:
- fake accounts,
- duplicate profiles,
- sparse interactions,
- missing metadata.

Good graph analytics depends on clean and reliable data.

## Conclusion

Graphs are one of the most important underlying structures in social media platforms. They model relationships among users, content, and interactions, enabling recommendations, feed ranking, community detection, virality analysis, and fraud detection. Social media systems rely on directed, weighted, dynamic, and bipartite graphs, along with graph algorithms and machine learning methods, to operate at scale and personalize user experiences. In practice, graph-based thinking is central to how modern social platforms are built and optimized [1][2][3][5].

## Sources

1. **Tanenbaum - Computer Networks** — local://books/tanenbaum_computer_networks.pdf  
2. **data mining** — local://books/data_mining.pdf  
3. **Tanenbaum - Distributed Systems** — local://books/tanenbaum_distributed_systems.pdf  
4. **Tanenbaum - Modern Operating Systems** — local://books/tanenbaum_modern_os.pdf  
5. **math behind ml** — local://books/math_behind_machine_learning.pdf