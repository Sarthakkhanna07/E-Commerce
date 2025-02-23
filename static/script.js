// for making flash message duration to 5sec
document.addEventListener("DOMContentLoaded", function() {

    const timeoutDuration = 5000;

    const flashMessage = document.getElementById('flash-message');

    if (flashMessage) {
        setTimeout(() => {
            flashMessage.style.display = 'none';
        }, timeoutDuration);
    }
});
