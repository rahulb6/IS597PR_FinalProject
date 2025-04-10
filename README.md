# Red Bull’s Race Day Delivery for Double-Headers  
### Monte Carlo Simulation to Explore Logistics Risks in Formula 1

## Project Overview:

Formula 1 teams face a substantial logistical challenge when they have to move equipment from one race location to the next—especially during back-to-back race weekends (double-headers). With tight FIA deadlines and unpredictable issues like traffic, weather, or equipment failures, there is a lot that can go wrong.

In this project, we simulate what could happen during those race-to-race delivery windows. We model real-world delivery risks using a Monte Carlo approach to see how often things go smoothly and when and why they don’t. Our focus is on Red Bull Racing, and our goal is to better understand the impact of breakdowns, delays, and disruptions on meeting a strict 96-hour delivery deadline.


## Inputs:

These are the constants in our simulation that reflect reality as closely as possible:

- **Race Calendar:** Based on the actual 2024 F1 schedule  
- **Distances:** Calculated geodesically between tracks and from team HQ in Milton Keynes  
- **Number of Trucks:** 3 per team  
- **Air Cargo:** 1 shipment per team  
- **Delivery Deadline:** 96 hours (FIA rule for setup completion before race)



## 🎲 Variables:




---

## 🧩 Code Structure:

We’ve broken the simulation into modular functions and a class-based simulator to keep it structured and reusable:



---



## Hypotheses:


