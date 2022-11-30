
$(function () {

})

/* Когда пользователь нажимает на кнопку,
переключение между скрытием и отображением раскрывающегося содержимого */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

function filterFunction() {
    var input, filter, ul, li, a, i;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    div = document.getElementById("myDropdown");
    a = div.getElementsByTagName("a");
    for (i = 0; i < a.length; i++) {
        txtValue = a[i].textContent || a[i].innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            a[i].style.display = "";
        } else {
            a[i].style.display = "none";
        }
    }
}

/*
    показать/скрыть input
*/

let dataCloseItem = document.querySelectorAll('.data__item-close');
let dataItems = document.querySelectorAll('.data__form');
let closeBtns = document.querySelectorAll('.data__item-close');

for (let i = 0; i < dataCloseItem.length; i++) {
    dataCloseItem[i].addEventListener('click', () => {
        dataItems[i].classList.toggle('is-active');
        closeBtns[i].classList.toggle('is-transform');
    });
}

/*
    кнопка бургер для sidebar
*/

let burgerBtn = document.querySelector('.burger');
let sideBar = document.querySelector('.sidebar');
let logo = document.querySelector('.logo');
let sideBarList = document.querySelector('.sidebar__list');

burgerBtn.addEventListener('click', () => {
    sideBar.classList.toggle('sidebar-is-close');
    burgerBtn.classList.toggle('burger-is-close');
    logo.classList.toggle('is-close');
    sideBarList.classList.toggle('is-close');
});

/*
    Кнопки показать/скрыть контент для менеджера и админа
*/
let showManagerBtn = document.querySelector('.btn-manager');
let showAdminBtn = document.querySelector('.btn-admin');

let managerContent = document.querySelector('.manager-item');
let adminContent = document.querySelector('.admin-item');

showManagerBtn.addEventListener('click', () => {
    showManagerBtn.classList.toggle('btn-admin-is-active');
    managerContent.classList.toggle('is-active');
});

showAdminBtn.addEventListener('click', () => {
    showAdminBtn.classList.toggle('btn-admin-is-active');
    adminContent.classList.toggle('is-active');
});

/*
    Кнопка для добавления данных
*/

let addData = document.querySelectorAll('.add-formFields');

let startId = 0;

// const labelArray = ["Введите вес", "Введите длину", "Введите ширину", "Введите высоту"];
for (let j = 0; j < addData.length; j++){
    addData[j].addEventListener('click', () => {
        console.log('add el');
    
        let newEl = document.createElement("form");
        newEl.className = "done__form data__form is-active commonForm";
        newEl.id = startId++;
    
        for (let i = 0; i < 4; i++) {
    
            let divWrapper = document.createElement("div");//создаём div-обёртку
            divWrapper.className = "divInputWrapper";
    
            let label = document.createElement("input");//создаём label c подписью для input
            label.className = "inputLabel";
            label.setAttribute('type', 'text');
            label.placeholder = 'Введите название';
    
            let newInput = document.createElement("input");//создаём input
            newInput.className = "done__input data-input";
            newInput.placeholder = "Введите данные"
    
            divWrapper.append(label);//заполняем обёртку input и lable
            divWrapper.append(newInput);
    
            newEl.prepend(divWrapper);
        }
    
        let newSendBtn = document.createElement("button");
        newSendBtn.setAttribute('type', 'submit');
        newSendBtn.className = "send-btn done__btn";
        newSendBtn.innerHTML = "Отправить";
    
        newSendBtn.addEventListener('click', (e) => {
            e.preventDefault();
        });
    
        let newCloseBtn = document.createElement("button");
        newCloseBtn.className = "commonForm-close";
        newCloseBtn.id = newEl.id;
    
        newCloseBtn.addEventListener('click', (e) => {
            e.preventDefault();
            newCloseBtn.classList.toggle('is-transform');
            newCloseBtn.parentNode.parentNode.removeChild(newCloseBtn.parentNode);
        });
    
        newEl.append(newSendBtn);
        newEl.prepend(newCloseBtn);
        addData[j].after(newEl);
    
    });
}