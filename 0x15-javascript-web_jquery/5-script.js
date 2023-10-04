const $ = window.$;

$('div#add_item').click(function () {
  const item = $('<li>Item</li>');
  $('ul.my_list').append(item);
});
