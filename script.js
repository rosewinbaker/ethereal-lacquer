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

                // Create anchor div
                let div = document.createElement('div');
                div.className = 'test';

                // Create h5 text with product name
                var h5 = document.createElement("h5");
                h5.innerHTML = data[i].name;

                // Create image of product
                var img = document.createElement("img");
                img.src = data[i].img;

                // Create link to product listing on Ethereal Lacquer website
                var a = document.createElement('a');
                a.href = data[i].href;
                if (data[i].price_sale) {
                    console.log('Sale item: ' + data[i].name + " selling for " + data[i].price_sale)
                    a.innerText = 'Purchase Link: ' + data[i].price_sale + ' (Sale Price)';
                }
                else {
                    a.innerText = 'Purchase Link: ' + data[i].price_regular;
                }
                

                // Append all the things to the page
                content.appendChild(div);
                div.appendChild(h5);
                div.appendChild(img);
                div.appendChild(document.createElement('br'));
                div.appendChild(a)


            }
            
        }
    })
        
