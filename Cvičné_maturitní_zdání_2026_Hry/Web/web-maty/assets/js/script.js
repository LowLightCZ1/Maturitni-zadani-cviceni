const slots = document.querySelectorAll("h2");
let interval;

let slotValues = [0,0,0]

function slotBtnFunc(button){
    const clicked = button.classList.contains("clicked");

    if(!clicked){
        button.classList.add("clicked");
        button.textContent = "STOP";
        interval = setInterval(() => {slots.forEach(s => s.innerHTML = Math.floor(Math.random() * 10))}, 100)
    }
    else{ 
        button.classList.remove("clicked");
        button.textContent = "HRA";
        slots.innerHTML = "";
        clearInterval(interval);
        
        slotValues = Array.from(slots).map(s => Number(s.textContent));
        checkWin(slotValues);
    }

    function checkWin(values){
        const win = values.every(val => val===values[0]);

        if(win){
            alert("JACKPOT! Všechna čísla jsou: " + values[0]);
        }
        else{
            
        }
    }

}
