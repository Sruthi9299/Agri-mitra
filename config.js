// Agri Mitra – API base URL (same origin when deployed; localhost when dev)
(function() {
  var origin = window.location.origin || '';
  var isLocal = /localhost|127\.0\.0\.1|^file:/.test(origin);
  window.API_BASE = isLocal ? 'http://localhost:5000' : '';
})();
