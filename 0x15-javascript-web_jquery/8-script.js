// Javascript script that fetches and lists all movies title by using this
// URL: https://swapi-api.hbtn.io/api/films/?format=json
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (film of data['results']) {
    $('#list_movies').append('<li>' + film['title'] + '</li>');
  }
});
