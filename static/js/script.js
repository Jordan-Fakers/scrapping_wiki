const api_url = "http://localhost:5000/wiki"; 

async function getData(url){
    const response = await fetch(url);
    let data = await response.json();
    console.log(data[0]);
    return data
    }
getData(api_url)

function displayData(data){
    data.forEach(element => {
        let titres = document.querySelector('articleTitres');
        let images = document.querySelector('articleImages');
        let snippets = document.querySelector('snippets');
        let dates = document.querySelector('articleDates');
        let titre = titres.append(data[0]);
        console.log(data[0])
            titre.innerHTML +=  `<h4 class="articleTitres">${element[1]}</h4>`;
        let image = images.appendChild(data({titre:['titre']}));
            image.innerHTML += `src="${element[2]}"`;
        let snippet = snippets.appendChild(data[2]);
            snippet.innerHTML += `<p class="snippets">${element[3]}</p>`;
        let date = dates.appendChild(data[4]);
            date.innerHTML += `<p class="articleDates">${element[4]}</p>`;
    });
}