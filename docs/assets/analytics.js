// analytics.js
// Add privacy-friendly analytics and feedback widgets

// --- Analytics Integration (Plausible example) ---
(function() {
  var d=document, s=d.createElement('script');
  s.setAttribute('defer','');
  s.setAttribute('data-domain','annie-docs.netlify.app');
  s.src='https://plausible.io/js/plausible.js';
  d.head.appendChild(s);
})();

// --- Page Rating Widget ---
function injectRatingWidget() {
  if (!document.body) return;
  var container = document.createElement('div');
  container.id = 'page-rating';
  container.innerHTML = `
    <div style="margin:2em 0 1em 0;padding:1em;border:1px solid #eee;border-radius:6px;max-width:400px;">
      <strong>Was this page helpful?</strong>
      <button onclick="window.submitPageRating('yes')" style="margin-left:1em">👍 Yes</button>
      <button onclick="window.submitPageRating('no')" style="margin-left:0.5em">👎 No</button>
      <span id="rating-thanks" style="display:none;margin-left:1em;color:green;">Thank you!</span>
    </div>
  `;
  var main = document.querySelector('main') || document.body;
  main.appendChild(container);
}
window.submitPageRating = function(rating) {
  // Send event to analytics (Plausible custom event)
  if (window.plausible) window.plausible('Page Rating', {props: {rating: rating, path: location.pathname}});
  document.getElementById('rating-thanks').style.display = '';
};

// --- Feedback Form Widget ---
function injectFeedbackForm() {
  if (!document.body) return;
  var container = document.createElement('div');
  container.id = 'page-feedback';
  container.innerHTML = `
    <form id="feedback-form" style="margin:1em 0;max-width:400px;">
      <label for="feedback-text"><strong>Suggestions for improvement?</strong></label><br>
      <textarea id="feedback-text" rows="2" style="width:100%;margin-top:0.5em;"></textarea><br>
      <button type="submit">Send Feedback</button>
      <span id="feedback-thanks" style="display:none;margin-left:1em;color:green;">Thank you!</span>
    </form>
  `;
  var main = document.querySelector('main') || document.body;
  main.appendChild(container);
  document.getElementById('feedback-form').onsubmit = function(e) {
    e.preventDefault();
    var text = document.getElementById('feedback-text').value;
    if (window.plausible && text.trim()) window.plausible('Doc Feedback', {props: {feedback: text, path: location.pathname}});
    document.getElementById('feedback-thanks').style.display = '';
    document.getElementById('feedback-text').value = '';
  };
}

// --- Search Analytics ---
function trackSearchQueries() {
  var searchInput = document.querySelector('input.md-search__input');
  if (!searchInput) return;
  searchInput.addEventListener('change', function() {
    var q = searchInput.value;
    if (window.plausible && q) window.plausible('Search', {props: {query: q}});
  });
}

// --- On page load ---
document.addEventListener('DOMContentLoaded', function() {
  injectRatingWidget();
  injectFeedbackForm();
  trackSearchQueries();
});

// --- For A/B testing and user journey tracking, see docs-management/ANALYTICS-GUIDE.md ---
