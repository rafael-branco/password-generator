function randomIntFromInterval(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

function copyToClipboard(){

    let inputText = document.getElementById('password').value;

    if(inputText != '' || inputText != NaN){
        navigator.clipboard.writeText(inputText);
    }

    const clipboardSVG = document.querySelector('#copy-to-clipboard svg');
    const clipboardCheck = document.querySelector('#copy-to-clipboard img')

    clipboardSVG.classList.add('display-none');
    clipboardCheck.classList.remove('display-none');

    setTimeout(() => {
        clipboardSVG.classList.remove('display-none');
        clipboardCheck.classList.add('display-none');
    }, 3000);

}
  
function getRandomCharacter(characters){
    return characters[randomIntFromInterval(0, characters.length - 1)]
}

function updateValue(val) {
    document.getElementById('value-display').innerText = val;
}

function countActiveSelection(){
    const buttons = document.querySelectorAll('.character-inclusions button');
    let counter = 0;
    for (const button of buttons) {
        if (button.classList.contains('selected')) {
            counter++;
        }
    }
    return counter;
}

function toggleSelection(button) {

    if(countActiveSelection() > 1 || !button.classList.contains('selected')){
        button.classList.toggle('selected');
        generatePassword(button);
    }

}

function shuffleString(str) {

    let arr = str.split('');
    
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr.join('');
}

function generatePassword() {

    let selectedCharacters = "";

    let passwordSetup = {
        "configurations": [
            {
                "name": "uppercase",
                "is_active": true,
                "setup": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            },
            {
                "name": "lowercase",
                "is_active": true,
                "setup": "abcdefghijklmnopqrstuvwxyz"
            },
            {
                "name": "numbers",
                "is_active": true,
                "setup": "0123456789"
            },
            {
                "name": "symbols",
                "is_active": true,
                "setup": "!@#$%^&*()-_=+[]{}|;:,.<>?/`~"
            }
        ]
    };

    const buttons = document.querySelectorAll('.character-inclusions button');

    buttons.forEach(button => {
        const isSelected = button.classList.contains('selected');
        const id = button.id.split('-').pop(); 

        passwordSetup.configurations.forEach(config => {
            if (config.name == id) {
                config.is_active = isSelected;
            }
        });
    });

    let initialPassword = '';

    passwordSetup.configurations.forEach(config => {
        if (config.is_active) {
            selectedCharacters += config.setup;
            initialPassword += getRandomCharacter(config.setup);
        }
    });

    let passwordLength = parseInt(document.getElementById('password-length').value);

    let password = "";
    for (let i = 0; i < passwordLength - initialPassword.length; i++) {
        password += getRandomCharacter(selectedCharacters);
        
    }

    password = initialPassword + password;
    password = shuffleString(password);
    
    document.getElementById('password').setAttribute('value', password)
}