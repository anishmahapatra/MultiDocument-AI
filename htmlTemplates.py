css = '''
<style>
.chat-message {
    padding: 1.5rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    max-width: 80%;
}

.chat-message.user {
    background-color: #2b313e;
    border-left: 5px solid #4CAF50;
}

.chat-message.bot {
    background-color: #475063;
    border-left: 5px solid #FF5722;
}

.chat-message .avatar {
    width: 15%;
    margin-right: 1rem;
}

.chat-message .avatar img {
    max-width: 60px;
    max-height: 60px;
    border-radius: 50%;
    object-fit: cover;
}

.chat-message .message {
    width: 85%;
    padding: 0 1.5rem;
    color: #fff;
    font-size: 16px;
    line-height: 1.5;
}

.sidebar .sidebar-content {
    padding: 1rem;
    border-radius: 10px;
    background-color: #3E4E63;
    margin-bottom: 1rem;
    color: #fff;
}

.sidebar h2 {
    color: #FF5722;
}

.sidebar p {
    font-size: 14px;
    line-height: 1.6;
    margin: 0;
}

.header {
    background-color: #1F2A40;
    color: #FF5722;
    padding: 1rem;
    border-radius: 10px;
    text-align: center;
}

</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/yXWS4NR/Designer.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/7yWvjTZ/Anish-Mahapatra.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''