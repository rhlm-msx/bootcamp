let lambda_url = "http://localhost:8000"
let code = `
<page>
        <text value="title"/>
        <info>
            <text value="name"/>
            <text value="email"/>
        </info>
        <banners/>
        <products/>

</page>
`


document.getElementById("xml_code").innerText = code
document.querySelector("iframe").src = `${lambda_url}/format/output`
