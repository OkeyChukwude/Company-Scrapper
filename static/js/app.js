// Listen for submit
document.getElementById('scrape-form').addEventListener('submit', async function(e){
  e.preventDefault();

  // Hide results
  document.getElementById('results').style.display = 'none';
  
  // Show loader
  document.getElementById('loading').style.display = 'block';

  await getCompanyInfo()

});

// Send POST Request to search endpoint
async function scrape(name, country, url=null) {
  console.log(name, country, url)
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

// Get Result
async function getCompanyInfo(){
  // UI Vars
  const companyName = document.getElementById('company_name').value;
  const country = document.getElementById('country').value;
  const companyUrl = document.getElementById('url').value;

  const resultText = document.getElementById('result_text');

  let companyInfo

  if (companyUrl === '') {
    companyInfo = await scrape(companyName, country)
  } else {
    companyInfo =  await scrape(companyName, country, url=companyUrl)
  }

  if (companyInfo.message) {
    resultText.textContent = companyInfo.message
  } else {
    resultText.innerHTML = `<p>${companyInfo.description}</p>`
    resultText.innerHTML += `<p><strong>Keywords</strong>: ${companyInfo.keywords}</p>`

    if (companyInfo.products === 'No products') {
      resultText.innerHTML += `<p><strong>Products</strong>: ${companyInfo.products}</p>`
    } else {
      resultText.innerHTML += `<p><strong>Products</strong>: ${companyInfo.products.join(', ')}</p>`
    }

    if (companyInfo.servicess === 'No services') {
      resultText.innerHTML += `<p><strong>Services</strong>: ${companyInfo.services}</p>`
    } else {
      resultText.innerHTML += `<p><strong>Services</strong>: ${companyInfo.services.join(', ')}</p>`
    }

    resultText.innerHTML += `<p><strong>Company Clasicication</strong>: <ul>
    <li>SIC: ${companyInfo['SIC Specifications']}</li> <li>NAIC: ${companyInfo['NAIC Specifications']}</li>
    </ul></p>`
  }
  
  // Show results
  document.getElementById('results').style.display = 'block';

  // Hide loader
  document.getElementById('loading').style.display = 'none';

}
