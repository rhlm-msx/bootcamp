let lambda_url = "http://localhost:8000"
cards_data = [{
    title : "Inventory",
    subtitle: "A Walmart Repo",
    feats : [
        "RestAPI",
        "AWS S3 Bucket",
        "AWS Lambda",
        "Databases",
        "Search"
    ],
    callback : ()=>{
        window.location.href = "products"
    }
},{
    title : "Document Generator",
    subtitle: "PDF",
    feats : [
        "Data Format"
    ],
    callback : (e)=>{
        window.location.href = "dsr"
    }
}, {
    title : "Look and Feel",
    subtitle: "config with JSON,YAML and XML",
    feats : [
        "Data Format"
    ],
    callback : ()=>{
        window.location.href = "format"
    }
}]


let root = document.querySelector("#root")
let cards = document.createElement("div")
root.appendChild(cards)
cards.classList.add("container-fluid", "d-flex", "flex-nowrap")
cards.style = "padding: 10px;scroll-behavior: smooth;"
cards.style="transform: translateX(80%); "
document.body.onscroll = ()=>{
    cards.style="transition: transform 1s;transform: translateX(0px);"
    cards.classList.add("overflow-auto")
    document.body.onscroll = null
}
document.body.onclick = ()=>{
    cards.style="transition: transform 1s;transform: translateX(0px);"
    cards.classList.add("overflow-auto")
    document.body.onclick = null
}
function addCard(data){    
    let id = cards.childElementCount;
    let div = document.createElement("div")
    title = data.title
    subtitle = data.subtitle
    feats = data.feats


    let u = (fts) => {
        let sp = ""
        for(let x in fts)
        sp += `<span class="list-group-item">${fts[x]}</span>`
        return sp;
    }

    div.innerHTML = ` 
        <div class="card me-3 bg-dark-subtle" style="width:18rem;border:1px solid black;border-radius: 6px;padding: 5px;min-height:25rem;">
                <div class="card-body">
                <h1 class="card-title">${title}</h1>
                <span class="badge text-bg-secondary mb-2" style="font-size: 10px">${subtitle}</span>
                <div class="list-group mb-3">
                ${u(feats)}
                </div> 
                <button id="exp_${id}" class="card-link btn text-bg-warning">Explore</button> 
                </div> 
            </div> `
    cards.appendChild(div)
    div.querySelector(`#exp_${id}`).onclick = data.callback
}

cards_data.forEach(e => {
    addCard(e)
});


