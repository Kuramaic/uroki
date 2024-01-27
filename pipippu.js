const titleDOM = document.getElementById('title');
const descriptionDOM = document.getElementById('description');
const buttonAdd = document.getElementById('add');
const listDOM = document.getElementById('list');
const formDOM = document.getElementById('form');

let items = []

function generateHtml(object){
    const text = `<div class="item-title">${ item.title }</div>
                      <div class="item-description">${ item.description }</div>`;
    const newDiv = document.createElement('div');
    newDiv.innerHTML = text;
    newDiv.classList.add('item');
    listDOM.appendChild(newDiv);
}



if (titleDOM && descriptionDOM && buttonAdd && listDOM) {
    items=localStorage.getItem('items')
    items=JSON.parse(items)
    if(!items){
        items=[]
    }
    for (const item of items) {
        generateHtml(item)
    }
    buttonAdd.addEventListener('click', function(event) {
        const title = titleDOM.value;
        const description = descriptionDOM.value;

        if (!title) {
            alert('Необходимо указать заголовок');
            return;
        }

        if (!description) {
            alert('Необходимо указать описание');
            return;
        }

        const text = `<div class="item-title">${ title }</div>
                      <div class="item-description">${ description }</div>`;
        const newDiv = document.createElement('div');
        newDiv.innerHTML = text;
        newDiv.classList.add('item');
        listDOM.appendChild(newDiv);


        const object={ title, description }
        items.push(object)
        localStorage.setItem('items',JSON.stringify(items))

        // titleDOM.value = '';
        // descriptionDOM.value = '';
        formDOM.reset();
    });
}
else {
    console.error('Нет какого-то элемента');
}
















const titleDOM= document.getElementById('title')
const categoryDOM= document.getElementById('category')
const priceDOM= document.getElementById('price')
const countDOM= document.getElementById('count')
const discountYesDOM= document.getElementById('discountYes')
const discountNoDOM= document.getElementById('discountNo')
const speciality1DOM= document.getElementById('speciality1')
const speciality2DOM= document.getElementById('speciality2')
const descriptionDOM= document.getElementById('description')
const buttonAdd= document.getElementById('button')
const discountsDOM=document.getElementById('discounts')
const discountDom= document.getElementById('discount')
const listDom=document.getElementById('list')
const zena_discountDom=document.getElementById('zena-discount')
const zena_defaultDom=document.getElementById('zena-default')
const formaDom =document.getElementsByClassName('forma')
// const deleteDom =document.getElementById('delete')

let items=[]

function deleteCard(index) {
    items.splice(index, 1)
    listDom.innerHTML = ''
    for (const index in items) {
        generateHtml(items[index], index)
    }
    localStorage.setItem('items',JSON.stringify(items))
}

function generateHtml(object, index){
    let text=`
        <h2>${object.title}</h2>
        <div><i>${object.category}</i></div>
         <div>${object.description}</div>
         <div>${object.speciality1} ${object.speciality2}</div>
         `
    if (discont) {
        text += `
         <div class="zena-discount">
             <div>Цена:<s>${object.price}</s> <i>${eval(object.price-((object.price)*(object.discount))/100)}</i></div>
             <div>Количество:${object.count}</div>
         </div>`
    }
    else {
        text += `
        <div class="zena-default">
             <div>Цена:${object.price}</div>
             <div>Количество:${object.count}</div>
        </div>
        `
    }
    text +=`<button id="delete" onclick="deleteCard(${index})">DELETE</button>`
    const newDiv=document.createElement('div')
    newDiv.innerHTML=text
    newDiv.classList.add('item');
    listDom.appendChild(newDiv)
}

let discont = false


if (titleDOM&&categoryDOM&&priceDOM&&listDom&&countDOM&&discountsDOM&&discountYesDOM&&discountNoDOM&&speciality1DOM&&speciality2DOM&&descriptionDOM&&buttonAdd){
    // выгрузка из памяти
    items=localStorage.getItem('items')
    items=JSON.parse(items)
    if(!items){
        items=[]
    }
    for (const index in items) {
        generateHtml(items[index], index)
    }


    // проверка наличия скидки
    discountYesDOM.addEventListener('click',function (){
        discountsDOM.style.display='block'
        discont=true
    })
    discountNoDOM.addEventListener('click',function (){
        discountsDOM.style.display='none'
        discont=false
    })

    buttonAdd.addEventListener('click',function (){
        const title=titleDOM.value
        const category=categoryDOM.value
        const price=priceDOM.value
        const count=countDOM.value
        let discount;
        if (discont){
            discount=discountDom.value
        }
        else {
            discount=null
        }

        let speciality1
        if (speciality1DOM.checked){
            speciality1=speciality1DOM.name
        }
        else {
            speciality1=''
        }

        let speciality2
        if (speciality2DOM.checked){
            speciality2=speciality2DOM.name
        }
        else {
            speciality2=''
        }

        const description=descriptionDOM.value
        const object={title,category,price,count,discount,speciality1,speciality2,description}

        items.push(object)
        const index = items.length - 1;

        generateHtml(object, index)


        localStorage.setItem('items',JSON.stringify(items))
    })

    formaDom.reset()
}
else{
    console.error('Нет элемента')
}




.head{
    display: flex;
    flex-direction: row;
    width: 100vw;
}
.head>div{
    display: flex;
    flex-direction: column;
    width: 35%;
    margin: 40px 50px;
}
.head>div>h3{
    text-align: center;
}
.forma>div,.forma>div>input,.forma>div>select{
    width: 100%;
}

.forma{
    line-height: 2rem;
}
#description{
    width: 100%;
    height: 125px;
}
#button{
    width: 100%;
}
#discounts{
    display: none;
}

.item{
    width: 100%;
    background-color: #e0e0e0;
    border-radius: 40px;
    padding: 20px;
    margin: 20px 0;
}
#zena-discount{
    display: flex;
    flex-direction: row;
}
#zena-default{
    display: flex;
    flex-direction: row;
}
