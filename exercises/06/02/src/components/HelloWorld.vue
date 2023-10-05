<template>
  <div class="container">
    <form @submit.prevent="register" class="form">
      <h1>Register User</h1>
      <input type="text" v-model="registerUsername" placeholder="Username" class="input-field" />
      <input type="password" v-model="registerPassword" placeholder="Password" class="input-field" />
      <button type="submit" class="submit-button">Register User</button>
    </form>
    <p v-if="registerMessage" class="message">{{ registerMessage }}</p>

    <form @submit.prevent="login" class="form">
      <h1>Login</h1>
      <input type="text" v-model="loginUsername" placeholder="Username" class="input-field" />
      <input type="password" v-model="loginPassword" placeholder="Password" class="input-field" />
      <button type="submit" class="submit-button">Login</button>
    </form>
    <p v-if="loginMessage" class="message">{{ loginMessage }}</p>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue';
import axios from 'axios';
// @ts-ignore
import PBKDF2 from 'crypto-js/pbkdf2';

const salt = "somesalt"
const keySize = 512 / 32;
const iterations = 1000;
const baseUrl = 'http://localhost:3000';

export default {
  setup() {
    const registerUsername = ref('');
    const registerPassword = ref('');
    const loginUsername = ref('');
    const loginPassword = ref('');
    const registerMessage = ref('');
    const loginMessage = ref('');

    const hashPassword = (password: string) => {
      return PBKDF2(password, salt, { keySize, iterations }).toString();
    };

    const register = async () => {
      const clientHash = hashPassword(registerPassword.value);
      try {
        const response = await axios.post(`${baseUrl}/register`, { username: registerUsername.value, clientHash });
        registerMessage.value = response.data.success ? 'User created' : 'User creation failed';
      } catch (error) {
        registerMessage.value = 'An error occurred';
        console.log(error);
      }
    };

    const login = async () => {
      const clientHash = hashPassword(loginPassword.value);
      try {
        const response = await axios.post(`${baseUrl}/login`, { username: loginUsername.value, clientHash });
        loginMessage.value = response.data.success ? 'Login successful' : 'Login failed';
      } catch (error) {
        loginMessage.value = 'An error occurred';
        console.log(error);
      }
    };

    return {
      registerUsername,
      registerPassword,
      loginUsername,
      loginPassword,
      register,
      login,
      registerMessage,
      loginMessage
    };
  },
};
</script>



<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

.form {
  margin: 10px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 20px;
}

.input-field {
  margin-bottom: 15px;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 3px;
  width: 80%;
}

.submit-button {
  padding: 10px 20px;
  background-color: #227a3b;
  color: white;
  border: none;
  border-radius: 3px;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #45a049;
}

.message {
  color: red;
  font-size: 16px;
  margin-top: 10px;
}
</style>