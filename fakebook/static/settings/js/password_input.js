// Password visibility toggle
const togglePasswordButton = document.getElementById('toggle-password');
const passwordField = document.getElementById('new-password');

if (togglePasswordButton && passwordField) 
    togglePasswordButton.addEventListener('click', function() {
        const type = passwordField.type === 'password' ? 'text' : 'password';
        passwordField.type = type;
        togglePasswordButton.textContent = type === 'password' ? 'Show' : 'Hide';
    });
else
     console.error('Toggle password button or password field not found');
