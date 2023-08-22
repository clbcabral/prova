const fs = require('fs');
const {UsersFileRepository, UsersMemoryRepository} = require('./repository');

const FILE = './users.json';
//const repository = new UsersFileRepository(FILE);
const repository = new UsersMemoryRepository();

const listUsers = function() {
    return repository.retrieve();
};

const findUser = function(userId) {
    let users = repository.retrieve();
    return users.find(u => u.id == userId);
}

const insertUser = function(user) {
    let users = repository.retrieve();
    users.push(user);
    repository.persist(users);
    return user;
};

module.exports = {
    listUsers, findUser, insertUser
}