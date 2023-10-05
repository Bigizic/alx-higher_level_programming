const $ = window.$;

$(document).ready(function () {
  function fetch () {
    const languageCode = $('input#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;

    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  }
  $(document).keypress(function (e) {
    if (e.which === 13) {
      fetch();
    }
  });
  $('INPUT#btn_translate').click(fetch);
});
