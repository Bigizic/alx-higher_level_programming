const $ = window.$;

$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

  $.get(url, function (data) {
    for (const item of data.results) {
      const listItems = $(`<li>${item.title}</li>`);
      $('ul#list_movies').append(listItems);
    }
  });
});
