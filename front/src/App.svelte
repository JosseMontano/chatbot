<script lang="ts">
  import { fetchData } from "./utilities/fetch";

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

  .chat-container {
    width: 100%;
    height: 100%;
    margin: 20px; 
    display: flex;
    flex-direction: column;
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
    color: rgba(30, 30, 30,.8);
    align-self: flex-start;
  }

  .input-container {
    position: absolute;
    top:80%;
    left: 50%;
    transform: translate(-50%,50%);
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
