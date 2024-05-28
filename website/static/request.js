document.getElementById('recommendationForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const title = document.getElementById('title').value.trim();
    if (!title) return;

    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://127.0.0.1:5000/recommendations?title=' + encodeURIComponent(title), true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            const recommendations = JSON.parse(xhr.responseText);
            const recommendationsDiv = document.getElementById('recommendations');
            let htmlToAppend = '<div class="row">';
            const titles = recommendations['titles']
            for (const movieTitle in titles) {
                const movieData = titles[movieTitle];
                const posterUrl = movieData.poster_url;
                const movieLink = movieData.movie_link;
                htmlToAppend += '<div class="column">';
                htmlToAppend += '<a href="' + movieLink + '" target="_blank">';
                htmlToAppend += '<img class="image" src="' + posterUrl + '" alt="' + movieTitle + '">';
                htmlToAppend += '<div class="text">' + movieTitle + '</div>';
                htmlToAppend += '</a>';
                htmlToAppend += '</div>';
            }
            htmlToAppend += '</div>';
            console.log(recommendations['repetitive']);
            if (recommendations['repetitive'] === 1)
                recommendationsDiv.innerHTML = htmlToAppend;
            else
                recommendationsDiv.innerHTML += htmlToAppend;
        } else if (xhr.status === 404) {
            document.getElementById('popup-container').style.display = 'block';
        } else {
            console.error('Request failed. Status: ' + xhr.status);
        }
    };
    xhr.onerror = function() {
        console.error('Request failed. Network error.');
    };
    xhr.send();
});