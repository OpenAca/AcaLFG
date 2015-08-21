function initialize() {
  $('.autocomplete').each(function(e) {
    var autocomplete =
        new google.maps.places.Autocomplete(e, { types: ['geocode'] });
    google.maps.event.addListener(autocomplete, 'place_changed', function() {
      var place = autocomplete.getPlace();
      if (!place.geometry) {
        return;
      }
      $(e).val(place.formatted_address);
      $(e).parent().find('.latitude').val(place.geometry.location.lat());
      $(e).parent().find('.longitude').val(place.geometry.location.lng());
    });
  });
}
