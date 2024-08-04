function validateSearchForm() {
  var query = document.getElementById('searchInput').value.trim();
  if (query === '') {
    document.getElementById('searchInput').value = '';
    document.getElementById('searchInput').focus();
    return false;
  }
  return true;
}
