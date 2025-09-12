let root = document.querySelector("#inventory")

let entity_cards = []
let cat_prod = {
    "stocked": "red",
    "rollback" : "orange",
    "clearance": "green",
    "reduced price": "blue"
}


function addBadge(val, classes = [], prefix = ""){
    if(val != "-1")
    return `<span class="badge text-bg-secondary ${classes.join(" ")}">${prefix}${val}</span>`
    return ""
}

function addEntity(obj){
let card = document.createElement("div")
card.classList.add("card")
card.style = style="min-width: 15rem;width: 15rem;min-height: 20rem;"
let col = cat_prod[obj.status.toLowerCase()]
card.innerHTML = `
    <div class="fw-bolder card-header text-bg-danger text-center" style="background-color: ${col} !important">
    ${obj.status}
    </div>
    <img class="card-img-top w-100 justify-content-center align-items-center d-flex" src="/assets/image/${obj.id}">
    <div class="card-body">
        <h4 class="card-title lh-1">
        ${obj.name}
        </h4>
        <div>
        ${addBadge(obj.price, ["fs-5"])}
        ${addBadge(obj.old_price, ["text-bg-danger", "text-decoration-line-through"])}
        ${addBadge(obj.shipping, ["text-bg-primary"], prefix='<i class="bi bi-truck"></i>')}
        ${addBadge(obj.rate, ["text-bg-secondary"])}
        ${addBadge(obj.opts, ["text-bg-warning"])}
        </div>
        <p card="card-text">Description</p>
        <button class="btn btn-primary">Explore</button>
    </div>
`
root.appendChild(card)
card.querySelector("img").onload = (e)=>{
fetch("/utils/colors/" + obj.id).then(res => {

   res.json().then(res => {
    let color1 = res["colors"]["color2"];
    let color2 = res["colors"]["color7"];
    let colors = res["colors"]
    let u = Object.values(colors).slice(3, 8).join(",")
    card.style.background= `linear-gradient(10deg, ${u})`
   })

})
}
entity_cards.push(card)
}

fetch("/inventory/listing").then(res => {
    res.json().then(res =>{
        res.forEach(data => {
            addEntity(data)
        });
    })
})

