const $ = window.$;

$(document).ready(function () {
  $('div#add_item').click(function () {
    const items = $('<li>Item</li>');
    $('ul.my_list').append(items);
  });
  $('div#remove_item').click(function () {
    $('ul.my_list li:last').remove();
  });
  $('DIV#clear_list').click(function () {
    $('ul.my_list li').remove();
  });
});
