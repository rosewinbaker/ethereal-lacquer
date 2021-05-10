console.log("what up")

fetch('polishes.json')
    .then(response => response.json())
    .then(data => {
        // console.log(data)

        var content = document.getElementsByClassName("polish-content")[0];

        for(var i = 0; i < data.length; i++) {
            if (data[i].status != "sold_out") {
            // if (data[i].name == "Agave") {
                console.log(data[i].name)
                let div = document.createElement('div');
                div.className = 'test';
                var h5 = document.createElement("h5");
                h5.innerHTML = data[i].name;
                var img = document.createElement("img");
                img.src = data[i].img;
                content.appendChild(div);
                div.appendChild(h5);
                div.appendChild(img)
            }
            
        }
    })
        
