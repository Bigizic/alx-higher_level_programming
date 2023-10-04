const $ = window.$;
$('div#toggle_header').click(function () {
  if ($('header').hasClass('green')) {
    $('header').removeClass('green').addClass('red');
  } else { $('header').removeClass('red').addClass('green'); }
});
