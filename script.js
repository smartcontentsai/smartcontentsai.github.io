// 1. Loading Screen
window.addEventListener('load', () => {
    setTimeout(() => {
        const loader = document.getElementById('loader');
        loader.style.opacity = '0';
        setTimeout(() => loader.style.display = 'none', 800);
    }, 2500);
});

// 2. Chatbot Logic
function toggleChat() {
    const chat = document.getElementById('aiChat');
    chat.style.display = (chat.style.display === 'flex') ? 'none' : 'flex';
}

function sendMsg() {
    const input = document.getElementById('chatIn');
    const box = document.getElementById('messages');
    if(!input.value) return;

    // User message
    const uDiv = document.createElement('div');
    uDiv.className = 'msg user';
    uDiv.innerText = input.value;
    box.appendChild(uDiv);

    const q = input.value.toLowerCase();
    input.value = '';

    // Bot Response
    setTimeout(() => {
        const bDiv = document.createElement('div');
        bDiv.className = 'msg bot';
        
        let res = "Մանրամասների համար գրեք Instagram-ին՝ @smartcontent_ai";
        
        if(q.includes("բարև", "barev", "voxjuyn", "barev dzez", "բարև ձեզ")) res = "Ողջույն! SmartContent AI-ն ողջունում է ձեզ 2050 թվականից:";
        if(q.includes("գին") || q.includes("պատվեր")) res = "Պատվերների և գների համար կարող եք կապնվել մեր Instagram-ին կամ Telegram-ին (@SmartContentAI):";
        
        bDiv.innerText = res;
        box.appendChild(bDiv);
        box.scrollTop = box.scrollHeight;
    }, 600);
}