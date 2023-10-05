const $ = window.$;

$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const languageCode = $('input#language_code').val();
    const apiUrl = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;

    $.get(apiUrl, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
