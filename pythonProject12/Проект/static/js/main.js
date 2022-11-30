
let flipBtn = document.querySelector('.flip-btn');
let flipContainer = document.querySelector('.flipper');
let flipArrow = document.querySelector('.flip-btn__arrow');
let mainRegistr = document.querySelector('.main__title');
let mainEntry = document.querySelector('.main__subtitle');

flipBtn.addEventListener('click', () => {
    flipContainer.classList.toggle('is-active');
    flipArrow.classList.toggle('flip-btn-is-active');
    mainRegistr.classList.toggle('title-is-active');
    mainEntry.classList.toggle('subtitle-is-active');
});

$(function(){
    $(".login-form").validate();
    $(".registr-form").validate();
});