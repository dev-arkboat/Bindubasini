document.addEventListener('DOMContentLoaded', function () {
    var brandText = document.querySelector('.brand-text');
    if (brandText) {
        brandText.style.fontFamily = "'Playfair Display', serif";
        brandText.style.fontWeight = '700';
    }

    var loginLogo = document.querySelector('.login-logo');
    if (loginLogo) {
        loginLogo.style.fontFamily = "'Playfair Display', serif";
        loginLogo.style.fontWeight = '700';
        loginLogo.style.background = 'linear-gradient(135deg, #C9A84C, #9E8232)';
        loginLogo.style.webkitBackgroundClip = 'text';
        loginLogo.style.webkitTextFillColor = 'transparent';
    }
});
