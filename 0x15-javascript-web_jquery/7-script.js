const $ = window.$;

$(document).ready(function () {
  const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

  $.get(url, function (data) {
    $('div#character').text(data.name);
  });
});
