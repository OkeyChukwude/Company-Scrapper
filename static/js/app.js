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
    companyInfo =  await scrape(companyName, country)
  } else {
    companyInfo =  await scrape(companyName, country, url=companyUrl)
  }

  if (companyInfo.message) {
    resultText.textContent = companyInfo.message
  } else {
    resultText.innerHTML = companyInfo.description.split('Their products and services include')[0]

    resultText.innerHTML += `\nTheir products and services include:
    <ul>`

    for (let item of companyInfo['products/services']) {
      resultText.innerHTML += `<li> ${item}</li>\n`
    }

    resultText.innerHTML += '</ul>'
  }
  

  
  // Show results
  document.getElementById('results').style.display = 'block';

  // Hide loader
  document.getElementById('loading').style.display = 'none';

}
