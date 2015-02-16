$(document).ready(function() {
  $('.audition-row').click(function() {
    window.location.href = '/auditions/' + $(this).data('id');
  });
});
