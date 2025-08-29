let main =  document.querySelector("#main")
let grid = document.createElement("div")
main.classList.add("container-fluid", "text-center")
grid.classList.add("row", "row-col-2", "gap-1")
main.appendChild(grid)


card_details = {
    img_link: "logo.svg",
    title: "Main",
    text: "More Details"
}

product_nodes = []
product_data = []

function generateCard(details){
let card = document.createElement("div")
card.classList.add("card")
card.style = "width:15rem"
let img = document.createElement("img")
img.classList.add("card-img-top")
img.src = details.img_link

let card_cont = document.createElement("div")
card_cont.classList.add("card-body")

let card_title = document.createElement("h5")
card_title.classList.add("card-title", "prod-title")
card_title.innerText = details.title

let card_text = document.createElement("p")
card_text.classList.add("card-text")
card_text.innerHTML = details.text
let btn = document.createElement("button")
btn.classList.add("btn", "btn-primary")
btn.innerText = "Explore"





card.appendChild(img)
card_cont.appendChild(card_title)
card_cont.appendChild(card_text)
card.appendChild(card_cont)

card_cont.appendChild(btn)
return card
}


function split(string, dlim = " "){
    let splitted = []
    let inquote = false
    let curr = ""
    for(let i = 0; i < string.length; i++){
        let ch = string[i]
        if(ch == "\"" || ch == '\''){
            inquote = !inquote
            continue
        } 
        if (dlim == string[i] && inquote == false){
            splitted.push(curr)
            curr = ""
        }
        else{
            curr += ch
        }
    }
    return splitted
}

req = fetch("http://localhost:8000/products_csv")
req.then(res => {
    if (res.ok) {
        
        res.body.getReader().read().then(r=>{
            let data = new TextDecoder().decode(r.value)
           rows = data.split("\n").slice(1,)
           rows.forEach(row => {
                if(row.length == 0){
                    return null;
                }
                row = split(row, ",")

                let [id,name,img,status,price,opts,rate,old_price,shipping] = row
                
                let card_node = generateCard({
                    img_link: "/product_img/" + id,
                    title: name,
                    text:  ("$" + price).strike()
                })
                product_data.push({
                    id: id,
                    name: name
                })
                product_nodes.push(card_node)
                grid.append(card_node)
                
           })
        }
        )
    }else{
        console.log("Failed Fetching")
    }
})

let text_enc = new TextEncoder()
let text_dec = new TextDecoder()

function getSignature(str){
    let buffer = new Uint8Array(26)
    text_enc.encode(str).forEach(e => {
        let c = 122 - e
        if(c >= 0 && c < 26){
            buffer[c] += 1
        }
    })
    return buffer
}

function simi(sub, target){
    let sign_sub = getSignature(sub)
    let sign_tar = getSignature(target)
    let score = 0
    for(let i = 0; i < 26;i++){
        
        score += (sign_sub[i] - sign_tar[i])
    }
    return Math.abs(score)
    
}


document.querySelector("#inp").addEventListener("input", (e)=>{
    let sub = e.srcElement.value
    product_data.forEach(data => {
        if (data.name == undefined){
            return 
        }
        let target = data.name.toLowerCase()
        
        let score = simi(sub, target)
        if(score > 50){
            product_nodes[data.id].style="display: none"
        }else{

            product_nodes[data.id].style="display: flex"
        } 
    })
})
