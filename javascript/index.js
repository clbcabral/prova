const {listUsers, findUser, insertUser} = require('./service');
const express = require('express');

const app = express();
app.use(express.json());
app.use(express.urlencoded({
    extended: true
}));
app.set('view engine', 'pug');
app.set('views', './templates')

app.get('/', (req, res) => {
    res.render('index.pug', {
        'nums': [1,2,3,4]
    });
});

app.get('/users', (req, res) => {
    let users = listUsers();
    res.json(users);
});

app.get('/user/:id', (req, res) => {
    let user = findUser(req.params.id);
    res.json(user);
});

app.post('/user', (req, res) => {
    let newUser = insertUser(req.body);
    res.json(newUser);
});

const server = app.listen(8000, () => {
    console.log(`Escutando na porta ${server.address().port}.`);
});