var input = document.getElementById("id_imagem");
const modal_img = document.getElementById("modal_img");
const myModal = new bootstrap.Modal(document.getElementById('modal_crop'), {
  keyboard: false
})
const botao_crop = document.getElementById("botao-crop");

var final_img;
const confirm_btn = document.getElementById("confirmBtn");
const csrf = document.getElementsByName("csrfmiddlewaretoken");
const form = document.getElementById("main_form");
const container = document.getElementById("div-form");

input.addEventListener("change", function(){
  console.log(input.files[0])
  const img_data = input.files[0];
  const img_url = URL.createObjectURL(img_data);
  modal_img.src = img_url
  myModal.show();
  var $image = $('#modal_img');
  myModal.handleUpdate();
  $image.cropper({
    minContainerWidth: 700,
    minContainerHeight: 450,
    responsive: true,
    aspectRatio: 224 / 168,
    crop: function(event) {
      console.log(event.detail.x);
      console.log(event.detail.y);
      console.log(event.detail.width);
      console.log(event.detail.height);
      console.log(event.detail.rotate);
      console.log(event.detail.scaleX);
      console.log(event.detail.scaleY);
    }
  });
  
  // Get the Cropper.js instance after initialized
  var cropper = $image.data('cropper');

  botao_crop.addEventListener('click', () =>{
    cropper.getCroppedCanvas().toBlob((blob) =>{
      confirm_btn.classList.remove("disabled");
      console.log(confirm_btn.classList)
      myModal.hide();
      var file = blob;

      confirm_btn.addEventListener('click', () =>{
        var fd = new FormData();
        var fd_antigo = new FormData(form);
        fd.append("csrfmiddlewaretoken", fd_antigo.get("csrfmiddlewaretoken"));
        fd.append("nome", fd_antigo.get("nome"));
        fd.append("descricao", fd_antigo.get("descricao"));
        fd.append("tipo", fd_antigo.get("tipo"));
        fd.append("imagem", file, 'imagem-cortada.png');
        console.log("oi", form.action);
      
        $.ajax({
          type: 'POST',
          url: form.action,
          enctype: 'multipart/form-data',
          data: fd,
          success: function(response){
            console.log(response);
            container.innerHTML = `
            <div class="alert alert-success d-flex align-items-center show fade w-100 fixed alert-ending alerta" role="alert" id="myAlert">
              <div>
                Ferramenta cadastrada com sucesso.
              </div>
            </div>
            ` + container.innerHTML;
            const alert = bootstrap.Alert.getOrCreateInstance('#myAlert');
            
            setTimeout(()=>{
              alert.close();
              location.href = "/ferramenta/" + response.id;
              }, 2000)
          },
          error: function(error){
            container.innerHTML = `
            <div class="alert alert-danger d-flex align-items-center show fade" role="alert">
              <div>
                An example success alert with an icon
              </div>
            </div>
          ` + container.innerHTML;
          },
          cache: false,
          contentType: false,
          processData: false
        })
      
      
      })
    });
  })


});
