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

const users = [ { username: 'user', password: '05c3cea53cb17d68ccb4173402d68d13f803ef78b383023373257c1340542f5caacaccd44fd70ae80387e77c2307186d758c040dc997ffad694f00c8438b0eff' }];
app.post('/register', bodyParser.json(), (req, res) => {
    const { username, clientHash } = req.body;

    const serverHash = PBKDF2(clientHash, salt, { keySize: keySize, iterations: iterations }).toString();

    if (users.find(user => user.username === username)) {
        res.json({ success: false });
    }
    else {
        console.log(`Registering user ${username} with password hash ${serverHash}`)
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