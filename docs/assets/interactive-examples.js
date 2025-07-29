// interactive-examples.js
// Adds Pyodide-powered code execution, copy buttons, and sliders to code blocks in the docs

// --- Pyodide Loader ---
window.pyodideReadyPromise = null;
function loadPyodideIfNeeded() {
  if (!window.pyodideReadyPromise) {
    window.pyodideReadyPromise = new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = 'https://cdn.jsdelivr.net/pyodide/v0.25.1/full/pyodide.js';
      script.onload = async () => {
        window.pyodide = await loadPyodide();
        resolve(window.pyodide);
      };
      script.onerror = reject;
      document.head.appendChild(script);
    });
  }
  return window.pyodideReadyPromise;
}

// --- Add Try It and Copy Buttons ---
function enhanceCodeBlocks() {
  document.querySelectorAll('pre code.language-python').forEach((block, idx) => {
    const pre = block.parentElement;
    // Add Try It button
    if (!pre.querySelector('.try-it-btn')) {
      const tryBtn = document.createElement('button');
      tryBtn.textContent = 'Try it';
      tryBtn.className = 'try-it-btn';
      tryBtn.onclick = async () => {
        tryBtn.disabled = true;
        tryBtn.textContent = 'Running...';
        const code = block.textContent;
        await loadPyodideIfNeeded();
        let output;
        try {
          output = await window.pyodide.runPythonAsync(code);
        } catch (e) {
          output = e.toString();
        }
        let outDiv = pre.querySelector('.pyodide-output');
        if (!outDiv) {
          outDiv = document.createElement('div');
          outDiv.className = 'pyodide-output';
          pre.appendChild(outDiv);
        }
        outDiv.textContent = output;
        tryBtn.disabled = false;
        tryBtn.textContent = 'Try it';
      };
      pre.appendChild(tryBtn);
    }
    // Add Copy button
    if (!pre.querySelector('.copy-btn')) {
      const copyBtn = document.createElement('button');
      copyBtn.textContent = 'Copy';
      copyBtn.className = 'copy-btn';
      copyBtn.onclick = () => {
        navigator.clipboard.writeText(block.textContent);
        copyBtn.textContent = 'Copied!';
        setTimeout(() => (copyBtn.textContent = 'Copy'), 1200);
      };
      pre.appendChild(copyBtn);
    }
  });
}

// --- Add Parameter Sliders for Demos ---
function addParameterSliders() {
  document.querySelectorAll('.ann-slider-demo').forEach((container) => {
    if (container.querySelector('input[type=range]')) return; // Already added
    const slider = document.createElement('input');
    slider.type = 'range';
    slider.min = 1;
    slider.max = 100;
    slider.value = 50;
    slider.oninput = function () {
      container.querySelector('.slider-value').textContent = slider.value;
      // Optionally, update a D3.js chart here
    };
    container.appendChild(slider);
    const valueSpan = document.createElement('span');
    valueSpan.className = 'slider-value';
    valueSpan.textContent = slider.value;
    container.appendChild(valueSpan);
  });
}

// --- On page load ---
document.addEventListener('DOMContentLoaded', () => {
  enhanceCodeBlocks();
  addParameterSliders();
});
