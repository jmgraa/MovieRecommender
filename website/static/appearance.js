let suggestions = [];

function fetchAndStoreSuggestions() {
  fetch('http://127.0.0.1:5000/static/resources/suggestions.json')
    .then(response => response.json())
    .then(data => {
      suggestions = data.suggestions;
    })
    .catch(error => {
      console.error('Error fetching JSON file:', error);
    });
}
document.addEventListener('DOMContentLoaded', fetchAndStoreSuggestions);

function showSuggestions() {
  const input = document.getElementById("title").value.trim().toLowerCase();
  const suggestionsDiv = document.getElementById("suggestions");

  if (input === "") {
    suggestionsDiv.style.display = "none";
    return;
  }

  const filteredSuggestions = suggestions.filter(title => title.toLowerCase().startsWith(input));
  const suggestionsList = document.createElement("ul");
  suggestionsList.innerHTML = "";

  filteredSuggestions.forEach(title => {
    const li = document.createElement("li");
    li.textContent = title;
    li.onclick = function() {
      document.getElementById("title").value = title;
      suggestionsDiv.style.display = "none";
    };
    suggestionsList.appendChild(li);
  });

  suggestionsDiv.innerHTML = "";
  suggestionsDiv.appendChild(suggestionsList);
  suggestionsDiv.style.display = "block";
}
document.getElementById("title").addEventListener("input", showSuggestions);

function closePopup() {
  document.getElementById('popup-container').style.display = 'none';
}