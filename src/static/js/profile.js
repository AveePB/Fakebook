function toggleFollowers() {
    var followersList = document.getElementById('followersList');
    if (followersList.style.display === 'none' || followersList.style.display === '') {
        followersList.style.display = 'block';
    } else {
        followersList.style.display = 'none';
    }
}
