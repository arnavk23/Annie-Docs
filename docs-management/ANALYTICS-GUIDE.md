# Analytics, Feedback, and User Insights Guide

This guide explains how analytics and user feedback are integrated into the documentation, and how to use the collected data to improve docs quality.

## Analytics Integration
- **Plausible Analytics** is used for privacy-friendly tracking.
- The script is loaded via `docs/assets/analytics.js` (see mkdocs.yml `extra_javascript`).
- Tracks page views, search queries, page ratings, and feedback submissions.

## Page Rating and Feedback
- Every page includes a “Was this helpful?” widget and a feedback form.
- Ratings and feedback are sent as custom events to Plausible.

## Search Analytics
- All search queries are tracked as custom events.
- Use Plausible’s dashboard to identify popular searches and content gaps.

## Usage Dashboards
- Visit your Plausible dashboard to view:
  - Most/least popular pages
  - Search analytics
  - Feedback and ratings
  - User journeys (paths through docs)

## A/B Testing
- Use Plausible’s [Experiments](https://plausible.io/docs/experiments) or PostHog for A/B tests.
- Example: Test different doc layouts or headlines.

## User Journey Tracking
- Plausible’s “Paths” feature shows which pages lead to success (e.g., API usage, downloads).
- Use custom events for key actions (e.g., clicking code copy, completing a tutorial).

## Effectiveness Metrics
- Track:
  - Page helpfulness ratings
  - Feedback volume and sentiment
  - Search success/failure rates
  - Time on page and bounce rates

## Privacy
- No personal data is collected.
- All analytics are anonymous and GDPR-compliant.

---

For setup or dashboard access, contact the project maintainer.
