$(document).ready(function() {
  $('.member-row').click(function() {
    window.location.href = '/members/' + $(this).data('id');
  });
});
