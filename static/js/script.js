(function () {
  // --- Validate BP and Age ---
  const sys = document.getElementById('sysBP');
  const dia = document.getElementById('diaBP');
  const age = document.getElementById('age');

  function validateBP() {
    const s = parseFloat(sys.value);
    const d = parseFloat(dia.value);

    if (!isNaN(s) && !isNaN(d) && d >= s) {
      dia.setCustomValidity('Diastolic must be less than systolic.');
    } else {
      dia.setCustomValidity('');
    }
  }

  function validateAge() {
    const value = parseFloat(age.value);
    if (isNaN(value) || value <= 0) {
      age.setCustomValidity('Please enter a valid age.');
    } else {
      age.setCustomValidity('');
    }
  }

  ['input', 'change'].forEach(ev => {
    sys.addEventListener(ev, validateBP);
    dia.addEventListener(ev, validateBP);
    age.addEventListener(ev, validateAge);
  });
})();

// --- Smooth scroll for navbar ---
document.querySelectorAll('.nav-links a').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute('href')).scrollIntoView({
      behavior: 'smooth',
    });
  });
});

// --- AJAX form submission ---
const form = document.getElementById('predict-form');
const resultContainer = document.getElementById('result-container');

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  if (!form.checkValidity()) {
    console.log('Form validation failed');
    form.reportValidity();
    return;
  }

  const formData = new FormData(form);

  try {
    const response = await fetch('/predict', {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      throw new Error(`Server responded with status: ${response.status}`);
    }

    const html = await response.text();
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    const result = doc.querySelector('.result-combined');

    if (result) {
      resultContainer.innerHTML = '';
      resultContainer.appendChild(result);
      result.scrollIntoView({ behavior: 'smooth', block: 'center' });
    } else {
      console.error('No .result-combined element found in response');
      resultContainer.innerHTML = '<p>Error: No result found. Please try again.</p>';
    }
  } catch (error) {
    console.error('Submission error:', error);
    resultContainer.innerHTML = '<p>Error submitting form. Please try again later.</p>';
  }
});

// --- Cigarettes per Day toggle ---
document.addEventListener("DOMContentLoaded", function () {
  const radios = document.querySelectorAll('input[name="is_smoking"]');
  const cigs = document.getElementById("cigsPerDay");

  function toggleCigs() {
    const val = document.querySelector('input[name="is_smoking"]:checked');
    if (val && val.value === "0") {
      // No → auto 0 and lock
      cigs.value = "0";
      cigs.disabled = true;
    } else if (val && val.value === "1") {
      // Yes → clear if 0 and unlock
      if (cigs.value === "0") cigs.value = "";
      cigs.disabled = false;
    } else {
      // Nothing selected → keep blank editable
      cigs.value = "";
      cigs.disabled = false;
    }
  }

  radios.forEach(r => r.addEventListener("change", toggleCigs));
  toggleCigs(); // Run once on load
});

