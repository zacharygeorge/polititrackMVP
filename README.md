# polititrackMVP
MVP news aggregator tracking 100 U.S. federal politicians with bias-aware analysis.

# MVP Scope — Polititrack

## Purpose
Create a clean, filterable, bias-aware dashboard that tracks news coverage of federal U.S. politicians using OSINT and automated aggregation, without the noise of traditional social platforms.

## Target Audience
Civic-minded users, political researchers, journalists, and students looking for a centralized place to view recent headlines tied to political figures.

## MVP Features
- Tracks news for 100 federal politicians (scalable to 600+)
- News fetched every 15 minutes via GNews API
- Stores last 30 days of headlines and metadata
- Sort/filter by politician name, position, and party
- Bias/subjectivity score displayed on each article
- Fully responsive frontend (TailwindCSS + React)
- Hosted on Vercel with Postgres (Supabase) backend

## Out of Scope (for MVP)
- User accounts / auth
- State or local politician coverage
- Full-text article scraping
- Mobile app or push notifications

## Tech Stack
- GNews API
- Supabase (PostgreSQL)
- Render (cron jobs)
- TailwindCSS + React (Vercel frontend)
- NLP libraries for bias scoring (VADER/TextBlob)

## Scalability Plan
- Backend built to expand to all 600+ federal politicians
- Bias scoring can be upgraded to ML-based models or external services
- Future versions may include state/local coverage and personalization
