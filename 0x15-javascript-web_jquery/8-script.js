// Queries an API and fetches all movie titles and inserts them
// into the UL#list_movies tag

$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
  var movies = data.results;
  var list = $('#list_movies');
  for (var i = 0; i < movies.length; i++) {
    var title = movies[i].title;
    list.append('<li>' + title + '</li>');
  }
});

