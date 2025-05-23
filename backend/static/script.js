document.getElementById('upload-form').addEventListener('submit', async function(e) {
    e.preventDefault();
  
    const fileInput = document.getElementById('csv-file');
    const outputDiv = document.getElementById('output');
    const resultSection = document.getElementById('result-section');
  
    if (!fileInput.files.length) {
      alert('Please upload a CSV file.');
      return;
    }
  
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
  
    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        body: formData,
      });
  
      const data = await response.json();
  
      if (data.error) {
        outputDiv.textContent = `⚠️ Error: ${data.error}`;
      } else {
        outputDiv.textContent = JSON.stringify(data.output, null, 2);
      }
      if (data.plot) {
        const img = document.getElementById('plot-img');
        img.src = `http://localhost:5000${data.plot}?t=${Date.now()}`; // Cache-busting
        img.style.display = 'block';
      }
    
    resultSection.style.display = 'block';

    } catch (err) {
      outputDiv.textContent = `❌ Failed to connect to the backend.`;
      resultSection.style.display = 'block';
    }
  });
  