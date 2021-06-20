//Notes on DOM manipulation on Amazon
//cm-cr-dp-review-list -- Top reviews on product page
let toggled = false
document.getElementById('info').addEventListener('click', () => {
    if (!toggled){
        toggled = true
        document.getElementById('infobox').style.display = 'block'
    } else {
        toggled = false
        document.getElementById('infobox').style.display = 'none'
    }
})