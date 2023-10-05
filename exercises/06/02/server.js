import express from 'express';
import bodyParser from 'body-parser';
import PBKDF2 from "crypto-js/pbkdf2";

const cors = require('cors');
const app = express();
app.use(cors());
const port = 3000;

const salt = 'somesalt';
const keySize = 512/32;
const iterations = 1000;

const users = [ { username: 'user1', password: 'password1' }, { username: 'user2', password: 'password2' } ];
app.post('/register', bodyParser.json(), (req, res) => {
    const { username, clientHash } = req.body;

    const serverHash = PBKDF2(clientHash, salt, { keySize: keySize, iterations: iterations }).toString();

    if (users.find(user => user.username === username)) {
        res.json({ success: false });
    }
    else {
        users.push({ username, password: serverHash });
        res.json({ success: true });
    }
});

app.post('/login', bodyParser.json(), (req, res) => {
    const { username, clientHash } = req.body;

    if (users.find(user => user.username === username)) {

        const serverHash = PBKDF2(clientHash, salt, { keySize: keySize, iterations: iterations }).toString();

        if (users.find(user => user.username === username && user.password === serverHash)) {
            res.json({ success: true });
        } else {
            res.json({ success: false });
        }
    } else {
        res.json({ success: false });
    }
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}!`)
});