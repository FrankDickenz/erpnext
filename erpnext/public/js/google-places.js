(function() {
  var googleMapsScript = document.createElement('script');
  googleMapsScript.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyALQeTzcPybl49BHvmR23_cE2PsRkcG8uw&libraries=places';
  googleMapsScript.defer = true;
  document.head.appendChild(googleMapsScript);
})();