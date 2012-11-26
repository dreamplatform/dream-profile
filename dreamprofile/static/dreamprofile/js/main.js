$(document).ready(function () {

/* Option lists
======================================================== */

  $('.option-list input').on('change', function () {
    $('label[for="' + $(this).attr('id') + '"]').closest('.option-list-item').toggleClass('selected');
  });

});