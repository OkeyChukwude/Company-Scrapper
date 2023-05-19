// Listen for submit
document.getElementById('scrape-form').addEventListener('submit', async function(e){
  e.preventDefault();

  // Hide results
  document.getElementById('results').style.display = 'none';
  
  // Show loader
  document.getElementById('loading').style.display = 'block';

  await getCompanyInfo()

});

async function scrape(name, country, url=null) {
  console.log(name, country)
  const response = await fetch('/scrape', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({name, country, url})
  });

  const data = response.json();
  return data;
}

// Calculate Results
async function getCompanyInfo(){
  console.log('Calculating...');
  // UI Vars
  const companyName = document.getElementById('company_name').value;
  const country = document.getElementById('country').value;
  const companyUrl = document.getElementById('company_url').value;

  const resultText = document.getElementById('result_text');

  let companyInfo

  if (companyUrl === '') {
    companyInfo =  await scrape(companyName, country)
    resultText.textContent = companyInfo.data
  } else {
    companyInfo =  await scrape(companyName, country, companyUrl)
    resultText.textContent = `${companyName.value} is located in ${country.value}. It's URL is ${companyUrl.value}`
  }

  
  // Show results
  document.getElementById('results').style.display = 'block';

  // Hide loader
  document.getElementById('loading').style.display = 'none';

}

// Show Error
function showError(error){
  // Hide results
  document.getElementById('results').style.display = 'none';
  
  // Hide loader
  document.getElementById('loading').style.display = 'none';

  // Create a div
  const errorDiv = document.createElement('div');

  // Get elements
  const card = document.querySelector('.card');
  const heading = document.querySelector('.heading');

  // Add class
  errorDiv.className = 'alert alert-danger';

  // Create text node and append to div
  errorDiv.appendChild(document.createTextNode(error));

  // Insert error above heading
  card.insertBefore(errorDiv, heading);

  // Clear error after 3 seconds
  setTimeout(clearError, 3000);
}

// Clear error
function clearError(){
  document.querySelector('.alert').remove();
}