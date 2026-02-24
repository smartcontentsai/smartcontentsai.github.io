const chatWindow = document.getElementById('chat-window');
        const messagesContainer = document.getElementById('chat-messages');

        function toggleChat() {
            chatWindow.style.display = (chatWindow.style.display === 'none' || chatWindow.style.display === '') ? 'flex' : 'none';
        }

        function openChatWithMsg(msg) {
            toggleChat();
            addMsg(msg, 'user');
            processAI(msg);
        }

        function addMsg(text, sender) {
            const div = document.createElement('div');
            div.className = `msg ${sender}`;
            div.innerText = text;
            messagesContainer.appendChild(div);
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }

        async function sendMessage() {
            const input = document.getElementById('user-input');
            const text = input.value.trim();
            if(!text) return;
            addMsg(text, 'user');
            input.value = '';
            processAI(text);
        }

        async function processAI(text) {
            document.getElementById('typing').style.display = 'block';
            try {
                
                const res = await fetch('https://backend-lvew.onrender.com/chat', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({message: text})
                });
                const data = await res.json();
                addMsg(data.reply, 'bot');
            } catch(e) {
                addMsg("Ներողություն, կապի սխալ: Սերվերն անջատված է:", "bot");
            } finally {
                document.getElementById('typing').style.display = 'none';
            }
        }

        // Initial welcome

        setTimeout(() => addMsg("Ողջույն! Ես SmartContentAI-ի օգնականն եմ: Ինչպե՞ս կարող եմ օգնել:", "bot"), 4000);
