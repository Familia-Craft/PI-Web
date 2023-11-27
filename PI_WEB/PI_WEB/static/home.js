const load_box = document.getElementById("load-box");
const data_box = document.getElementById("data-box");
const filtro  = document.getElementById("filtro");
const confirm_btn = document.getElementById("confirm-btn");
const form = document.getElementsByTagName("form")[0];


$.ajax({
    type: 'GET',
    url:  '/get-ferramentas',
    success: function(response){
        setTimeout(() =>{
            console.log("Deu bom.")
            load_box.classList.add("not-visible")
            let ferramentas = response.ferramentas
            for (const f of ferramentas) {
                data_box.innerHTML += `
                <div class="col">
                    <a href="/ferramenta/${f.id}">
                        <div class="card my-3 me-3 bg-body-secondary border border-success-subtle sombra" style="width: 18rem;">
                            <img class='card-img-top' src="${f.img_url}">
                            <div class="card-body">
                                <p class="card-title">${f.nome}</p>
                                
                            </div>
                        </div>
                    </a>
                </div>`
            }

        }, 500)

    },
    error: function(error){
        console.log(error);
    }
});

const csrf = document.getElementsByName("csrfmiddlewaretoken")[0];


confirm_btn.addEventListener('click', () =>{
    load_box.classList.remove("not-visible")
    data_box.innerHTML = "";
    fd = new FormData(form);
    
    $.ajax({
        type: 'POST',
        contentType: false,
        processData: false,
        url:  '/get-ferramentas',
        data: fd,
        success: function(response){
            setTimeout(() =>{
                console.log("Deu bom.")
                load_box.classList.add("not-visible");
                let ferramentas = response.ferramentas
                for (const f of ferramentas) {
                    data_box.innerHTML += `
                    <div class="col">
                        <a href="/ferramenta/${f.id}">
                            <div class="card my-3 me-3 bg-body-secondary border border-success-subtle sombra" style="width: 18rem;">
                                <img class='card-img-top' src="${f.img_url}">
                                <div class="card-body">
                                    <p class="card-title">${f.nome}</p>
                                </div>
                            </div>
                        </a>
                    </div>`
                        }
    
                    }, 500)
                },
                error: function(error){
                    console.log(error);
                }
            });
        })
filtro.addEventListener('change', () =>{
    load_box.classList.remove("not-visible")
    data_box.innerHTML = "";
    fd = new FormData(form);
    
    $.ajax({
        type: 'POST',
        contentType: false,
        processData: false,
        url:  '/get-ferramentas',
        data: fd,
        success: function(response){
            setTimeout(() =>{
                console.log("Deu bom.")
                load_box.classList.add("not-visible");
                let ferramentas = response.ferramentas
                for (const f of ferramentas) {
                    data_box.innerHTML += `
                    <div class="col">
                        <a href="/ferramenta/${f.id}">
                            <div class="card my-3 me-3 bg-body-secondary border border-success-subtle sombra" style="width: 18rem;">
                                <img class='card-img-top' src="${f.img_url}">
                                <div class="card-body">
                                    <p class="card-title">${f.nome}</p>
                                </div>
                            </div>
                        </a>
                    </div>`
                }
                
            }, 500)
    },
    error: function(error){
        console.log(error);
    }
    });
})