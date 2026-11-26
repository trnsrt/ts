---
layout: book-section
kind: section
title: "Modular vs. Monolithic Blockchains – Web3 Unlocked"
heading: "Modular vs. Monolithic Blockchains"
chapter: 2
chapter_title: "Key Pillars of the Web3 Economy"
order: 203
permalink: /Web3_Unlocked/chapter-2/modular-vs-monolithic/
description: "Two competing philosophies are shaping the future of blockchain infrastructure: the monolithic and the modular approach."
---

Two competing philosophies are shaping the future of blockchain infrastructure: the monolithic and the modular approach. Let's explore what they are and, more importantly, why they matter.

## The Power of Interoperability {#the-power-of-interoperability}

Web3's biggest difference from the internet we know today is how its applications interact. In the old world—Web2—tech companies build walled gardens. They create a product, control all its components, and offer you a finished, take-it-or-leave-it package. It's convenient, but it's also limiting. You're stuck with their package deal.

Web3 shatters this model. Here, the user is in control, free to pick and choose different components to create their own experience. Because applications are built on shared, open standards, a wallet from one developer can seamlessly interact with a [marketplace from another](https://whitepaper.walletconnect.network/WalletConnect%2520Whitepaper.pdf). This creates a powerful dynamic. Developers compete on the quality of their specific component, leading to relentless innovation. Teams focus on solving one problem exceptionally well, knowing they can rely on other best-in-class solutions for the rest. This accelerates progress for everyone.

This Lego-like [interoperability](https://www.alchemy.com/overviews/modular-vs-monolithic-blockchains) is the engine of Web3. This leads to a natural question: if breaking applications into specialized pieces makes them better, can we do the same for the blockchains they run on?

At first, this might seem like an abstract, technical debate. Why should you care how the underlying blockchain is pieced together? The answer comes down to the fundamental limitations of blockchain technology. This isn't just a theoretical problem; it directly impacts the transaction fees you pay, turning an architectural debate into a very real hit to your wallet.

## The Constraints of a Blockchain {#the-constraints-of-a-blockchain}

At its core, a blockchain is a system for creating an unchangeable record of transactions.

The only way to guarantee this [immutability](https://www.geeksforgeeks.org/computer-networks/immutability-in-blockchain/) is to distribute the ledger across as many different machines in as many different locations as possible. This makes taking over the network impossible, or at least prohibitively expensive.

From a pure performance perspective, centralized systems will always be [faster](https://www.mdpi.com/2076-3417/13/1/499). They are managed from a single point. But that single point is also a single point of failure. While you can technically "bulletproof" a centralized server against digital attacks, defending it against political or social pressure is a much harder problem to solve.

Decentralization is the answer to this pressure. To achieve it, however, the system has to be accessible to as many people as possible, which means the blockchain's ledger must remain small and the hardware requirements low[^1]. If you fail at this, only those with high-capacity machines can run the system. The number of participants shrinks, the network centralizes, and the security evaporates.

This creates a core problem. The very thing a blockchain sells is its block space—that limited, secure digital territory. When demand is high, the chain doesn't simply crash[^2]. Instead, [transaction fees rise in a dynamic auction](https://trakx.io/resources/insights/ethereum-gas-fees-crypto/), pushing out those whose needs aren't urgent. While this is a logical market mechanic, persistently high fees will inevitably drive users to seek out alternatives.

### Ethereum’s Persistent Challenge {#ethereums-persistent-challenge}

There is no better case study for this dilemma than Ethereum.

During the DeFi and NFT boom of 2020-21, demand for Ethereum's block space exploded, and transaction fees skyrocketed. Users were paying hundreds of dollars for simple operations, making the network unusable for many. The development community was caught in a difficult position, without a quick fix.

The initial dream was to scale the blockchain by splitting it into parallel 'execution shards'—imagine an island for DeFi and another for NFTs, each processing its own transactions. But after realizing the immense complexity of this approach, the strategy shifted.

Instead of sharding for execution, Ethereum's developers [pivoted](https://www.alchemy.com/overviews/ethereum-scaling-solutions) to a 'rollup-centric' roadmap, choosing to 'outsource' the heavy lifting to Layer 2 systems built on top of the main chain. The concept of sharding evolved to support this: with the Dencun upgrade in early 2024, Ethereum introduced Proto-Danksharding, which creates dedicated, low-cost data space for these rollups, making them significantly cheaper and more powerful.

## Blockchain’s Four Core Tasks {#blockchains-four-core-tasks}

A blockchain may be a ledger, but it has to perform [four distinct jobs](https://goldrush.dev/guides/deep-dive-into-modular-blockchain-architecture-paradigms-layers-and-technologies/) to reliably record anything on it. Think of them as the layers of work required for every single transaction.

**Execution: The Action** This is where things happen. Execution is the act of computing a transaction—transferring an asset, swapping tokens on a decentralized exchange, or minting an NFT. Applications tell the chain what they want to do, and this layer processes that request. For most of us, this is the only part of the process we directly experience.

**Consensus: The Agreement** Once a transaction is broadcast to the network, thousands of independent machines must agree on its validity and, crucially, its order. Consensus is the process of getting the entire network to agree: "Yes, this transaction is valid, it happened in this exact sequence, and here's the resulting state of all accounts." This is the decentralized heart of the system.

**Settlement: The Finality** After the network agrees on a set of transactions, it's time to make them permanent. Settlement is the point of no return—where the results are officially committed to the blockchain's ledger. When you send money, this is the moment your balance officially decreases and the recipient's increases. The validators lock in the final state of the accounts, and from this point forward, the record cannot be altered.

**Data Availability (or Publishing):** The transaction is done, settled, and final. Now, the entire system needs to be updated. This final step involves [publishing the data](https://blog.thirdweb.com/data-availability-blockchain/) from the new block across the network. This is critical because every application and user needs to know the most current state of the ledger to build the *next* set of transactions[^3]. Without this shared public knowledge, the chain would grind to a halt.

## Monolithic vs. Modular Approaches {#monolithic-vs-modular-approaches}

This brings us to the great architectural debate in crypto: how should a blockchain perform these four essential jobs? Two distinct philosophies have emerged. The first is the **monolithic** approach, where a single chain does everything, much like Apple’s tightly integrated ecosystem. The second is the **modular** approach, where different specialized layers handle each job, similar to the more open and layered Android ecosystem.

The monolithic school is led by networks like Bitcoin and [Solana](https://crypternon.com/en/solara/).

Bitcoin chose this path out of elegant simplicity. It's, in essence, an application-specific network—built to do one thing and one thing only: process BTC transactions. Since it doesn’t support general-purpose smart contracts, it can’t serve as a platform for other applications[^4]. By deliberately keeping its scope narrow, Bitcoin sidesteps the scaling race entirely[^5].

**[Solana](https://blog.bcas.io/introduction-to-solana)** represents a far more ambitious take on the monolithic design. It *is* a generalized network that runs complex smart contracts, and it attacks the scaling problem head-on by using much larger blocks. This makes it incredibly fast, but it comes with a serious trade-off. Processing these massive blocks demands [high-performance hardware](https://hackernoon.com/what-it-takes-to-run-a-solana-validator-hardware-bandwidth-and-budget), significantly raising the cost to run a validator. This barrier to entry inevitably reduces the number of participants, creating a constant risk of centralization.

On the other side of this debate are the modular systems. You can see this philosophy in two interconnected trends.

First are the **Layer 2 rollups** built on Ethereum, which handle execution independently but rely on the main chain for security and settlement.

Second, and more recently, are dedicated modular blockchains like **Celestia**, which don't process user transactions at all but instead offer a specialized, low-cost layer for **Data Availability** that other chains can use.

The most common approach combines these, with Ethereum Layer 2s outsourcing their execution while leveraging the main chain for settlement. Let's dive into how they work.

[^1]: The size of the blockchain ledger naturally increases over time as more transactions are recorded. Developers are implementing solutions like light nodes or pruning to manage the growing size of the blockchain ledger and keep hardware requirements manageable.

[^2]: Some blockchains do halt operations occasionally, but we exclude these immature exceptions here.

[^3]: "Data publishing" (broadcasting recent transactions) is often confused with "data availability" (archiving historical data), which can be stored on fewer nodes, not all.

[^4]: The narrative that it cannot serve as a platform for other applications has been challenged. The recent development of protocols like Ordinals and [Runes](https://www.gemini.com/cryptopedia/what-are-bitcoin-runes) has enabled token and NFT-like assets directly on its ledger. This, combined with an emerging ecosystem of Bitcoin Layer 2s aimed at adding more complex functionality, shows that even Bitcoin is becoming a platform for new innovation, albeit in a different way from its peers.

[^5]: Debate continues whether Bitcoin’s simple approach is viable long-term. With mining rewards halving every four years, transaction fees must increase through added functionality (Layer 2 or DeFi) to maintain miner incentives.
