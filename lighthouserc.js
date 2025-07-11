module.exports = {
  ci: {
    collect: {
      numberOfRuns: 3,
      staticDistDir: null, // we're testing live Netlify preview
    },
    assert: {
      assertions: {
        'categories:performance': ['error', { minScore: 0.6 }],
        'categories:accessibility': ['error', { minScore: 0.6 }],
        'categories:seo': ['error', { minScore: 0.6 }],
        'categories:best-practices': ['error', { minScore: 0.6 }],
      },
    },
    upload: {
      target: 'temporary-public-storage',
    },
  },
};
