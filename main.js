'use strict';

$(function () {
  $('div#selector input[type="checkbox"]').on('click', function() {
    update ();
  });
});

function update () {
  const tags = $('div#selector input:checkbox:checked').map(function() { return this.id }).get();
  console.log(tags);

  $('div#projects > div').each(function () {
    if ($(this).data('tags').split(' ').some(x => tags.includes(x)))
    $(this).slideDown(1000);
  else
    $(this).slideUp(1000);
  });
}
