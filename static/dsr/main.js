let inp_ele = `
    <div class="input-group mb-3">
    <div class="input-group-text">
        <input type="checkbox" class="form-check-input mt-0">
    </div>
    <textarea class="form-control" placeholder="Describe Work"></textarea>
    <button class="btn btn-secondary" >-</button>
    </div>
`

let chal_ele = `
    <div class="input-group mb-3">
    <div class="input-group-text">
        <input type="checkbox" class="form-check-input mt-0">
    </div>
    <textarea class="form-control" placeholder="Describe Challenges"></textarea>
    <button class="btn btn-secondary" >-</button>
    </div>
`

let work =  document.querySelector("#work")
let workbtn =  document.querySelector("#work-btn")
workbtn.addEventListener("click", (e)=>{

    let div = document.createElement("div")
    div.innerHTML = inp_ele
    div.querySelector("button").addEventListener("click", (k)=>{
    work.removeChild(div)
    })
    work.appendChild(div)

})

let chal =  document.querySelector("#chal")
let chalbtn =  document.querySelector("#chal-btn")
chalbtn.addEventListener("click", (e)=>{

    let div = document.createElement("div")
    div.innerHTML = chal_ele
    div.querySelector("button").addEventListener("click", (k)=>{
    chal.removeChild(div)
    })
    chal.appendChild(div)

})


let frame = document.querySelector("#pdf")

document.querySelector("#submit").addEventListener("click", e => {
    let work_in_progress = []
    let work_done = []
    let inps = document.querySelector("#work").querySelectorAll("input")
    let ta = document.querySelector("#work").querySelectorAll("textarea")
    for(let i = 0; i < ta.length; i++){
    if (inps[i].checked) {
        work_done.push(ta[i].value)
    }else{
        work_in_progress.push(ta[i].value)
    }
    }
    let res_chal = []
    let unres_chal = []
    inps = document.querySelector("#chal").querySelectorAll("input")
    ta = document.querySelector("#chal").querySelectorAll("textarea")
    for(let i = 0; i < ta.length; i++){
    if (inps[i].checked) {
        res_chal.push(ta[i].value)
    }else{
        unres_chal.push(ta[i].value)
    }
    }
    fetch("http://localhost:8000/dsr", {
    method: "POST",
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        mentor: document.querySelector("#mentor").value,
        week: document.querySelector("#week").value,
        date: document.querySelector("#date").value,
        res_chal: document.querySelector("#res_chal").value,
        ccl: document.querySelector("#ccl").value,
        ndp: document.querySelector("#ndp").value,
        work_done: work_done,
        work_in_progress: work_in_progress,
        res_chal: res_chal,
        unres_chal: unres_chal
    })
    }).then(res => {
        let frame = window.parent.document.querySelector("#pdf")
        if (res.ok){
            res.blob().then(k => {
            url = URL.createObjectURL(k)
            frame.src = url
        })}
        else{
            res.json().then(k => {
                alert(k)
            })
        } 
    })
})