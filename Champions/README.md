# 🧠 Champion | Customer Segmentation & CLV Optimization Strategy

## Executive Summary

This project delivers a strategic customer segmentation and **Customer Lifetime Value (CLV)** optimization framework for **Champion**, a leading global apparel brand. Leveraging RFM (Recency, Frequency, Monetary) modeling and predictive analytics within **SAS Studio**, we developed a four-tier segmentation model that informs **personalized marketing strategies**, **retention programs**, and **budget allocation**.

---

## 🏢 Business Challenge

Champion is witnessing post-pandemic sales growth and global market expansion. However, the brand needs a data-driven strategy to:

- Identify and reward high-value customers
- Re-engage lapsed and low-value segments
- Personalize digital engagement
- Optimize marketing ROI across customer segments

The solution: **A scalable segmentation and CLV framework that transforms transactional data into actionable marketing insights.**

---

## 🎯 Marketing & CRM Objectives

| Objective | Strategic Implication |
|----------|-----------------------|
| **Recognize & reward top customers** | Increase retention and maximize value from high CLV segments |
| **Grow mid-tier engagement** | Nurture frequent buyers with personalized campaigns |
| **Reactivate churned customers** | Win back lapsed customers through targeted offers |
| **Enhance brand engagement** | Use segmentation to drive product discovery and category expansion |
| **Optimize marketing investment** | Allocate resources based on CLV and retention potential |

---

## 🔍 Analytical Methodology

### Phase 1: Data Preparation & RFM Scoring (SAS Studio)

We utilized **SAS Studio** for data cleaning, ranking, and scoring customers across three RFM dimensions:

- **Recency (R)**: Days since last purchase
- **Frequency (F)**: Number of transactions in past 12 months
- **Monetary (M)**: Total revenue per customer over 12 months

Each customer was scored and categorized into binary classes (High = 1, Low = 0) to generate a `combined_RFM` identifier (e.g., `011`, `100`, etc.).

### Phase 2: Segment Assignment (SAS Logic)

Based on RFM combinations, we mapped each customer into one of **four strategic segments**:

```sas
#if combined_RFM in ('011') then segment_assignment = '1. Elite Patrons';
#if combined_RFM in ('010', '111') then segment_assignment = '2. Dedicated Patrons';
#if combined_RFM in ('000','001') then segment_assignment = '3. Prospective Patrons';
#if combined_RFM in ('100','101','110') then segment_assignment = '4. Lost Patrons';

## 📐 Phase 3: Customer Lifetime Value (CLV) Estimation

Using contribution margins and retention rate estimates, we applied the following CLV formula:
CLV = Margin × [ (1 + Discount Rate) / (1 + Discount Rate - Retention Rate) ]

> The discount rate was standardized across segments to ensure fair comparison.

---

## 🧮 Phase 4: Segment Profiling & Strategic Interpretation

Each segment was profiled based on:

- Purchase behavior (Recency, Frequency, Monetary)
- Product category preferences
- Responsiveness to promotions
- Retention rates
- Customer Lifetime Value (CLV) and projected purchasing lifespan

---

## 🧩 Key Segments & Strategic Insights

| Segment             | % of Customers | Avg CLV | Description                                                                  |
|---------------------|----------------|---------|------------------------------------------------------------------------------|
| **Elite Patrons**    | 13%            | $426    | High-frequency, high-spend, brand-loyal customers. Core revenue drivers.     |
| **Dedicated Patrons**| 10%            | $248    | Loyal but moderate spenders. High potential for upselling.                   |
| **Prospective Patrons**| 37%         | $68     | New or lightly engaged customers. Opportunity for conversion.                |
| **Lost Patrons**     | 40%            | $45     | Lapsed or disengaged. Candidates for win-back campaigns.                     |

---

## 🧬 Segment Behavioral Profiles

| Metric                     | Elite | Dedicated | Prospective | Lost |
|----------------------------|-------|-----------|-------------|------|
| **Recency (days)**         | 69    | 250       | 84          | 263  |
| **Frequency (purchases)**  | 4.4   | 3.5       | 1.4         | 1.4  |
| **Monetary ($/year)**      | 258   | 235       | 75          | 68   |
| **Avg Order Size ($)**     | 60    | 60        | 51          | 48   |
| **Promo Usage (%)**        | 93%   | 90%       | 32%         | 34%  |
| **Retention Rate (%)**     | 82%   | 66%       | 59%         | 40%  |

---

## 💡 Strategic Recommendations

### **Segment 1: Elite Patrons**
**Goal:** Maximize loyalty & customer value  
**Tactics:**
- Launch **VIP programs** or **exclusive early-access events**
- Offer **personalized shopping experiences**
- Involve them in **beta launches** and **feedback loops**

---

### **Segment 2: Dedicated Patrons**
**Goal:** Upsell and increase frequency  
**Tactics:**
- Implement **AI-driven cross-sell** (e.g., *"Complete the Look"*)
- Offer **bundled promotions** and **loyalty tiers**
- Use **post-purchase dynamic emails** for personalized offers

---

### **Segment 3: Prospective Patrons**
**Goal:** Convert and nurture  
**Tactics:**
- Introduce **welcome offers** or **“Starter Packs”**
- Deliver **educational content** via email and social media
- Retarget using **browsing and interaction behavior**

---

### **Segment 4: Lost Patrons**
**Goal:** Reactivate or learn from churn  
**Tactics:**
- Launch **“We Miss You”** campaigns with time-limited offers
- Include **personalized product suggestions**
- Run **exit surveys** for churn insight and future improvement

---

## 💰 Budget Allocation Strategy

| Segment             | Avg CLV | % of Customers | Budget Allocation (%) | Rationale                                                              |
|---------------------|---------|----------------|------------------------|------------------------------------------------------------------------|
| **Elite Patrons**    | $426    | 13%            | 15%                    | High ROI from loyalty and retention investments                        |
| **Dedicated Patrons**| $248    | 10%            | 30%                    | Potential for frequency and value growth through upselling             |
| **Prospective Patrons**| $68  | 37%            | 20%                    | Acquisition-focused spend to grow their lifetime value                 |
| **Lost Patrons**     | $45     | 40%            | 35%                    | Reactivation efforts and churn analysis for CX improvements            |

---

## 📊 Tools & Technologies

| Tool                      | Purpose                                                 |
|---------------------------|---------------------------------------------------------|
| **SAS Studio**            | Data processing, RFM scoring, segment assignment         |
| **Excel / PowerPoint**    | Data visualization, reporting, business storytelling     |
| **Email CRM (Suggested)** | Campaign automation (e.g., Mailchimp, Salesforce)       |
| **AI Recommender Engine** | Dynamic cross-selling and personalized experiences      |

---

> _Strategic segmentation empowers personalized growth. Align data with action to elevate your brand’s value._





