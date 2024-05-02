class livre {
    id;
    prix;
    nom;
    Editeur;
    status_de_vente;
    livre(name,edditor,price){
    this.id= window.crypto.randomUUID();
    this.prix= price,
    this.nom= name,
    this.Editeur=edditor,
    this.status_de_vente= "en vente"
    }
}

const books =[
    {
        id: window.crypto.randomUUID(),
        prix: 12.57,
        nom: "tintin",
        Editeur:"dupuis",
        status_de_vente: true
        },

    {
        id: window.crypto.randomUUID(),
        prix: 12.57,
        nom: "tintin2",
        Editeur:"dupuis",
        status_de_vente: true
    },


    {
        id: window.crypto.randomUUID(),
        prix: 12.57,
        nom: "tintin3",
        Editeur:"dupuis",
        status_de_vente: true
    }
]

const addBehaviorToBook = (book) => {
    // Ensure each book has a unique ID
    const bookId = book.id || window.crypto.randomUUID()
    $(book).attr('id', bookId)
    // ensure book has price ?
    const bookprice = book.price || 0.00
    $(book).attr('price', bookprice)

    $(book).on('dragstart', (event) => {
        event.originalEvent.dataTransfer.setData("book-id", bookId)
    })

    $(book).on('dragend', (event) => {
        event.preventDefault()
    })
    
}

const addBehaviorToPanel = (panel) => {
    $(panel).on('dragover', (event) => {
        event.preventDefault()
    })

    $(panel).on('drop', (event) => {
        event.preventDefault();
        const dragged_book_id = event.originalEvent.dataTransfer.getData("book-id");
        const book = $('#' + dragged_book_id);
        
        //prevent from droping book into book
        if (event.target.draggable==true||event.target.className!="col bg-light border rounded m-4 p-4"){
            console.log(event)
            return;
        }
        // Temporarily hide the book with fadeOut
        book.fadeOut(300, function () {
            // Move the book to the new panel
            book.appendTo($(event.target)).fadeIn(300)
        })
    })
};

function onSubmitForm(event) {
    event.preventDefault()
    const form = $(event.target)
    const name = form.find('#name').val()
    const edditor = form.find('#edditor').val()
    const price = form.find('#price').val()
    const status_vente = form.find('#vendu').prop('checked')//rend bool

    console.log({ name, edditor,price, status_vente })
    addbook(name, edditor,price,status_vente)
}

function removebook(id){
    const book=document.getElementById(id);
    book.remove();}

function addbook(name, edditor, price,status_vente="en vente") {
    let book_column;
    if (status_vente){ book_column = document.querySelector("#livres_a_vendre")}
    else{ book_column = document.querySelector("#livres_vendu")}
    const id =String(window.crypto.randomUUID());
    const new_book = document.createElement('div')
    new_book.setAttribute("class","book")
    new_book.setAttribute('id',String(id))
    new_book.setAttribute('draggable', true)
    new_book.innerHTML += `<h6>${name}</h6>`
    const content =document.createElement("div")
    content.setAttribute("class","book-body")
    content.innerHTML += `<h6>${"editeur"}</h6>`
    content.innerHTML += `<p>${edditor}</p>`
    content.innerHTML += `<h6>${"prix"}</h6>`
    content.innerHTML += `<p>${price}</p>`
    
    new_book.append(content)

    const completion_button = document.createElement('button')
    completion_button.onclick=function(){
        removebook(id)
    }
    completion_button.innerText = 'delete'
    const completion_button_td = document.createElement('td')
    completion_button_td.appendChild(completion_button,)
    new_book.appendChild(completion_button_td)
    addBehaviorToBook(new_book)
    book_column.appendChild(new_book)
    
    

}

const main = () => {
    
    books.forEach((book) => {
        addbook(book.nom,book.Editeur,book.prix,book.status_de_vente)
    });
    
    // Enable dragging for cards and apply behaviors
    $(".book").attr('draggable', true).each(function () {
        addBehaviorToBook(this)
    })
    

    // Apply behavior to panels where we can drop cards
    $(".col.bg-light.border").each(function () {
        addBehaviorToPanel(this)
    })

    const form = document.getElementById('new_book_form')
    form.addEventListener('submit', onSubmitForm)
}

$(document).ready(main)
