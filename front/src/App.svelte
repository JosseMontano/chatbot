<script lang="ts">
  import Call from "./icons/call.svelte";
  import { fetchData } from "./utilities/fetch";
  import ChatbotPng from "./assets/chatBot.png";

  let msgInput = "";
  let mensajes = [];

  const addMessage = async () => {
    const res = await fetchData("chat/" + msgInput);
    if (msgInput != "") {
      const addMsgUser = {
        type: "user-message",
        msg: msgInput,
      };

      const addMsgBot = {
        type: "bot-message",
        msg: res.message,
      };

      mensajes = [...mensajes, addMsgUser];
      mensajes = [...mensajes, addMsgBot];
      msgInput = "";

      return;
    }
  };
</script>

<main>
  <div class="chat-container">
    <div class="header">
      <div class="container_title">
        <img src={ChatbotPng} alt="chatbot" />
        <h3>ChatComidas</h3>
      </div>
      <Call />
    </div>

    <div class="chat">
      {#each mensajes as msg}
        <div class={`message ${msg.type}`}>{msg.msg}</div>
      {/each}
    </div>

    <div class="input-container">
      <input
        type="text"
        id="user-input"
        placeholder="Escribe un mensaje..."
        bind:value={msgInput}
        on:input={(e) => {
          //@ts-ignore
          msgInput = e.target.value;
        }}
      />
      <button id="send-button" on:click={() => addMessage()}>Enviar</button>
    </div>
  </div>
</main>

<style lang="scss">
  $primary-color: #713aff;
  $secondary-color: #ddd;
  $border-color: #ddd;

  main {
    font-family: Arial, sans-serif;
    background-color: #ffffff;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: flex-end; /* Alinea el chat a la derecha */
    align-items: flex-end; /* Alinea el chat abajo */
  }

  .header {
    background-color: $primary-color;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    padding: 2px 10px;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 70px;

    .container_title {
      display: flex;
      align-items: center;
      justify-content: flex-start;
      gap: 10px;
      color:#fff;
    }
    img {
      width: 55px;
      height: 55px;
    }
  }

  .chat-container {
    width: 100%;
    height: 100%;
    margin: 20px;
    display: flex;
    flex-direction: column;
    margin-top: 70px;
  }

  .chat {
    padding: 20px;
    max-height: 490px;
    overflow-y: auto;
    display: flex;
    flex-direction: column;
  }

  .message {
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 5px;
    max-width: 70%;
  }

  .user-message {
    background-color: $primary-color;
    color: white;
    align-self: flex-end;
  }

  .bot-message {
    background-color: $secondary-color;
    color: rgba(30, 30, 30, 0.8);
    align-self: flex-start;
  }

  .input-container {
    position: absolute;
    top: 80%;
    left: 50%;
    transform: translate(-50%, 50%);
    width: 80%;
    display: flex;
    align-items: center;
    padding: 20px;
    border-top: 1px solid $border-color;

    input[type="text"] {
      flex: 1;
      padding: 10px;
      border: none;
      border-radius: 5px;
    }

    button {
      background-color: $primary-color;
      color: white;
      border: none;
      border-radius: 5px;
      padding: 10px 20px;
      margin-left: 10px;
      cursor: pointer;
    }
    button:disabled {
      color: red;
    }
  }
</style>
